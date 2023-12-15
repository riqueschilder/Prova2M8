import gradio as gr
import openai
import os
import pyttsx3

openai.api_key = ""  # Substitua com sua chave API do OpenAI

messages = [{"role": "system", "content": 'Voce eh um tradutor, repita o que eu te falar em ingles.'}]

def transcribe(audio, text):
    global messages
    if audio:
        audio_filename_with_extension = audio + '.wav'
        os.rename(audio, audio_filename_with_extension)
    
        audio_file = open(audio_filename_with_extension, "rb")
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    
        messages.append({"role": "user", "content": transcript["text"]})

        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

        system_message = response["choices"][0]["message"]
        messages.append(system_message)

        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
        engine.say(system_message['content'])
        engine.runAndWait()

        chat_transcript = ""
        for message in messages:
            if message['role'] != 'system':
                chat_transcript += message['role'] + ": " + message['content'] + "\n\n"
        return chat_transcript
    else:
        messages.append({"role": "user", "content": text})
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
        system_message = response["choices"][0]["message"]
        messages.append(system_message)
        engine = pyttsx3.init()
        engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
        engine.say(system_message['content'])
        engine.runAndWait()
        chat_transcript = ""
        for message in messages:
            if message['role'] != 'system':
                chat_transcript += message['role'] + ": " + message['content'] + "\n\n"
        return chat_transcript

    

ui = gr.Interface(fn=transcribe, inputs=[gr.Audio(type="filepath"), 'text'], outputs="text")
ui.launch()

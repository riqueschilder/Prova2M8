# Conversor de Áudio para Texto e Tradutor 
Este código implementa um sistema de conversão de áudio para texto e tradução automática utilizando a API do OpenAI e a biblioteca Gradio. O objetivo é permitir que o usuário forneça áudio em português e receba a transcrição em inglês, com a capacidade de interagir através de texto.

## Requisitos 
Certifique-se de ter os seguintes requisitos instalados antes de executar o código:

Python 3.x Bibliotecas necessárias: gradio(VERSAO MAIN: pip install https://gradio-builds.s3.amazonaws.com/7ba8c5da45b004edd12c0460be9222f5b5f5f055/gradio-4.9.1-py3-none-any.whl), openai, os, pyttsx3 Configuração Antes de iniciar, substitua a variável openai.api_key com sua chave de API do OpenAI para garantir o acesso correto aos serviços.

## Uso
O código oferece duas opções de entrada: áudio ou texto. Se a entrada for áudio, o sistema transcreverá o áudio fornecido usando a API de transcrição de áudio do OpenAI. Em seguida, traduzirá a transcrição para inglês usando o modelo de linguagem GPT-3.5-turbo. O resultado da tradução será falado usando o mecanismo Text-to-Speech (TTS) do pyttsx3.

Se a entrada for texto, o sistema utilizará diretamente o modelo GPT-3.5-turbo para gerar uma resposta traduzida.

Dependências de Voz O código usa a biblioteca pyttsx3 para a síntese de voz. Certifique-se de que o pacote está instalado e configure a voz desejada ajustando a propriedade 'voice'.

Interface Gráfica O código utiliza a biblioteca Gradio para criar uma interface simples. A interface permite a entrada de áudio ou texto e exibe a saída traduzida em tempo real.

Como Executar Execute o código e a interface gráfica será lançada automaticamente. Você pode interagir com ela fornecendo áudio ou texto e observar a resposta traduzida.


https://github.com/riqueschilder/Prova2M8/assets/99187952/3eef06dd-fdb1-4473-9773-e9222362b2aa

não consegui fazer o audio do pysttx3 sair no video, mas ele fala...

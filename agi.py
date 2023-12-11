# to converting text to speech
import pyttsx3 #pip install pyttsx3 ==  text data into voice/speech
import os
import openai
import speech_recognition as sr #pip install SpeechRecognition == voice/audio into text data 
from dotenv import load_dotenv
import openai

load_dotenv()  # This loads the environment variables from .env file


openai.api_key = os.getenv('OPENAI_API_KEY')

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly. \n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help ypu today?\nHuman: ",

## Speak Function
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def STT():
    r = sr.Recognizer()
    with sr. Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r. listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print("Human Said :" +query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


def gpt_output(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=True,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["Human:"," AI:"]
    )
    data = response.choices[0].text
    speak(data)
    print(data)
    # return data


# gpt_output("who is the founder of python programming language")
STT()
while True:
    query = STT()
    gpt_output(query)
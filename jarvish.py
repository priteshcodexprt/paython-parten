from email.mime import audio
from unittest import result
import pyttsx3
import speech_recognition as sr
import datetime
from time import ctime
import time
import os
import webbrowser
import smtpd

import youtube_dl

engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak ("Good Morning!")

    elif hour >= 12 and hour<18:
        speak("Good Afternoon!")
    else :
        speak ("Good Morning!")
    speak("I am jarvis sir . Please  tell me how may i help you ")

def takeCommand():


    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try :
        print("Recognizing ...")
        query =r.recognize_google(audio , language="en-in")
        print(f"user said :{query}\n")

    except Exception as e:
        # print(e)
        print("say that again please ...")
        return "None"
    return query

if __name__ == "main ":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia ...')
            query =query.replace("wikipedia...")
            result=wikipedia.summary(query,sentence=2)
            speak("According to Wikipedia  ")
            print(result)
            speak(result)

        elif 'open youtube'in query:    
            webbrowser.open("youtube.com")
            





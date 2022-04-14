import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import os

eng=pyttsx3.init()
voices=eng.getProperty('voices')
eng.setProperty('voice',voices[0].id)
print('\nHi im Jarvis...your personal assistant...')
eng.setProperty('rate',150)
eng.say("Hi i am Jarvis ...your personal assistant")
eng.runAndWait()

recognizer=sr.Recognizer()

def cmd():

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        print('\nHappy to help you...')
        print('Ask what you want...')
        recordedaudio=recognizer.listen(source)
    try:
        
        command=recognizer.recognize_google(recordedaudio,language="en_US")
        command=command.lower()
        print('\nYour message: ',format(command))

    except Exception as ex:
        print(ex)

    if 'chrome' in command:

        a='Opening chrome..'

        eng.say(a)

        eng.runAndWait()

        programName = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        subprocess.Popen([programName])

    if 'time' in command:

        time = datetime.datetime.now().strftime('%I:%M %p')

        print(time)

        eng.say(time)

        eng.runAndWait()

    if 'play' in command:

        a='opening youtube..'

        eng.say(a)

        eng.runAndWait()

        pywhatkit.playonyt(command)

    if 'youtube' in command:

        b='opening youtube'

        eng.say(b)

        eng.runAndWait()

        webbrowser.open('www.youtube.com')
        
    if 'whatsapp' in command:
        
        c='opening whatsapp...'

        eng.say(c)

        eng.runAndWait()
        webbrowser.open('web.whatsapp.com')
    
while True:

    cmd()
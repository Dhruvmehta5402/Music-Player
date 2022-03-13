import playsound
import os
import random
import math
import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# For listening and recognizing
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 2
        #r.dynamic_energy_threshold = True
        #r.energy_threshold = 2000
        audio = r.listen(source)

    try:
        print('Recognizing..')
        query = r.recognize_google(audio,  language='en-in')
        print(f'User said: {query} \n')
    except Exception as e:
        print(e)
        print('say that again please')
        return "None"
    return query

directory = "Songs"
path = "Songs\\"
songList = []
for filename in os.listdir(directory):
    songList.append(filename)


while True:
    i = math.floor(random.random() * len(songList))
    print(songList[i])
    speak("Now Playing " + songList[i])
    songName = path + songList[i]
    query = takeCommand().lower()
    if 'skip' in query:
        continue
    try:
        playsound.playsound(songName)
    except:
        speak("Error in file name. Sorry!")
    

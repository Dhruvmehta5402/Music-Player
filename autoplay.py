import playsound
import os
import random
import math
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

#Speak Function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

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
    try:
        playsound.playsound(songName)
    except:
        speak("Error in file name. Sorry!")
    

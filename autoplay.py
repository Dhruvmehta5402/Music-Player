import playsound
import os
import random
import math


directory = "Songs"
path = "Songs\\"
songList = []
for filename in os.listdir(directory):
    songName = path + filename
    songList.append(songName)


while True:
    i = math.floor(random.random() * len(songList))
    print(songList[i])
    playsound.playsound(songList[i])

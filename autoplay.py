import playsound
import os


directory = "Songs"
path = "Songs\\"
for filename in os.listdir(directory):
    print(path + filename)
    songname = path + filename
    playsound.playsound(songname)

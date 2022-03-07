import playsound
import os


directory = "Songs"
path = "C:\\Users\\Dhruv\\musicplayer\\Songs\\"
for filename in os.listdir(directory):
    print(path + filename)
    songname = path + filename
    playsound.playsound(songname)

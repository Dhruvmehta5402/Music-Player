# Music-Player
Music Player to autoplay music offline on computer/pen drive

I was playing some music that I had on my Pen Drive on my laptop and for some reason,  
the default music player for Windows (Groove Music) did not have an autoplay option  
and every time a song ended I had to go back to the folder to play the next song.  
To avoid this, I wrote this python script using the playsound module to play songs from my song folder.  
I even added a shuffle feature and incorporated text to speech to speak the song name before the song is played.  

## Functioning
Create a new Folder called `Songs` in the same folder as the code and add all your song files to the folder.  
You can then run the code using the command
```bash
$ python autoplay.py
```

## Requirements
TODO: Add a requirements.txt
You will need to install playsound, os, pyttsx3 for the code to work as desired.

## Future Features
I am planning on adding a hands-free skip feature to the player using Voice recognition. Also want to add a feature to display the Time Remaining in a song. Features should hopefully be added within a week or 2 😄


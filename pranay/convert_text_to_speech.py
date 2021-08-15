# pip install pyttsx3

#convert text into speech

import pyttsx3
engine=pyttsx3.init()
with open("C:\\Users\\yjasw\\OneDrive\\Documents\\HTML\\strength_weakness.txt") as pp:
    x=pp.read()
engine.say(x)
engine.runAndWait()
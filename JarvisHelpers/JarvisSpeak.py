# -*- coding: utf-8 -*-
from gtts import gTTS
from playsound import playsound

LANGUAGE = 'en'


def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString,lang=LANGUAGE)
    tts.save("./sounds/audio.mp3")
    playsound("./sounds/audio.mp3")
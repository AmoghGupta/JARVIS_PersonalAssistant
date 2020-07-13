#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:40:45 2020

@author: agupta
"""

import speech_recognition as sr
from gtts import gTTS 
from playsound import playsound
import os

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Language in which you want to convert 
language = 'en'

with sr.Microphone() as source:
    while(1):
        speech = gTTS(text="Say something", lang=language, slow=False)
        #speech.save("voice.mp3")
        playsound("./sounds/talk.mp3")
        
        audio_text = r.listen(source,20)
        #print("Time over, thanks")
        
        try:
            # using google speech recognition
            if r.recognize_google(audio_text):
            
               print(r.recognize_google(audio_text))
               if r.recognize_google(audio_text).lower()  == 'Hello Jarvis'.lower():
                   speech = gTTS(text="What can I do for you?", lang=language, slow=False)
                   speech.save("./sounds/jarvis_what.mp3")
                   playsound("./sounds/jarvis_what.mp3")
        except:
             print("Sorry, I did not get that")

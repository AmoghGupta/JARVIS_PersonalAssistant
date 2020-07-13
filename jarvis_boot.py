# -*- coding: utf-8 -*-

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7
@author: agupta
"""
import sys
sys.path.append('./JarvisHelpers/')
import speech_recognition as sr 
from JarvisHelpers import *
from JarvisHelpers import JarvisListen
import GLOBALS
import _thread
import GoogleAuthenticate
import Greet
import JarvisSpeak
import FaceAuthorization

def mainfunction(source):
    usertext ='none'
    audio_text = r.listen(source,2000)
    try:
        if r.recognize_google(audio_text):
            usertext = r.recognize_google(audio_text)
            print(usertext)
    except:
            pass
    return usertext

if __name__ == "__main__":
    try:
        if FaceAuthorization.imageValidation():
            #doing google authentication on a separate thread
            _thread.start_new_thread(GoogleAuthenticate.authenticateGoogle, ())
            r = sr.Recognizer()
            with sr.Microphone() as source:
                JarvisSpeak.speak("Hello Amogh,"+Greet.greet())
                print("Started listening....")
                print("Say Jarvis Activate to activate")
                print("Say Jarvis Deactivate to Deactivate")
                while GLOBALS.KILL_MYSELF<1:
                   data = mainfunction(source)
                   JarvisListen.jarvis(data)
            
            #terminate the thread if active when main is killed
            # if GLOBALS.CAL_EVENT_THREAD.isAlive(): 
            #     GLOBALS.CAL_EVENT_THREAD.stop()
            if GLOBALS.CAL_EVENT_THREAD.isAlive(): 
                print("Waiting for pending threads to complete")
            GLOBALS.CAL_EVENT_THREAD.join()
        else:
            print("Failed to authorized you.")
            JarvisSpeak.speak("Failed to authorize you.")
            JarvisSpeak.speak("Terminating myself.")
        
    except Exception as e:
        print("Error ",e)
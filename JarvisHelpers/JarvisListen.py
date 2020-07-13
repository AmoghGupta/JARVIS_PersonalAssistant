# -*- coding: utf-8 -*-
import JarvisSpeak
import GLOBALS
import IntentIdentifier

def jarvis(usertext):
    try:
        usertext= usertext.lower()
        
        if  "jarvis activate" in usertext:
            JarvisSpeak.speak("Jarvis Activated")
            GLOBALS.ACTIVATED = True        
            
        if  "jarvis deactivate" in usertext:
            JarvisSpeak.speak("Jarvis deactivated")
            GLOBALS.ACTIVATED = False        
            
        if "jarvis exit" in usertext:
                JarvisSpeak.speak('I am terminating myself')
                GLOBALS.KILL_MYSELF =2
                return        
            
        if GLOBALS.ACTIVATED == True:        
                IntentIdentifier.myIntent(usertext)
    except:
         print("Some issues while listening")
        
            
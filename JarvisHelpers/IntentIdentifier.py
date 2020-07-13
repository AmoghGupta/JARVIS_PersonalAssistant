# -*- coding: utf-8 -*-
import TaskIdentifier
from Tasks import JarvisWiki
import JarvisSpeak
from datetime import date
from time import ctime
from Tasks import GoogleCalendarTasks
import GLOBALS
from Tasks import OfficeStuff



SUPPORTED_INTENTS = {
           "open browser": "open browser",
           "show news":"show news",
           "play music":"play music",
           "play video":"play video",
           "current time":"current time",
           "date today":"date today",
           "wiki1":"what is (your question)",
           "wiki2":"who is (your question)",
           "upcoming events":"upcoming events",
           "create event":"create event",
           "where is":"where is (location)",
           "open url": "open url (ex: open url google.com)",
           "open app": "open app (appname)",
           "close app": "close app (appname)"
        }
    
    
def myIntent(usertext):
    try:
        if "help me" in usertext:
            JarvisSpeak.speak("Below are the commands which I support currently.")
            #Supported stuff
            intent_dict = {k: v.upper() for k, v in SUPPORTED_INTENTS.items()}
            for value in intent_dict.values():
                print(value+'\n')
        
        if "where is" in usertext or "location" in usertext:
            TaskIdentifier.getLocation(usertext)
            return
        
        if "open browser" in usertext:
            TaskIdentifier.openBrowser()
            return
        
        if "show news" in usertext:
            TaskIdentifier.getNews(usertext)
            
        if "play music" in usertext:
            TaskIdentifier.music()
            return
        
        if "play video" in usertext:
            TaskIdentifier.video()
            return
            
        if "current time" in usertext:
            JarvisSpeak.speak(ctime())
            return
        
        if "date today" in usertext:
            JarvisSpeak.speak(date.today())
            return
        
        if "upcoming events" in usertext:
            if GLOBALS.IS_GOOGLE_SERVICE_AUTHENTICATED:
                GoogleCalendarTasks.fetchUpcomingEvents()
            else:
                print("Not authorized to use google..")
            return
       
        if "create event" in usertext:
            if GLOBALS.IS_GOOGLE_SERVICE_AUTHENTICATED:
                GoogleCalendarTasks.createAnEvent()
            else:
                print("Not authorized to use google..")
            return
            
        if "what is" in usertext or "who is" in usertext:
            JarvisWiki.readWiki(usertext)
            return
        
        
        if "open url" in usertext:
            TaskIdentifier.openWebsite(usertext)
            return
        
        if "app" in usertext:
            TaskIdentifier.appHandler(usertext)
            return
        
        if "generate token" in usertext:
            OfficeStuff.generateSID()
            return
        
    except Exception as ex:
        print("Intent not clear: {}",format(ex))
    
    #JarvisWiki.genericWiki(usertext)
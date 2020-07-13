# -*- coding: utf-8 -*-

import subprocess
import os
import psutil    


def appCheck(userText):
    if "open app" in userText:
        openApp(userText)
   
    if "close app" in userText:
        closeApp(userText)
    
def isAppAlreadyRunning(appName):
     found = False
     for myprocess in [p.name().lower() for p in psutil.process_iter()]:
         if appName in myprocess:
             found = True
             break
    
     return found

def openApp(userText):    
    try:
        appName = userText.split("open app ")[1]
        appFound = False
        #print(appName)
        appsList = os.listdir("/Applications")
        print("getting all apps installed in Applications..")
        #print(appsList)
        print("checking if the app exists in Applications..")
        
        if not isAppAlreadyRunning(appName):
    
            for application in [x.lower() for x in appsList]:
                if appName in application:
                    print("App found {}..".format(application))
                    appName=application
                    appstr="/Applications/{}".format(appName)
                    subprocess.call(["/usr/bin/open", "-n", "-a",appstr])
                    appFound= True
                    break
             
            if not appFound:
                 print("No such app found")
        else:
            print("App already running..")
     
    except Exception as ex:
        print("Some issue while opening website: "+ex)

        
def closeApp(userText):    
    try:
        print("Sorry I dont have permissions to close apps")

    except Exception as ex:
        print("Some issue while closing the app: "+ex)
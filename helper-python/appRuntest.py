# -*- coding: utf-8 -*-

import psutil    
import os


def isAppAlreadyRunning(appName):
     found = False
     for myprocess in [p.name().lower() for p in psutil.process_iter()]:
         if "postman" in myprocess:
             found = True
             break
    
     return found
 
    
print(isAppAlreadyRunning())
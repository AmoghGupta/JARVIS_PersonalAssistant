# -*- coding: utf-8 -*-
import datetime

def greet():
    currentDT = datetime.datetime.now()
    hr = currentDT.hour
        
    if hr>=0 and hr<12: 
       return "Good Morning"
    elif hr>=12 and hr<18 : 
        return "Good afternoon"
    elif hr>=18 and hr<24 : 
        return "Good evening"
        
        

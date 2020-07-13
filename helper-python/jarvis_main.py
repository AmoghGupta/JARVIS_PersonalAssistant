#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 20:39:00 2020

@author: agupta
"""


import os
import webbrowser
import subprocess
import speech_recognition as sr


os.system("say Welcome to Amoghs MAC!!!" )
webbrowser.open('http://www.google.com')
os.system("""osascript -e 'tell app "Notes" to open'""")


apps_list = ['/Applications/Slack.app',
             '/Applications/Postman.app',
             '/Applications/Anaconda-Navigator.app',
             '/Users/agupta/Downloads/VisualStudioCode.app']

for appPath in apps_list:
    os.system(f"open {appPath}")
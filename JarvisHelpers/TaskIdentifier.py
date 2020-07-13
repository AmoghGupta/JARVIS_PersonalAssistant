# -*- coding: utf-8 -*-
import sys
sys.path.append('./Tasks/')
import webbrowser
from Tasks import News
from Tasks import Location
from Tasks import AppHandler

def openBrowser():
    webbrowser.open('https://www.google.com')

def music():
    #os.system(f"open /Applications/iTunes.app")
    webbrowser.open('https://www.gaana.com')
    
def video():
    webbrowser.open('https://www.youtube.com')
    
def appHandler(userText):
    AppHandler.appCheck(userText)
    
def openWebsite(userText):
    try:
        userText = userText.split("url ")[1]
        url = userText
        print(url)
        webbrowser.open('https://{}'.format(url))
    except Exception as ex:
        print("Some issue while opening website: "+ex)
    
def getLocation(userText):
    Location.openLocation(userText)
    
def getNews(usertext):
    News.showTopNews(usertext)

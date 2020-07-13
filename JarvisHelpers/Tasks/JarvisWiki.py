# -*- coding: utf-8 -*-

import wikipedia
import JarvisSpeak


def readWiki(usertext):
    try:
        if "what is" in usertext:
            usertext = usertext.split("what is")[1]
        if "who is" in usertext:
            usertext = usertext.split("who is")[1]
        wikiresult = wikipedia.page(usertext)
        wikistring = str(wikiresult.content)
        JarvisSpeak.speak(wikistring.split(".")[0])
    except:
        JarvisSpeak.speak("No results found!")
        
    
def genericWiki(usertext):
    wikiresult = wikipedia.page(usertext)
    wikistring = str(wikiresult.content)
    JarvisSpeak.speak(wikistring.split(".")[0])
    
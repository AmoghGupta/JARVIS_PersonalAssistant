# -*- coding: utf-8 -*-
import requests
import json
import webbrowser



def displayTopNews():
    newsapikey = 'f208ac5b07294ddda461c697258a3952'
    country = 'USA'
    try:
        top_headlines = requests.get("http://newsapi.org/v2/top-headlines?sources=google-news-{}&apiKey={}".format(country,newsapikey))        
        
        json_news = json.loads(top_headlines.text)['articles']
        for article in json_news:
            print(article['description'])
            print('_____________________________')
    except:
        print("Failed to fetch news")

def showTopNews(usertext):
    url= "https://news.google.com/topstories?hl=en-IN"
    webbrowser.open(url)
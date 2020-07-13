# -*- coding: utf-8 -*-
import webbrowser


def openLocation(usertext):
    webbrowser.open('https://www.google.com/maps/search/{}'.format(usertext))

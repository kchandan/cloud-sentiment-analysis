from textblob import TextBlob
import requests
from os.path import expanduser
import os
import configparser


class analyzer:
    def __init__(self,module):
        self.module = module

    def aws(self):
        pass
    def analyze(self,text):
        self.local(text)
    def local(self,text):
        blob = TextBlob(text)
        print (text,blob.sentiment.polarity)
        
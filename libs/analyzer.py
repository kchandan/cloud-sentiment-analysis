from textblob import TextBlob
import requests
from os.path import expanduser
import os
import configparser
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

import matplotlib.pyplot as plt

class analyzer:
    def __init__(self):
        pass

    def aws(self):
        pass
    
    def gcp(self):
        pass
    
    def analyze_sentiment(self,text):

        self.local(text)
    def local(self,text):
        
        blob = TextBlob(text)
        print (text,blob.sentiment.polarity)
        
    def analyze_df(self,search_result):
        df=pd.DataFrame()    
        dftemp= json_normalize(search_result,'statuses')
        df=df.append(dftemp,ignore_index=True)
        tweettext=df['text']
        df.to_csv("tweets.csv")
        wordlist=pd.DataFrame();
        polarity=[]
        subj=[]
        for t in tweettext:
            tx= TextBlob(t)
            polarity.append(tx.sentiment.polarity)
            subj.append(tx.sentiment.subjectivity)

        print (tweettext)
        poltweet= pd.DataFrame({'polarity':polarity,'subjectivity':subj})
        poltweet.polarity.plot(title='Polarity')
        plt.show()
        
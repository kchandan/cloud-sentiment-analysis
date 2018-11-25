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

    def analyze_sentiment(self,text):
        tx= TextBlob(t)
    
    def bulk_detect_sentiment(self,df):
        df['Py_polarity'] = df['tweets'].apply(lambda x: TextBlob(x).sentiment.polarity)
        
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
            print(t,tx.sentiment.polarity)
        #     polarity.append(tx.sentiment.polarity)
        #     subj.append(tx.sentiment.subjectivity)

        # print (tweettext)
        # poltweet= pd.DataFrame({'polarity':polarity,'subjectivity':subj})
        # poltweet.polarity.plot(title='Polarity')
        # plt.show()
        
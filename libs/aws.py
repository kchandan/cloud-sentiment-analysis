import boto3
import json

from os.path import expanduser
import os
import configparser
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt

#'SentimentScore': {'Positive': 0.0005348395789042115,
#  'Negative': 0.002301972359418869, 'Neutral': 0.9965127110481262, 'Mixed': 0.0006505127530544996}
class aws_comp:
    def __init__(self,region):
        self.comprehend = boto3.client(service_name='comprehend', region_name=region)

    def detect_lang(self,text):
        output = self.comprehend.detect_dominant_language(Text = text)
        for lang in output['Languages']:
            # print (lang['LanguageCode'], lang['Score'])
            return lang['LanguageCode']
    
    def detect_sentiment(self,text):
        lang = self.detect_lang(text)
        return self.comprehend.detect_sentiment(Text=text, LanguageCode=lang)
    
    def bulk_detect_sentiment(self,df):
        response = self.comprehend.batch_detect_sentiment(TextList = df['tweets'].values.tolist(),LanguageCode = 'en')
        aws_score = []
        for result in response['ResultList']:
            aws_score.append(result['Sentiment'])
        df['aws_sentiment'] = aws_score

        

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
            data = self.detect_sentiment(t)
            print (t,data['Sentiment'])
            # polarity.append(data('Sentiment'))
        
        # poltweet= pd.DataFrame({'polarity':polarity})
        # poltweet.polarity.plot(title='Polarity')
        # plt.show()
    

# if __name__ == "__main__":
    # a = aws_comp('us-east-1')
    # a.detect_lang("Use access keys to make secure REST or HTTP Query protocol requests to AWS service APIs")


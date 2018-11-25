# -*- coding: utf-8 -*-
import requests
from os.path import expanduser
import os
import configparser
import json

class azure:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(expanduser("~"),".azure/credentials"))
        region = config.get('default','region')
        key1 = config.get('default','key1')
        key2 = config.get('default','key2')
        self.azure_lang_endpoint = "https://{}.api.cognitive.microsoft.com/text/analytics/v2.0/languages".format(region)
        self.azure_senti_endpoint = "https://{}.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment".format(region)
        self.key1 = key1
        self.key2 = key2
        self.headers = {
        'Content-Type': "application/json",
        'Ocp-Apim-Subscription-Key': self.key1,
        'Cache-Control': "no-cache"
        }
    def detect_language(self,text):
        response = requests.request("POST", self.azure_lang_endpoint, data=text, headers=self.headers)
        print (response)
        if response.status_code != 200:
            return (False,response.status_code)
        print (response.text)
        return (True,response.text)
    
    def detect_sentiment(self,text):
        response = requests.request("POST", self.azure_senti_endpoint, data=text, headers=self.headers)
        print (response)
        if response.status_code != 200:
            return (False,response.status_code)
        print (response.text)
        return (True,response.text)

    def bulk_detect_sentiment(self,df):
        tweets = df['tweets'].values.tolist()
        items = []
        for num, tweet in enumerate(tweets,1):
            item = {"language": "en", "id": num,"text": tweet}
            items.append(item)
        
        text = {}
        text['documents'] = items
        response = requests.request("POST", self.azure_senti_endpoint , data = json.dumps(text), headers=self.headers)
        if response.status_code == 200:
            j = json.loads(response.text)
            azure_score = []
            for doc in j['documents']:
                score =doc['score']
                azure_score.append(score)
            df['azure_score'] = azure_score
            print (df)
        else:
            print("Response for Azure Text Analytics:",response.status_code)


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
    


if __name__ == '__main__':

    a = aws()
    input_text = {"documents": [{"language": "en", "id": "1","text": "Hello world. This is some input text that I love."}]} 
    # input_text = open("a.text").read()
    # j = json.load(input_text)
    print(input_text)
    status,text = a.detect_sentiment(json.dumps(input_text))
    print(status,text)
    # if status == True:
    #     j =json.loads(text)
    #     for doc in j['documents']:
    #         for lang in doc['detectedLanguages']:
    #             print(lang['name'],lang['iso6391Name'])



        
        




        
import numpy as np
import libs.aws
import libs.azure
# import libs.gcp
import libs.local
import libs.twitter
from textblob import TextBlob
import json
import pandas as pd
import matplotlib.pyplot as plt

def download_tweets():
    tweets = libs.twitter.twitter()
    search_results = tweets.tweet_batch("trump",10)
    with open("tweets.json",'w') as f:
        json.dump(search_results,f)

def py_analyze(df):
    a = libs.local.analyzer()
    a.bulk_detect_sentiment(df)

def aws_analyze(df):
    a = libs.aws.aws_comp('us-east-1')
    a.bulk_detect_sentiment(df)

def azure_analyze(df):
    a = libs.azure.azure()
    a.bulk_detect_sentiment(df)

def analyze():
    with open("tweets.json") as f:
        search_results = json.load(f)
    data = []
    df = pd.DataFrame(columns=['tweets'])
    for num,tweet in enumerate(search_results['statuses']):
        if tweet['user']['lang'] == 'en':
            data.append(tweet['text'])
    df['tweets'] = data
    py_analyze(df)
    aws_analyze(df)
    azure_analyze(df)
    print(df)

def main():
    analyze()


def pplot():

    df=pd.DataFrame.from_csv('tweets.csv')
    tweettext=df['text']

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



if __name__ == "__main__":
    # download_tweets()
    main()
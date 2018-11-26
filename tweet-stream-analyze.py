import libs.aws
import libs.azure
# import libs.gcp
import libs.local
import libs.twitter
from textblob import TextBlob
import json
import pandas as pd
import matplotlib.pyplot as plt

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
    tweets = libs.twitter.twitter()
    search_results = tweets.tweet_batch("trump",10)
    data = []
    df = pd.DataFrame(columns=['tweets'])
    for num,tweet in enumerate(search_results['statuses']):
        if tweet['user']['lang'] == 'en':
            data.append(tweet['text'])
    df['tweets'] = data
    py_analyze(df)
    aws_analyze(df)
    azure_analyze(df)

def main():
    analyze()
    


if __name__ == "__main__":
    main()
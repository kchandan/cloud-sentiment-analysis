# import libs.aws
# import libs.azure
# import libs.gcp
import libs.analyzer
import libs.twitter
from textblob import TextBlob

        
def analyze():
    tweets = libs.twitter.twitter()
    search_results = tweets.tweet_batch("weed",10)
    a = libs.analyzer.analyzer()
    a.analyze_df(search_results)
    

def main():
    analyze()


if __name__ == "__main__":
    main()
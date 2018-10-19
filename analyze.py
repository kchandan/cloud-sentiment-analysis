import libs.aws
import libs.azure
import libs.gcp
import libs.twitter
from textblob import TextBlob

        
def analyze():
    tweets = libs.twitter.twitter()
    tweets.tweet_stream(["coffee"])
    

def main():
    analyze()


if __name__ == "__main__":
    main()
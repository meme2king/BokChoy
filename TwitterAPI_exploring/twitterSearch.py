import constants
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

def main():
    authentication = tweepy.OAuthHandler(constants.API_KEY, constants.API_SECRET_KEY)
    authentication.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_SECRET_TOKEN)
    api = tweepy.API(authentication)


    tweets = api.search('weather', 'ohio', 50)

    for tweet in tweets:
        print("Tweet from "  + tweet.user + " Tweet Message: " + tweet.text)
    
    tweets = api.search('39.758949,-84.191605,25mi', 50)

    for tweet in tweets:
        print("Tweet from "  + tweet.user + " Tweet Message: " + tweet.text)
        
if __name__ == "__main__":
    main()

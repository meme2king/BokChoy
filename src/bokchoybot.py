import constants
import tweepy
import time
from tweepy import Stream
from tweepy.streaming import StreamListener
import schedule

def main():
    authentication = tweepy.OAuthHandler(constants.API_KEY, constants.API_SECRET_KEY)
    authentication.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_SECRET_TOKEN)
    api = tweepy.API(authentication)



        
if __name__ == "__main__":
    main()


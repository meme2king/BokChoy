import constants
import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener

def main():
    authentication = tweepy.OAuthHandler(constants.API_KEY, constants.API_SECRET_KEY)
    authentication.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_SECRET_TOKEN)
    api = tweepy.API(authentication)


    userInput = ''
    while userInput != '!':
        userInput = input("Enter a Twitter display name to crawl for information (Press ! to exit program)\n")
        if userInput == "!":
            break

        friends = api.friends(userInput)

        print(userInput + " friends: ")
        for friend in friends:
            print(friend.screen_name + ", ", end='')
        
        followers = api.followers(userInput)
        
        #follower_amount = 20
        
        #count = 0

        print("\n" + userInput + " followers: ")
        for follower in followers:
            print(follower.screen_name + ", ", end='')

    return
        
if __name__ == "__main__":
    main()

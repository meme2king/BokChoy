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
        userInput = input("Enter a Twitter display name to crawl for follower/friend information (Press ! to exit program)\n")
        user = api.get_user(userInput)
        print("Username: " + user.name) 
        print("Screen name: " + user.screen_name)
        print("Location: " + user.location) 
        print("User description: " + user.description)
        print("The number of followers: " + str(user.followers_count))
        print("The number of friends: " + str(user.friends_count))
        print("The number of tweets (e.i., statuses): " + str(user.statuses_count))
        print("User URL: " + str(user.url))

    return
        
if __name__ == "__main__":
    main()


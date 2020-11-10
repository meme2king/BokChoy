# CPS 470 Assignment 2 Report

## Part 1

1)  A use profile provides a rich source of information to study twitter users. Given a
list of user’s screen names, write a crawler to display this users’ profile information.
You should get the following information for any existing twitter user: [User name, Screen name, User ID, Location, User description, The number of followers, The number of friends, The number of tweets (i.e., statuses), User URL]

This was completed with the following code

```python
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
```
Here it is critical the use of tweepy to get the access and the critical function used to get the user information is api.get_user() which allows us to extract a user object from the Twitter API. From this we can extrapulate more information so as display name, location, bio, etc.

## Part 2

2) There are two types of connection between users: follower and friend. Friendship
is bidirectional while following is one direction. In the following figure, Amy and Peter
are friends (meaning that they follow each other), Bob is following Amy (so Bob is
Amy’s follower), and Amy follows Sophia.Given a list of user’s screen names (any existing names), write a crawler to collect the users’ social network information (i.e., display friends and the first 20 followers). Note that friends are bidirectional (e.g., Amy and Peter are friends as they follow each other)

This is an example of how Twitter network works and we want to try to find the user friends and followers. Below is the implementation for this

```python
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
```
Here the critical functions is api.friends() and api.followers() which both retrieve the friends and followers (up to 20) respectively.

## Part 3

3) Twitter provides APIs to collect tweets that contain the specified keywords or
originate from a given geographic region. The returned objects of the search are in JavaScript Object Notation (JSON). You will exact some fields in JSON. You will look at
both Search API and streaming API.
*  Write a crawler to collect the first 50 tweets that contain these two keywords:
 [Ohio, weather].
*  Write a crawler to collect the first 50 tweets that originate from Dayton region, specified by point_radius: [Longitude of the center, Latitude of the center, radius], where the radius can be up to 25 miles. Any tweet containing a geo point that falls within this region will be matched. Dayton OH geographic information is: Latitude 39.758949, Longitude -84.191605. Note that Google Map takes a slightly different format, i.e., [Latitude, Longitude]. 

Here we want to see the functionality of search in the twitter API fro finding several tweets. Below the code shows how this is done:

```python
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
```

import constants
import tweepy
import json
import time
import random
from tweepy import Stream
from tweepy.streaming import StreamListener
from pathlib import Path
import os.path
from os import path
import schedule

# Twitter Authentication Process
def authenticate():
    authentication = tweepy.OAuthHandler(constants.API_KEY, constants.API_SECRET_KEY)
    authentication.set_access_token(constants.ACCESS_TOKEN, constants.ACCESS_SECRET_TOKEN)
    api = tweepy.API(authentication)
    return api

# tweetMSG generates a random tweet for Bok Choy
def tweetMSG():

    msg = ''

    woof = 'Woof'
    bark = 'Bark'
    bork = 'Bork'

    for i in range(random.randint(1, 32)):
        randomWord = random.randint(0, 2)

        if(randomWord == 0):
            randomCapital = random.randint(0, 1)
            if(randomCapital == 0):
                msg += woof.upper() + " "
            else:
                msg += woof + " "

        if(randomWord == 1):
            randomCapital = random.randint(0, 1)
            if(randomCapital == 0):
                msg += bark.upper() + " "
            else:
                msg += bark + " "
        
        if(randomWord == 2):
            randomCapital = random.randint(0, 1)
            if(randomCapital == 0):
                msg += bork.upper() + " "
            else:
                msg += bork + " "
    msg = msg[:-1] + "!"
    return msg

def imgSelector():
    
    with open('imgCounter.json') as json_file:
        data = json.load(json_file)

    imgCounter = data['imgCounter']
    
    imgPath = Path(constants.IMAGE_PATH + 'bok' + str(imgCounter) + '.jpg')

    print(imgPath)

    if imgPath.exists():
        imgCounter += 1
        data['imgCounter'] = imgCounter
        with open('imgCounter.json', 'w') as json_file:
            json.dump(data, json_file)
        return imgPath
    else:
        print("DOES NOT EXISTS")
        imgCounter = 0
        data['imgCounter'] = imgCounter
        with open('imgCounter.json', 'w') as json_file:
            json.dump(data, json_file)
        imgPath = Path(constants.IMAGE_PATH + 'bok' + str(imgCounter) + '.jpg')

    return imgPath

def job(api):

    msg = tweetMSG()
    api.update_with_media(imgSelector(), msg)
    print("Bok Choy has just Tweeted: " + msg)
    return

def main():

    print("Bok Choy Bot Console:")

    # Authentication Process
    api = authenticate()
    print("Bok Choy has been Authenticated")

    schedule.every().minute.at(":30").do(job, api)

    while True: 
        schedule.run_pending()
        time.sleep(30)

if __name__ == "__main__":
    main()


#!/usr/bin/env python

#Please do not change anything to this section!
import sys
import os
import time
from twython import Tweepy
from datetime import datetime
import pytz

CONSUMER_KEY = 'XQFg5y1p8Oip9FBrhbTurLJgi'
CONSUMER_SECRET = 'AqULlrIHiVRpdrhney3oTCz3nvF2pwet8TtekZaeiHwJMViOWF'
OAUTH_TOKEN = os.environ'2919355408-hWZiwQ19iFXrorqfhtFrI2k211DqPuD33Rytkew'
OAUTH_TOKEN_SECRET = os.environ'eyIZ2yHXlmuJQGAPEYP5c7XZOkQK0kdS6tJ1W3soubf6A'

TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21
#Please so not change anything to this section!

today = datetime.now()
tz = pytz.timezone('Europe/Paris') # change the timezone to your desired/home timezone.
pht = datetime.now(tz) #change the variable too if you want

def OAuth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return auth
    except Exception as e:
        return None
   
oath = OAuth()
api = tweepy.API(oauth)
  
photo = open('./output/shop.png', 'rb')

#Change the text into anything you like! (and please change the variables accordingly if you changed it above.)
api.update_status('Boutique Fortnite du '+pht.strftime("%m/%d/%y")+'!\n'+pht.strftime("%I:%M %p")+', PHT/GMT+8\n\nSi tu veux me soutenir, utilise le code \"Dentoz\" Dans la boutique Forntite !\nReally appreciate it!')

api = twitter_handle()
response = api.upload_media(media=photo)
api.update_status(status=tweetStr, media_ids=[response['media_id']])

print ("Tweeted: " + tweetStr)

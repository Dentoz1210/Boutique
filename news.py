#!/usr/bin/env python

#Please do not change anything to this section!
import sys
import os
import time
from twython import Twython, TwythonError
from datetime import datetime
import pytz

CONSUMER_KEY = os.environ['XQFg5y1p8Oip9FBrhbTurLJgi']
CONSUMER_SECRET = os.environ['AqULlrIHiVRpdrhney3oTCz3nvF2pwet8TtekZaeiHwJMViOWF']
OAUTH_TOKEN = os.environ['2919355408-hWZiwQ19iFXrorqfhtFrI2k211DqPuD33Rytkew']
OAUTH_TOKEN_SECRET = os.environ['eyIZ2yHXlmuJQGAPEYP5c7XZOkQK0kdS6tJ1W3soubf6A']

TWEET_LENGTH = 280
TWEET_URL_LENGTH = 21
#Please do not change anything to this section!

today = datetime.now()
tz = pytz.timezone('Asia/Manila') # change the timezone to your desired/home timezone.
pht = datetime.now(tz) #change the variable too if you want

def twitter_handle():
    return Twython(CONSUMER_KEY, CONSUMER_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

photo = open('./output/news.png', 'rb')

#Change the text into anything you like! (and please change the variables accordingly if you changed it above.)
tweetStr = "Les nouveautés Fortnite du "+pht.strftime("%m/%d/%y")+', '+pht.strftime("%I:%M %p")+" PHT/GMT+8\n\n[Automatically Posted]"

api = twitter_handle()
response = api.upload_media(media=photo)	
api.update_status(status=tweetStr, media_ids=[response['media_id']])	

print("Tweeted: " + tweetStr)

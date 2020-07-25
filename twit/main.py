import tweepy
from auth import auth 

api = tweepy.API(auth)
api.update_status("Hello Tweepy")
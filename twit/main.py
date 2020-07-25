import tweepy
from auth import auth, verify_credentials 



api = tweepy.API(auth)
verify_credentials(api)
# api.update_status("Hello Tweepy")
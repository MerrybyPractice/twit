import json 
import tweepy 

class Stream_Lisitner(tweepy.StreamListener): 
    def init(self, api): 
        self.api = api
        self.me = api.me()
    
    def on_status(self, tweet): 
        print(f"{tweet.user.name}:{tweet.text}")
    
    def on_error(self, status): 
        print("Error!!!", status)
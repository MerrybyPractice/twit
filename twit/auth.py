import tweepy 
#os manipulation for import 
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

with open("resources/twt_secrets.txt", "r") as s:
    secrets = s.readlines()

secrets_dict = {}

for s in range(len(secrets)): 
    secret = secrets[s].split("=")
    secrets_dict[secret[0]] = secret[1]

# print(secrets_dict.keys())

API_KEY = secrets_dict["API_KEY"]
API_SECRET_KEY = secrets_dict["API_SECRET_KEY"]
ACCESS_TOKEN = secrets_dict["ACCESS_TOKEN"]
ACCESS_SECRET = secrets_dict["ACCESS_SECRET"]

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)




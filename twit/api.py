import tweepy
from auth import auth, verify_credentials
from Utilities import Utilities, Search, Status

#create API object and set options
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#unpack search_req.txt
search_req = Utilities()
search_req.read_in_resources("resources/search_req.txt")
search_req_dict = search_req.read_dict

search = Search(search_req_dict)

#set search criteria
result = api.search(q=search.query_string, lang=search.lang, count=search.count)

for tweet in result: 
    search.search_results.append(tweet)

def retweet(): 
    for tweet in range(len(search.search_results)): 
        current_object = Utilities("status")
        current = search.search_results.pop()
        current_object.read_in_resources(current)
        current = current_object.read_dict
        api.retweet(current.get("id"))

def quote_tweet(status_info_file_path): 
    for tweet in range(len(search.search_results)): 
        current_object = Utilities("status")
        current = search.search_results.pop()
        current_object.read_in_resources(current)
        current = current_object.read_dict
        status = Status(status_info_file_path)
        api.update_status(status.status_string, in_reply_to_status_id=current.get("id"))

quote_tweet("resources/status_info.txt")




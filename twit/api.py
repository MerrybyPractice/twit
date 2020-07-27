import tweepy
from auth import auth, verify_credentials
from Utilities import Utilities, Search

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
    print(search.search_results)




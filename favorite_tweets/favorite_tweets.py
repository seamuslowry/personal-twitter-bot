from get_api.get_api import get_api

def favorite_tweets(api):
    mentions = api.mentions_timeline(100)
    print(mentions)

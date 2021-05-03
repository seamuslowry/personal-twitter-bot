from get_api.get_api import get_api
from favorite_tweets.favorite_tweets import favorite_tweets

api = get_api()

def entry_favorite_tweets():
    favorite_tweets(api)


entry_favorite_tweets()
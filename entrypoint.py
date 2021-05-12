import json
from get_api.get_api import get_api
from favorite_tweets.favorite_tweets import favorite_tweets

api = get_api()


def entry_favorite_tweets(event, context):
    favorited_tweets = favorite_tweets(api)
    return {
        "statusCode": 200,
        "body": json.dumps(favorited_tweets)
    }
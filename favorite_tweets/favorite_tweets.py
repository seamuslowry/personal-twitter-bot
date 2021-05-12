import commentjson
import os


def get_approved_users():
    f = open(f'{os.path.dirname(__file__)}/config.jsonc')
    return commentjson.load(f)


def favorite_tweets(api):
    approved_list = get_approved_users()

    all_mentions = api.mentions_timeline(100)
    needs_favorite = [mention for mention in all_mentions
                      if mention.user.id in approved_list
                      and not mention.favorited]

    favorited_tweets = {}
    for mention in needs_favorite:
        api.create_favorite(mention.id)
        favorited_tweets.setdefault(mention.user.name, []).append(mention.text)

    return favorited_tweets

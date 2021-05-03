approved_list = [54438886]


def favorite_tweets(api):
    all_mentions = api.mentions_timeline(100)
    needs_favorite = [mention for mention in all_mentions
        if mention.user.id in approved_list and not mention.favorited]
    for mention in needs_favorite:
        print(mention.text)

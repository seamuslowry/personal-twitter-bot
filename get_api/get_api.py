import dotenv
import os
import tweepy

# for local development, put .env configuration into environment variables
dotenv.load_dotenv()

def get_api():
  """get a tweepy API object for use in other functions"""
  consumer_key = os.getenv("CONSUMER_KEY")
  consumer_secret = os.getenv("CONSUMER_SECRET")
  access_token = os.getenv("ACCESS_TOKEN")
  access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

  auth.set_access_token(access_token, access_token_secret)
  return tweepy.API(auth)
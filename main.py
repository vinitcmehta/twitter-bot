import tweepy
from credentials import *


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

tweet = 'Hello, world!'
api.update_status(status=tweet)


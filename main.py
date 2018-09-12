import tweepy
from credentials import *


#TODO get reddit.py , import that and use top one that is valid for twitter (280 characters)
#TODO Lambda function AWS to run every 24 hours
#TODO tweet the thing

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)

for follower in tweepy.Cursor(api.followers).items():
    follower.follow()
    print ("Followed everyone that is following " + user.name)

#tweet = 'Hello, world!'
#api.update_status(status=tweet)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)


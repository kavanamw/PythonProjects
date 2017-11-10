import tweepy

auth = tweepy.OAuthHandler(2Ms1qRsrxUu2nXliA0TGWRERe, gyeVOAUWwqy0F79HMXwUqOlFGMbwLrJcmGOLkqU9NheQeXfUz7)
auth.set_access_token(2496354104-uPCkkSWZMKGoxSUQHAIQQL60TdJxuRiVCQdkERw, GItWzmaoI9deOVYlIT7iwcjhwVNYlx4zCjptmEQZwYoRN)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text

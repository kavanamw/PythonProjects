#Opens and imports the file with \n newline characters
with open('Topics.txt', 'r') as MyFile:
    data = MyFile.read()
#Splits by the \n newline characters and removes any spaces so that the hashtags can be added
TopicList = data.replace(' ', '').split('\n')

#Adds the '#' for the twitter search
HashList = []
for x in range(len(TopicList)):
    HashList.append('#' + TopicList[x])
print(HashList)

#Twitter OAuth credentials
import tweepy
consumer_key = '2Ms1qRsrxUu2nXliA0TGWRERe'
consumer_secret = 'gyeVOAUWwqy0F79HMXwUqOlFGMbwLrJcmGOLkqU9NheQeXfUz7'
access_token = '2496354104-uPCkkSWZMKGoxSUQHAIQQL60TdJxuRiVCQdkERw'
access_token_secret = 'GItWzmaoI9deOVYlIT7iwcjhwVNYlx4zCjptmEQZwYoRN'

# Access and authorize our Twitter credentials from credentials.py
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

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

#Searching Twitter
import tweepy

#Oauth 
access_token = "2496354104-uPCkkSWZMKGoxSUQHAIQQL60TdJxuRiVCQdkERw"
access_secret = "GItWzmaoI9deOVYlIT7iwcjhwVNYlx4zCjptmEQZwYoRN"
consumer_key = "2Ms1qRsrxUu2nXliA0TGWRERe"
consumer_secret = "gyeVOAUWwqy0F79HMXwUqOlFGMbwLrJcmGOLkqU9NheQeXfUz7"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

query = 'python'
max_tweets = 1
searched_tweets = [status for status in tweepy.Cursor(api.search, q=query).items(max_tweets)]
print(searched_tweets)
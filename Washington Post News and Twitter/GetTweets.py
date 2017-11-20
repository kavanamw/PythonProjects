import tweepy
import time
#Token and key setup, moving to a file would be more secure
access_token = "2496354104-uPCkkSWZMKGoxSUQHAIQQL60TdJxuRiVCQdkERw"
access_secret = "GItWzmaoI9deOVYlIT7iwcjhwVNYlx4zCjptmEQZwYoRN"
consumer_key = "2Ms1qRsrxUu2nXliA0TGWRERe"
consumer_secret = "gyeVOAUWwqy0F79HMXwUqOlFGMbwLrJcmGOLkqU9NheQeXfUz7"\

#Oauth and api
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

#Opens and imports the file with \n newline characters
with open('Topics.txt', 'r') as MyFile:
    data = MyFile.read()

#Splits by the \n newline characters and removes any spaces so that the hashtags can be added
TopicList = data.replace(' ', '').split('\n')

#File for the tweets to be saved into
File = open('Tweets.txt', 'w', encoding='utf-8')

#Adds the '#' for the twitter search
HashList = []
for x in range(len(TopicList)):
    HashList.append('#' + TopicList[x])
print(HashList)

#Write the HashTopics to file
Htopics = open('HashTopics.txt', 'w')
for x in range(len(HashList)):
    Htopics.write(HashList[x])
    Htopics.write('\n')
#Searching Twitter
REQUEST_DELAY = 5
for x in range(len(HashList)):
    searched_tweets = api.search(q=HashList[x])
    time.sleep(REQUEST_DELAY)
    File.write(HashList[x])
    File.write('\n')
    for searched_tweets in searched_tweets:
        print(searched_tweets.text)
        print(' ')
        File.write(searched_tweets.text)
        File.write('\n')
    File.write('\n')

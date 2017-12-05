import tweepy
import time
import os
import re
from textblob import TextBlob
#Token and key setup, moving to a file would be more secure
access_token = "2496354104-uPCkkSWZMKGoxSUQHAIQQL60TdJxuRiVCQdkERw"
access_secret = "GItWzmaoI9deOVYlIT7iwcjhwVNYlx4zCjptmEQZwYoRN"
consumer_key = "2Ms1qRsrxUu2nXliA0TGWRERe"
consumer_secret = "gyeVOAUWwqy0F79HMXwUqOlFGMbwLrJcmGOLkqU9NheQeXfUz7"

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
for x in range(len(TopicList) - 1):
    HashList.append('#' + TopicList[x])
print(HashList)

#Write the HashTopics to file
Htopics = open('HashTopics.txt', 'w')
for x in range(len(HashList)):
    Htopics.write(HashList[x])
    Htopics.write('\n')

def CreateFile():
    filename = "C:\\Users\\vuata\\Google Drive\\Git\\PythonProjects\\Washington Post News and Twitter\\Topics"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

#Searching Twitter
REQUEST_DELAY = 2
for x in range(len(HashList)):
    searched_tweets = api.search(q=HashList[x], count=1000)
    time.sleep(REQUEST_DELAY)
    File.write(HashList[x])
    File.write('\n')
    for searched_tweets in searched_tweets:
        #Prints the tweets for testing, remove for final version
        print(searched_tweets.text)
        print(' ')
        #Cleans tweets
        #analysis = TextBlob(self.clean_tweet(searched_tweets))
        #searched_tweets = analysis
        #searched_tweets = clean_tweet(searched_tweets)
        #Saves tweets into a file for each individual topic
        CreateFile()
        Tweets = open("C:\\Users\\vuata\\Google Drive\\Git\\PythonProjects\\Washington Post News and Twitter\\Topics\\%s.txt" % (TopicList[x]), 'a+', encoding='utf-8')
        Tweets.write('\n')
        Tweets.write(searched_tweets.text)
        Tweets.write('\n')
        #Saves all tweets in file
        File.write(searched_tweets.text)
        File.write('\n')
    File.write('\n')
Tweets.close()
File.close()

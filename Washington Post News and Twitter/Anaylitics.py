from textblob import TextBlob
import re
import os
#import preprocessor as p
Counter = 0

def GetFile():
    #Gets the file and returns the topics in a list
    Topics = os.listdir("C:\\Users\\vuata\Google Drive\\Git\\PythonProjects\\Washington Post News and Twitter\\Topics")
    Topicslst = [s.strip('.txt') for s in Topics]
    return Topicslst

def GetTopics():
    #Gets the topics of the tweets for each file and returns the tweets themselves
    global Counter
    TopicsList = GetFile()
    Counter = Counter + 1
    with open("C:\\Users\\vuata\\Google Drive\\Git\\PythonProjects\\Washington Post News and Twitter\\Topics\\%s.txt" % TopicsList[Counter], encoding='utf-8') as File:
        Tweets = File.read().splitlines()
        #Cleans a lot of the mess out of the tweets making it into only text and removeing special characters
        #CleanTweets = re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", str(Tweets))
    return Tweets

def Postive_Negative_Sent():
    #Returns the general sentiment of a tweet for each topic and outputs them as a percent postive, negative
    TweetText = GetTopics()
    Topics = GetFile()
    Postive = 0
    Negative = 0
    Undef = 0
    for x in range(1, len(TweetText)):
        BlobString = TextBlob(TweetText[x])
        Polarity = BlobString.sentiment.polarity
        if Polarity > 0:
            Postive += 1
        elif Polarity < 0:
            Negative += 1
        else:
            Undef += 1
    print('\n')
    print(Topics[Counter])
    PercentPostive = (Postive/len(TweetText)) * 100
    PercentNegative = (Negative/len(TweetText)) * 100
    PercentUndefined = (Undef/len(TweetText)) * 100
    print(str(round(PercentPostive)) + '% Postive')
    print(str(round(PercentNegative)) +'% Negative')
    print(str(round(PercentUndefined)) +'% Unable to determine the sentiment')
    return [PercentPostive, PercentNegative, PercentUndefined]

def AverageSent():
    #Returns the average of the postive vs. negative span and returns a string saying which was more prevalent
    Polarity = 0
    TweetText = GetTopics()
    for x in range(1, len(TweetText)):
        BlobString = TextBlob(TweetText[x])
        Polarity = BlobString.sentiment.polarity
        #Polarity += Polarity
        Average = Polarity/len(TweetText)
        Good = "Postive"
        Bad = "Negative"
        if Average > 0:
            print('On average most people feel Postively on this topic')
        elif Average < 0:
            print('On average most people feel Negatively on this topic')
        else:
            print("Error on Average sentiment")
        return Average

def main():
    Topics = GetFile()
    for x in range(1, len(Topics)):
        Postive_Negative_Sent()
        Average = AverageSent()


if __name__ == "__main__":
    # calling main function
    main()

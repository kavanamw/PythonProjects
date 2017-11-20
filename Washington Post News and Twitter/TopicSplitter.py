#Opens and imports the file with \n newline characters
with open('Tweets.txt', 'r', encoding='utf-8') as MyFile:
    data = MyFile.read()

from GetTweets.py import GetHashList
print(GetHashList())

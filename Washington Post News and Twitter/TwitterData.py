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
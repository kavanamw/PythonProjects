import requests
import csv
from bs4 import BeautifulSoup

#Get the page and make a beautiful soup object
page = requests.get('https://www.washingtonpost.com/')
soup = BeautifulSoup(page.text, 'html.parser')

#Find the in-the-news-wrapper and find all the 'a' tags
IntheNewClass = soup.find(class_= 'in-the-news-wrapper')
IntheNewClass = IntheNewClass.find_all('a')

#Creating file too read into
Topics = open('Topics.txt', 'w')

#Writes the topics into a file each on a new line
List = []
for NewsName in IntheNewClass:
    names = NewsName.contents[0]
    List.append(names)
for names in List:
    Topics.write("%s\n" % names)
Topics.close()
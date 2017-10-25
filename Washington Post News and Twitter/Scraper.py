import requests
from bs4 import BeautifulSoup

#Get the page and make a beautiful soup object
page = requests.get('https://www.washingtonpost.com/')
soup = BeautifulSoup(page.text, 'html.parser')

#Find the in-the-news-wrapper and find all the 'a' tags
IntheNewClass = soup.find(class_= 'in-the-news-wrapper')
IntheNewClass = IntheNewClass.find_all('a')

#Prints just the news keywords
for NewsName in IntheNewClass:
    names = NewsName.contents[0]
    print(names)
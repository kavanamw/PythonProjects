import requests
from bs4 import BeautifulSoup

#Get the page and make a beautiful soup object
page = requests.get('https://www.bing.com/')
soup = BeautifulSoup(page.text, 'html.parser')

#Find the wallpaper class
#IntheNewClass = soup.find(class_= 'hp_hd')
#IntheNewClass = IntheNewClass.find_all('div')

string = str(soup)
#print(str(IntheNewClass))
text = open('data.txt', 'w')
text.write(string)
#for data scraping we have to use [beautifulSoup4,request] package

import requests
import pprint
from bs4 import BeautifulSoup

res = requests.get('https://news.ycombinator.com/news')
res2= requests.get('https://news.ycombinator.com/news?p=2')
res3= requests.get('https://news.ycombinator.com/news?p=3')
soup = BeautifulSoup(res.text,'html.parser') #html convert
soup2 = BeautifulSoup(res2.text,'html.parser')
soup3 = BeautifulSoup(res3.text,'html.parser')
# print(soup.body) #to check the body of the website
# print(soup.find('a'))
# print(soup.find_all('a'))
links = soup.select('.titleline')#selecting the links
subtext = soup.select('.subtext')#and subtext
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')
links3 = soup3.select('.titleline')
subtext3 = soup3.select('.subtext')

megaLink = links+links2+links3 #merging 1 and 2
megaSub = subtext+subtext2+subtext3

def sortStories(hn):
    return sorted(hn,key = lambda k:k['votes'],reverse = True) #sotring the votes in desending order

def createCustomNews(megaLink,megaSub):
    hn =[]
    for idx,item in enumerate(links):
        title = item.getText()#get title
        href = item.get('href',None)#get links
        vote = megaSub[idx].select('.score')#in subtext select score
        if len(vote):#if the post has any votes
            points = int(vote[0].getText().replace(' points',''))
            if points > 99:
                hn.append({'title' : title, 'link' : href,'votes':points})
    return sortStories(hn)
pprint.pprint(createCustomNews(megaLink,megaSub))

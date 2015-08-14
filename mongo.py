__author__ = 'kslab'

#coding:utf-8
import requests
import json
import time
import pymongo
#from pymongo import MongoClient
from bs4 import BeautifulSoup

data = []
for i in range(1,50):
    url = "http://www.appledaily.com.tw/realtimenews/section/new/" + str(i)
    if i % 5 == 0:
        time.sleep(3)
    response = requests.get(url)
    #print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.findAll('li', {'class' : 'rtddt'}):
        #f.write('{\"time\" : \"' + item.a.time.text + '\",\t')
        #f.write('\"h2\" : \"' + item.a.h2.text + '\",\t')
        #f.write('\"h1\" : \"' + item.a.h1.text + '\"}\n')
        d = {"時間" : item.a.time.text, "類別" : item.a.h2.text, "標題" : item.a.h1.text}
        data.append(d)
        print(item.a.h1.text)

#file = json.dumps(data, ensure_ascii=False)

uri = "mongodb://ting:123456@ds029803.mongolab.com:29803/apple_news"
client = pymongo.MongoClient(uri)

db = client['apple_news']
#collection = db['news_collection']

db.news_collection.insert(data)

# -*- coding: utf-8 -*-
import urllib.request as req
import bs4
from re import match
import time


def getData(url):
    request=req.Request(
        url,
        headers={
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
            }
    )
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")
    root=bs4.BeautifulSoup(data,"html.parser")
    nextLink=root.find("a",string="‹ 上頁")
    return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/movie/index.html"
count=0
positiveCommon=[]
generalCommon=[]
negativeCommon=[]
timeBefore = time.time()
print("Searching......\nPlease wait a minute.")
while count < 10:   
    request=req.Request(
        pageURL,
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        }
    )
    with req.urlopen(request) as response:
        data=response.read().decode("utf-8")

    root=bs4.BeautifulSoup(data,"html.parser")
    titles=root.find_all("div",class_="title") 
    for title in titles:
        if title.a:        
            titleStrings=title.a.string
            #Filter
            '''
            #Method 1:
            if match(r"\[好雷\].*|\[普雷\].*|\[負雷\].*",titleStrings):
                if "好雷" in titleStrings:
                    positiveCommon.append(titleStrings)
                elif "負雷" in titleStrings:
                    negativeCommon.append(titleStrings)
                elif "普雷" in titleStrings:
                    generalCommon.append(titleStrings)
            '''
            #'''
            #Method 2:
            
            if match(r"\[好雷\].*",titleStrings):   
                positiveCommon.append(titleStrings)
            elif match(r"\[負雷\].*",titleStrings):
                negativeCommon.append(titleStrings)
            elif match(r"\[普雷\].*",titleStrings):
                generalCommon.append(titleStrings)  
            #'''      
            '''
            #Method 3:
            if titleStrings.startswith("[好雷]"):
                goodCommon.append(titleStrings)
            elif titleStrings.startswith("[負雷]"):
                badCommon.append(titleStrings)
            elif titleStrings.startswith("[普雷]"):
                generalCommon.append(titleStrings)
            '''
    count+=1
    pageURL="https://www.ptt.cc"+getData(pageURL)
print("Consume time: "+str(time.time()-timeBefore)+"\n")
print("Output to movie.txt.\nPlease wait a minute.")
with open('movie.txt', 'w',encoding="utf-8") as f:
    for title in positiveCommon:
        f.write(title+"\n")
    for title in generalCommon:
        f.write(title+"\n")
    for title in negativeCommon:
        f.write(title+"\n")
print("Done. Got titles about [好雷], [普雷], [負雷] to movie.txt successfully.")
print("Consume time: "+str(time.time()-timeBefore))



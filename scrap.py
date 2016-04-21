#!/usr/bin/python

import requests
from bs4 import BeautifulSoup




def google(query):
    url = "https://www.google.co.in/search?q=" + query
    r = requests.get(url, headers={"Accept" : "*/*", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36"})
    if r.status_code == 200:
        print r.request.headers
        return BeautifulSoup(r.text)

def parseSoup(s):
    for tag in s.find_all('a'):
        print tag


soup = google("chete karda mp3")
parseSoup(soup)
#print soup.prettify()

#!/usr/bin/python

import requests
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz


def google(query, cleaned=0):
    url = "https://www.google.co.in/search?q=" + query
    r = requests.get(url, headers={"Accept" : "*/*", "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36 googlescrap/0.1.0"})
    if r.status_code == 200:
        res = parseSoup(BeautifulSoup(r.text), query)
        if cleaned == 1:
            cleanedResults = []
            for x in res:
                if x["fuzz"] > 50 and x["text"] != "Cached":
                    cleanedResults.append(x)
            return cleanedResults
    return res

def parseSoup(s, query):
    result = []
    for tag in s.find_all('a'):
        try:
            st = str(tag.string)
            href = str(tag['href'])
            ratio = fuzz.partial_ratio(st.upper(), query.upper())
            result.append({"fuzz": ratio, "host": href[7 : int(href.find('/', 8))],  "href": href, "text": st})
        except KeyError, AttributeError:
            continue
    return result

if __name__ == "__main__":
    r = google("chete karda mp3", 1)
    for x in r:
        print x["fuzz"], x["text"], x["href"] 
#print soup.prettify()

'''chapter11_01.crawling.py v1.0'''

import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

news_url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query='
search = input("기사 검색어 : ")
url = news_url + urllib.parse.quote_plus(search)
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')
title = soup.find_all(class_='news_tit')
#print(title)
for i in title:
    print(i.attrs['title'])
    print(i.attrs['href'])
    print()

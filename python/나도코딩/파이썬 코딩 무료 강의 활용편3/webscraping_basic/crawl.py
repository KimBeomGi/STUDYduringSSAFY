# 기술노트with 알렉
# 파이썬 웹 크롤링 하기 - 너무 간단해서 민망합니다. 영상ㅇ미

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://news.naver.com/")

bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.find_all('a'):
    print(link.text.strip(), link.get('href'))
for link in bsObject.find_all('img'):
    print(link.text.strip(), link.get('src'))
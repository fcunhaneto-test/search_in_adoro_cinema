import os
import re
from urllib.request import urlopen
from unicodedata import normalize
from bs4 import BeautifulSoup

url1 = 'https://www.minhaserie.com.br/serie/236-the-x-files/episodios/s1e24'

num = url1[-2:]
if 'e' in num:
    num = url1[-1:]
    url2 = url1[:-1]
else:
    url2 = url1[:-2]

num = int(num)



for n in range(1, num+1):
    url = url2 + str(n)

    http = urlopen(url)
    #
    soup = BeautifulSoup(http, 'lxml')
    # html = soup.prettify("utf-8")

    # with open("ep1.html", "wb") as file:
    #     file.write(html)

    div = soup.find('div', {'id': 'episode_body'})
    name = div.h2.text
    summary = div.p.text

    print(name)
    #
    # num = url1[-2:]
    # if 'e' in url1:
    #     num = url1[-1:]
    # season = int(num)



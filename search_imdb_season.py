import os
import re
from urllib.request import urlopen
from unicodedata import normalize
from bs4 import BeautifulSoup

url1 = 'https://www.imdb.com/title/tt0106179/episodes?season=4&ref_=tt_eps_sn_4'
itemprop="name"

http = urlopen(url1)

soup = BeautifulSoup(http, 'lxml')
html = soup.prettify("utf-8")

names = soup.findAll(itemprop='episodes')
summaries = soup.findAll(itemprop='description')
total = len(names)
episodes = []
for i in range(total):
    episode = []
    episode.append(names[i].strong.text)
    episode.append(summaries[i].text.strip())

    episodes.append(episode)

print(episodes)
import os
import re

from urllib.request import urlopen
from unicodedata import normalize

from bs4 import BeautifulSoup

url = 'https://www.imdb.com/title/tt0117060/?ref_=nv_sr_4'
http = urlopen(url)
soup = BeautifulSoup(http, 'lxml')

get_time = soup.find('div', {'class': 'subtext'}).time.text
s = get_time.strip()
print(s)

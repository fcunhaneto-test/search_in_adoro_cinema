import os
from urllib.request import urlopen
from unicodedata import normalize
from bs4 import BeautifulSoup

url1 = 'http://www.adorocinema.com/series/serie-18159/'
# url1 = 'http://www.adorocinema.com/series/serie-440/'
# url1 = 'http://www.adorocinema.com/series/serie-65/'
# url1 = 'http://www.adorocinema.com/series/serie-182/'
# url1 = 'http://www.adorocinema.com/series/serie-9430/'

http = urlopen(url1)

soup = BeautifulSoup(http, 'lxml')
html = soup.prettify("utf-8")

# with open("se1.html", "wb") as file:
#     file.write(html)

title = None
# Title
if soup.find('div', {'class': 'titlebar-title'}):
    title = soup.find('div', {'class': 'titlebar-title'}).span.text
    print(title)

# Year Categories
if soup.find('div', {'class': 'meta-body-info'}):
    cats = soup.find('div', {'class': 'meta-body-info'})
    year = cats.text.split()
    if year[0] == 'Desde':
        print('year:', year[1])
    else:
        print('year:', year[0])

    categories = []
    for d in cats.children:
        if d.name == 'span' and d.text != '/':
            categories.append(d.text)

    print('categories:', categories)

# Creator
if soup.find('div', {'class': 'meta-body-direction'}):
    creator = soup.find('div', {'class': 'meta-body-direction'}).a.text
    print('creator:', creator)

if soup.find('div', {'class': 'content-txt'}):
    summary = soup.find('div', {'class': 'content-txt'}).text

print(summary.strip())

# Cast
with open("se2.html", "wb") as file:
    file.write(html)

if soup.findAll('div', {'class': 'person-card'}):
    names = soup.findAll('div', {'class': 'person-card'})

casts = []
for n in names:
    cast = []
    cast.append(n.a.text.strip())
    if n.findChildren('div', {'class': 'meta-sub'}):
        cast.append(n.findChildren('div', {'class': 'meta-sub'})[0].
                    text.strip().replace('Personagem : ', ''))
    else:
        cast.append('')

    casts.append(cast)

print(casts)

# Poster
if soup.find('div', {'class': 'entity-card'}):
    thumbnail = soup.find('div', {'class': 'entity-card'}).find('img')
    t_url = thumbnail['src']
    name = title.lower()
    char = [' ', '.', '/', '\\']
    for c in char:
        file = name.replace(c, '_')
    title = normalize('NFKD', title).encode('ASCII', 'ignore').decode('ASCII')
    path = os.getcwd()
    poster = path + '/poster/' + title + '.jpg'
    with open(poster, 'wb') as f:
        f.write(urlopen(t_url).read())
import re
from urllib.request import urlopen
from bs4 import BeautifulSoup

# url1 = 'http://www.adorocinema.com/series/serie-18159/'
# url1 = 'http://www.adorocinema.com/series/serie-440/'
# url1 = 'http://www.adorocinema.com/series/serie-65/'
# url1 = 'http://www.adorocinema.com/series/serie-182/'
url1 = 'http://www.adorocinema.com/series/serie-9430/'

http = urlopen(url1)

soup = BeautifulSoup(http, 'lxml')
html = soup.prettify("utf-8")

# with open("se1.html", "wb") as file:
#     file.write(html)

if soup.find('div', {'class': 'titlebar-title'}):
    name = soup.find('div', {'class': 'titlebar-title'}).span.text
    print(name)

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

if soup.find('div', {'class': 'meta-body-direction'}):
    creator = soup.find('div', {'class': 'meta-body-direction'}).a.text
    print('creator:', creator)

if soup.find('div', {'class': 'content-txt'}):
    summary = soup.find('div', {'class': 'content-txt'}).text

print(summary.strip())

# Character

with open("se2.html", "wb") as file:
    file.write(html)

if soup.findAll('div', {'class': 'person-card'}):
    names = soup.findAll('div', {'class': 'person-card'})

actors = []
characters = []
for n in names:
    actors.append(n.a.text.strip())
    if n.findChildren('div', {'class': 'meta-sub'}):
        characters.append(n.findChildren('div', {'class': 'meta-sub'})[0].text.strip().replace('Personagem : ', ''))
print(actors)
print(characters)
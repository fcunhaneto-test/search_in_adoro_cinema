import os
import re
from urllib.request import urlopen
from unicodedata import normalize
from bs4 import BeautifulSoup



# url1 = 'http://www.adorocinema.com/filmes/filme-114820/'
# url1 = 'http://www.adorocinema.com/filmes/filme-209778/'
# url1 = 'http://www.adorocinema.com/filmes/filme-33427/'
# url1 = 'http://www.adorocinema.com/filmes/filme-44436/'
# url1 = 'http://www.adorocinema.com/filmes/filme-448/'
# url1 = 'http://www.adorocinema.com/filmes/filme-189446/'
url1 = 'http://www.adorocinema.com/filmes/filme-232669/'
# url1 = 'http://www.adorocinema.com/filmes/filme-1420/'

http = urlopen(url1)

soup1 = BeautifulSoup(http, 'lxml')
html1 = soup1.prettify("utf-8")

# with open("mv2.html", "wb") as file:
#     file.write(html1)

# Porque o site adoro cinema é mal formato temos que testar todas as condições
# para saber se o item existe ou não
if soup1.find('div', {'class': 'titlebar-title'}):
    title = soup1.find('div', {'class': 'titlebar-title'}).text
    print(title)

if soup1.find(itemprop="director"):
    director = soup1.find(itemprop="director").get_text()
    print('director:', director.strip())

if soup1.find_all(itemprop="genre"):
    cats = soup1.find_all(itemprop="genre")
    categories = []
    for c in cats:
        categories.append(c.text)
    print('categories', categories)

if soup1.find(itemprop="description"):
    summary = soup1.find(itemprop="description")
    print('summary:', summary.text.strip())

if soup1.find('span', text=re.compile(r"^Data de lançamento$")):
    try:
        year = soup1.find('span', text=re.compile(r"^Data de lançamento$")).find_next_sibling('span').text[-4:]
    except AttributeError:
        year = soup1.find('span', text=re.compile(r"^Data de lançamento$")).parent.text
        year = year.split()[3]
    print(year)


if soup1.find('div', {'class': 'movie-card-overview'}):
    thumbnail = soup1.find('div', {'class': 'movie-card-overview'}).find('img')
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

# Character
url2 = url1 + 'creditos/'
http = urlopen(url2)

soup2 = BeautifulSoup(http, 'lxml')
html2 = soup2.prettify("utf-8")

# with open("ch2.html", "wb") as file:
#     file.write(html2)

if soup2.findAll('div', {'itemprop': "actor"}):
    d = soup2.findAll('div', {'itemprop': "actor"})

    actors_characters = []
    for f in d:
        actor_character = []
        a = f.text.strip()
        actor_character.append(a)

        d = f.find_next_siblings('div')
        c = d[0].text.strip().replace('Personagem : ', '')
        actor_character.append(c)

        actors_characters.append(actor_character)

    print('actor/character:', actors_characters)



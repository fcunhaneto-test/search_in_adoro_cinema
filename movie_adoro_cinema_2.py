import os
import re
from urllib.request import urlopen
from unicodedata import normalize
from bs4 import BeautifulSoup


url1 = 'http://www.adorocinema.com/filmes/filme-146349/'
# url1 = 'http://www.adorocinema.com/filmes/filme-114820/'
# url1 = 'http://www.adorocinema.com/filmes/filme-209778/'
# url1 = 'http://www.adorocinema.com/filmes/filme-33427/'
# url1 = 'http://www.adorocinema.com/filmes/filme-44436/'
# url1 = 'http://www.adorocinema.com/filmes/filme-448/'
# url1 = 'http://www.adorocinema.com/filmes/filme-189446/'
# url1 = 'http://www.adorocinema.com/filmes/filme-232669/'
# url1 = 'http://www.adorocinema.com/filmes/filme-1420/'
# url1 = 'http://www.adorocinema.com/filmes/filme-53751/'
# url1 = 'http://www.adorocinema.com/filmes/filme-209778/'
http = urlopen(url1)

soup1 = BeautifulSoup(http, 'lxml')
html1 = soup1.prettify("utf-8")

with open("mv3.html", "wb") as file:
    file.write(html1)

# Porque o site adoro cinema é mal formato temos que testar todas as condições
# para saber se o item existe ou não

# Title
if soup1.find('div', {'class': 'titlebar-title'}):
    title = soup1.find('div', {'class': 'titlebar-title'}).text
    print(title)

# Original Title
if soup1.find('h2', {'class', 'that'}):
    original_title = soup1.find('h2', {'class', 'that'}).text
    print(original_title)

# Director
if soup1.find('span', text=re.compile(r"^Direção:$")):
    director = soup1.find('span', text=re.compile(r"^Direção:$")).\
        find_next_sibling('a').text
    print('director:', director)

    div = soup1.find('span', text=re.compile(r"^Data de lançamento$")).parent.get_text()
    s = div.replace('\n', '')
    s = s.partition('(')
    s = s[-1].replace(')', '')
    print('s', s)

# Time


# Categories
if soup1.find('span', text=re.compile(r"^Gêneros$")):
    category1 = soup1.find('span', text=re.compile(r"^Gêneros$")).find_next_sibling()
    category2 = soup1.find('span',
                          text=re.compile(r"^Gêneros$")).find_next_sibling().find_next_sibling()
    print(category1.text, category2.text)

# Summary
if soup1.findAll('section', {'id': 'synopsis-details'}):
    summary = soup1.find('section', {'id': 'synopsis-details'}).find('div', {'class': 'content-txt'}).p.text
    print(summary)

if soup1.find('span', text=re.compile(r"^Data de lançamento$")):
    try:
        year = soup1.find('span', text=re.compile(r"^Data de lançamento$")).find_next_sibling('span').text[-4:]
    except AttributeError:
        year = soup1.find('span', text=re.compile(r"^Data de lançamento$")).parent.text
        year = year.split()[3]
    print(year)

# Poster
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

# Cast
url2 = url1 + 'creditos/'
http = urlopen(url2)

soup2 = BeautifulSoup(http, 'lxml')
html2 = soup2.prettify("utf-8")

# with open("ch2.html", "wb") as file:
#     file.write(html2)

if soup2.findAll('section', {'id': 'actors'}):
    section = soup2.find('section', {'id': 'actors'}).find_all('a')
    actors_characters = []
    for a in section:
        ac = []
        parent = a.find_parent('div').findNext('div')
        char = parent.text.strip()
        s = char.split(' : ')
        if s[0] != 'Personagem':
            break
        ac.append(a.text.strip())
        ac.append(s[1].strip())
        actors_characters.append(ac)

    print(actors_characters)


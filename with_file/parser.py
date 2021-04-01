from bs4 import BeautifulSoup
from sys import *

if __name__ == '__main__':
    if len(argv) == 2:
        file = argv[1]
    elif len(argv) == 1:
        print('Ошибка. Параметры не заданы!')
        exit()
    elif len(argv) > 2:
        print('Ошибка. Задано очень много параметров!')
        exit()

html = open(file)

content = html.read()

soup = BeautifulSoup(content, 'html.parser')

title = soup.find_all('h1', class_='title')
pharagraph = soup.find_all('p', class_='pharagraph')
link = soup.find_all('a', class_='link')
li = soup.find_all('li', class_='item')

for t in title:
    print('title:', t.get_text())

for p in pharagraph:
    print('p:', p.get_text())

for l in link:
    print('a:', l.get_text())

for l in li:
    print('li:', l.get_text())

html.close()
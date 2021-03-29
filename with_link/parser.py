from bs4 import BeautifulSoup
import urllib.request as url

req = url.urlopen('https://yandex.ru/')

html = req.read()

soup = BeautifulSoup(html, 'html.parser')

content = soup('a')

for i in content:
    print('link:', i.get('href'))
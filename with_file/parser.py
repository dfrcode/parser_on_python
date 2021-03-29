from bs4 import BeautifulSoup

html = open('./parser/with_file/index.html')

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
from bs4 import BeautifulSoup

html = open('./parser/with_file/index.html')

content = html.read()

soup = BeautifulSoup(content, 'html.parser')

li = soup.find_all('li', class_='item')

for l in li:
    print('li:', l.get_text())

html.close()
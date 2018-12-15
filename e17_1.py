# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup

url = 'https://www.idnes.cz/'
r = requests.get(url)
r_html = r.text


soup = BeautifulSoup(r_html, 'html.parser')

headers = soup.find_all('h3')
for header in headers:
    text = header.get_text()
    print(text)


# title = soup.find('span', 'articletitle').string
# https://www.practicepython.org/exercise/2014/07/14/19-decode-a-web-page-two.html

import requests
from bs4 import BeautifulSoup

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

texts = soup.find_all('p')
for part in texts:
    article = part.get_text()
    print(article)


# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup


url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

# print(r_html)

soup = BeautifulSoup(r_html, 'html.parser')

headers = soup.find_all('h2')
for header in headers:
    text = header.get_text()
    print(text)


# title = soup.find('span', 'articletitle').string
# https://www.practicepython.org/exercise/2014/11/30/21-write-to-a-file.html

#to do: get rid of symbols

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')

file_name = input("Enter a file name to put the text in: ")


with open(file_name, 'w') as open_file:
    for header in soup.find_all('h2'):
        text = header.get_text()
        open_file.write(text + '\n')

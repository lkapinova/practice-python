# exercise from Tom - extract headlines and paragraphs from webpage: https://tkteststatichtml5.azurewebsites.net/

import requests
from bs4 import BeautifulSoup

url = 'https://tkteststatichtml5.azurewebsites.net/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
row = soup.find("div", attrs={'class':'row'})

for div in row.find_all("div"):
    print(div.h2.text)
    for p in div.find_all("p"):
        print(p.text)
    print("\n")



    






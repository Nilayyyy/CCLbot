import requests
from bs4 import BeautifulSoup


r=requests.get('https://www.centralcoalfields.in/cmpny/cprfl.php', verify=False)

soup=BeautifulSoup(r.content, 'html.parser')

s=soup.find('div', class_='intro')

lines=s.find_all('tr')

paragraphc=""
for line in lines:
    l=line.text
    #print(l)
    lc=l.split()
    #print(ln)
    paragraphc+=' '.join([x.strip() for x in lc])
    
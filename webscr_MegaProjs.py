import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.centralcoalfields.in/cmpny/mgaprjts.php', verify=False)

soup=BeautifulSoup(r.content,'html.parser')

s=soup.find('div', class_='page-content')

lines=s.find_all('table')

paragraphmp=""
for line in lines:
    l=line.text
    #print(l)
    lm=l.split()
    #print(ln)
    paragraphmp+=' '.join([x.strip() for x in lm])
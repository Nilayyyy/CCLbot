import requests
from bs4 import BeautifulSoup



r = requests.get('https://www.centralcoalfields.in/cmpny/hstry.php',verify=False)

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find('div', class_='dez-post-title')

lines = s.find_all('p')


paragraphh=""
for line in lines:
    l=line.text
    #print(l)
    lh=l.split()
    #print(ln)
    paragraphh+=' '.join([x.strip() for x in lh])
    

import requests
from bs4 import BeautifulSoup

r=requests.get('https://www.centralcoalfields.in/cmpny/vsms.php',verify=False)

soup=BeautifulSoup(r.content,'html.parser')

s=soup.find('div', class_='dez-post-title')

lines=s.find_all('p')

for line in lines:
    l=line.text
    #print(l)
    #ln=l.split()
    #print(ln)
    
#for n in range(2):
    #if "vision" in ln[n]:
        #for i in range (10):
            #print(ln[n+i])
if l.find("satisfaction")==1:
    print(l)
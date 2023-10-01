import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
import requests
from bs4 import BeautifulSoup
from webscr_history import paragraphh
from webscr_compProfile import paragraphc
from webscr_MegaProjs import paragraphmp

r=requests.get('https://www.centralcoalfields.in/cmpny/vsms.php',verify=False)
soup=BeautifulSoup(r.content,'html.parser')
s=soup.find('div', class_='dez-post-title')
lines=s.find_all('p')



nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    tokens = word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

#vision and mission tab
paragraph=""
for line in lines:
    l=line.text
    #print(l)
    ln=l.split()
    #print(ln)
    paragraph+=' '.join([x.strip() for x in ln])
para = " ".join([paragraph, paragraphh, paragraphc, paragraphmp])
paran = word_tokenize(para.lower())
paran = [lemmatizer.lemmatize(token) for token in paran if token.isalnum()]
#print(paran)

    
def get_response(user_input):
    user_tokens = preprocess_text(user_input)
    res = [ele for ele in paran if(ele in user_tokens)]
    #print(res)
    print("search word in paran : " + str(bool(res)))
    
    l1=[]
    str1=" "
    if res:
        n=int(input("Enter number of words : "))
        for i in range(len(user_tokens)):
            for j in range (len(paran)):
                if user_tokens[i] == paran[j]:
                    
                    for k in range(n):
                        l1.append(paran[j+k-(n//2)])
                    return (str1.join(l1))
                            

while True:
    user_input = input(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n==> User: ")
    response = get_response(user_input)
    print("==> Bot:", response)
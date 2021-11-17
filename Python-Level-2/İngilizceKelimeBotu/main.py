#pip install requests bs4
import re
import requests
from bs4 import BeautifulSoup

URL='https://www.cumlesozluk.com/1000-kelime.html'
wordsList=[]
meanList=[]
def youtubeİsim(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'html.parser')
    words=soup.find_all('b')
    meanings=soup.find_all("li")
    mean(meanings)
    word(words)

def mean(meanings):
    liste = []
    for i in range(23, len(meanings) - 2):
        mean = meanings[i].text
        mean=mean.replace('\n','')
        mean=mean.replace('\r','')
        mean=mean.split(":")
        liste.append(mean[1])
    print(liste)



def word(words):
    for i in range(1,len(words)-2):
        name=words[i].text
        wordsList.append(name)
    print(wordsList)

















youtubeİsim(URL)

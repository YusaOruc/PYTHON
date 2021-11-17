import requests
from bs4 import BeautifulSoup

baseUrl='https://itch.io/game-assets/'
dizi=["new-and-popular/free/tag-tilemap","free/tag-tilemap","top-sellers/free/tag-tilemap"]
#new and Popular=new-and-popular/free/tag-tilemap
#soup.find_all('p', class_='outer-text')
#solmenu = source.find_all("a",attrs={"class":"item_1523a"})
def Youtube(url,dizi):

    for i in range(len(dizi)):
        sayfa=url+dizi[i]
        page = requests.get(sayfa)
        soup = BeautifulSoup(page.text, 'html.parser')


        deneme1 = soup.find_all(class_="grid_outer")
        deneme1 = soup.find_all(class_="game_title")
        for i in deneme1:
            print(i.text)
        print("------------------------------------------------")




Youtube(baseUrl,dizi)
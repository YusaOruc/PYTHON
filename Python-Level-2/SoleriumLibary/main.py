import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://www.youtube.com/watch?v=mkJK_44YZ_I"
browser=webdriver.Firefox()
browser.get(url)
html=browser.page_source
soup=BeautifulSoup(html,'html.parser')
print(soup)

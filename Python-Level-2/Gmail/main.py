import gettext
import smtplib
from typing import Any, Union
import time
import requests
from bs4 import BeautifulSoup

URL='https://www.amazon.com.tr/JBLC100SIUBLK-C100-JBL-Kulak-Kulaklık/dp/B01DEWVZ2C/?_encoding=UTF8&pd_rd_w=WM4Fp&pf_rd_p=84e5ee78-99ba-4bbf-ab40-3d08d46687dd&pf_rd_r=H9FAMNPTDDHC9BMFQP0X&pd_rd_r=91221ca4-b5d9-4c26-b27f-385c9e8eb676&pd_rd_wg=RePnS&ref_=pd_gw_crs_zg_bs_13709880031'

headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 OPR/76.0.4017.177"}
def price_check(URL,max_price):
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')
    price = soup.find(id='priceblock_ourprice').getText().strip()

    new_price = float(price[0:4].replace(",", "."))

    if (new_price < max_price):
        send_email("h.yusa98@gmail.com", URL)
    else:
        print("Fiyat değişmedi.")

def send_email(toMail,url):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("test51610898@gmail.com","Yusa.51610898")

    denemeUrl="dsfasfdasdfffffffffffffffffffff"
    msg="Link:  "+denemeUrl+"Fiyat düştüü"

    server.sendmail("test51610898@gmail.com",toMail,msg)
    print("Mesaj Gönderildi")
    server.quit()

while(True):
    price_check(URL, 20)
    time.sleep(5)








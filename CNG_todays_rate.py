import requests
from bs4 import BeautifulSoup

url ='https://www.mypetrolprice.com/7/CNG-price-in-Pune'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

CNG_rate = soup.find(id="BC_TitleLabel").get_text().strip()
print(CNG_rate)

CNG = soup.find(class_="fnt27")

for CNG_p in CNG:
    soup = BeautifulSoup(CNG_p, 'html.parser')
    result = soup.select('div')
    if CNG_p:
        break
    CNG_price = result[0].text.strip().split()[-1]    
print(CNG_p)
CNG_price = float(CNG_p.text.replace("₹ ",""))
print(CNG_price)
print(type(CNG_price))
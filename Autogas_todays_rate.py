import requests
from bs4 import BeautifulSoup

url ='https://www.mypetrolprice.com/7/AutoGas-price-in-Pune'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

autogas_rate = soup.find(id="BC_TitleLabel").get_text().strip()
print(autogas_rate)

autogas = soup.find(class_="fnt27")

for autogas_p in autogas:
    soup = BeautifulSoup(autogas_p, 'html.parser')
    result = soup.select('div')
    if autogas_p:
        break
    autogas_p = result[0].text.strip().split()[-1]    
print(autogas_p)
autogas_price = float(autogas_p.text.replace("₹ ",""))
print(autogas_price)
print(type(autogas_price))


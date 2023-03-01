import requests
from bs4 import BeautifulSoup

url ='https://www.mypetrolprice.com/7/Diesel-price-in-Pune'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

diesel_rate = soup.find(id="BC_TitleLabel").get_text().strip()
print(diesel_rate)

diesel = soup.find(class_="fnt27")

for diesel_p in diesel:
    soup = BeautifulSoup(diesel_p, 'html.parser')
    result = soup.select('div')
    if diesel_p:
        break
    diesel_p = result[0].text.strip().split()[-1]    
print(diesel_p)
diesel_price = float(diesel_p.text.replace("₹ ",""))
print(diesel_price)
print(type(diesel_price))

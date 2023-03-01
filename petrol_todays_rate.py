import requests
from bs4 import BeautifulSoup

url ='https://www.mypetrolprice.com/7/Petrol-price-in-Pune'

headers = {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup)

petrol_rate = soup.find(id="BC_TitleLabel").get_text().strip()
print(petrol_rate)

petrol = soup.find(class_='fnt27')


for petrol_p in petrol:
    soup = BeautifulSoup(petrol_p, 'html.parser')
    result = soup.select('div')
    if petrol_p:
        break
    petrol_p = result[0].text.strip().split()[-1]    
print(petrol_p)
print(type(petrol_p))
petrol_price = float(petrol_p.text.replace("₹ ",""))
print(petrol_price)
print(type(petrol_price))
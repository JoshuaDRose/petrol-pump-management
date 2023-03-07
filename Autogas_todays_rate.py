# # -*- coding=utf-8 -*-
import logging
from logging.config import fileConfig

from bs4 import BeautifulSoup
import requests

logger: logging.Logger = fileConfig('config.ini')
logger.setLevel(logging.DEBUG)

URL ='https://www.mypetrolprice.com/7/AutoGas-price-in-Pune'
HEADERS = {
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"
        }

get_request = requests.get(URL, HEADERS)
soup = BeautifulSoup(page.content, 'html.parser')

logger.debug(soup)

# This a static title - at least on my client.
autogas_title_static = soup.find(id="BC_TitleLabel").get_text().strip()

autogas = soup.find(class_="fnt27")

for autogas_p in autogas:
    soup = BeautifulSoup(autogas_p, 'html.parser')
    result = soup.select('div')
    if autogas_p:
        break
    autogas_p = result[0].text.strip().split()[-1]    

logger.debug(autogas_p)
autogas_price = float(autogas_p.text.replace("₹ ",""))

logger.debug(autogas_price)
logger.debug("{autogas_price_repr} type={autogas_price_type}".format(
    autogas_price_repr=autogas_price.__repr__(),
    autogas_price_type=type(autogas_price),)


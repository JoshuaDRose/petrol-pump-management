import logging
from logging.config import fileConfig

from bs4 import BeautifulSoup
import requests

fileConfig(open('config.ini'))
logger = logging.getLogger()

HEADERS = { 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" }


def get_prices(_type="AutoGas") -> list[str]:
    """ 
    🏎️ - AutoGas 
    🚚 - Diesel 
    🚉 - Petrol 
    🔋 - CNG 
    """

    request = requests.get(f'https://www.mypetrolprice.com/7/{_type}-price-in-Pune', HEADERS)
    soup = BeautifulSoup(request.content, 'html.parser') # 🍜
    string_title: str = soup.find(id="BC_TitleLabel").get_text().strip()
    prices = [''.join(list(i.contents)[0][2:]) for i in soup.select("div .fnt27")]

    return prices

import colorama
import logging
from logging.config import fileConfig
import os
import re

from bs4 import BeautifulSoup
import requests

fileConfig(open('config.ini'))
logger = logging.getLogger()

colorama.init()

HEADERS = { 'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36" }
COLORS = {
        'RED': colorama.Fore.RED,
        'YELLOW': colorama.Fore.YELLOW,
        'MAGENTA': colorama.Fore.MAGENTA,
        'GREEN': colorama.Fore.GREEN,
        'BLUE': colorama.Fore.BLUE
        }

def get_prices(_type="AutoGas") -> list[str]:
    """ 
    🏎️ - AutoGas 
    🚚 - Diesel 
    🚉 - Petrol 
    🔋 - CNG 
    """
    print(colorama.Fore.LIGHTWHITE_EX + "Fetching prices... " + colorama.Fore.RESET)
    request = requests.get(f'https://www.mypetrolprice.com/7/{_type}-price-in-Pune', HEADERS)
    soup = BeautifulSoup(request.content, 'html.parser') # 🍜
    # string_title: str = soup.find(id="BC_TitleLabel").get_text().strip()
    prices = list([''.join(list(i.contents)[0][2:]) for i in soup.select("div .fnt27")]) # pyright: ignore

    return prices[0] # pyright: ignore

def clear_screen():
    """ Clear screen for all operating systems 🖥️ """
    if os.name == 'posix':
        os.system('clear')
        return
    os.system('cls')

def line_break(count=10):
    """ Break lines a bit """
    clear_screen()
    for _ in range(count): print('\n')

import os
import sys
import email
import random
import smtplib
import util
import datetime
import colorama

import logging
from logging.config import fileConfig

import sys
from fpdf import fpdf
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email_pass import mail, pass_mail

from util import COLORS as colors, clear_screen

colorama.init()

fileConfig(open('config.ini'))
logger = logging.getLogger()

looping = True  # 🔁

def select_fuel(colored = False):
    """ Ask the operartor which fuel they wish to purchase """
    choice = input(" >> ")
    choices = [colors['BLUE']   + 'Petrol' + colorama.Fore.RESET,
               colors['YELLOW'] + 'Diesel' + colorama.Fore.RESET,
               colors['MAGENTA']+ 'CNG'    + colorama.Fore.RESET,
               colors['GREEN']  + 'Autogas'+ colorama.Fore.RESET]
    choices_raw = ['Petrol', 'Diesel', 'CNG', 'AutoGas']

    choice = choices_raw[int(choice) - 1]
    if colored:
        return choices[int(choice) - 1]
    return choices_raw[int(choice) - 1]

def ask_for_amount(fuel) -> float: # pyright: ignore
    """ Ask the operator how much fuel they want to purchase """
    util.line_break(count=1)
    cpl = float(util.get_prices(_type=fuel)) # pyright: ignore
    util.line_break(count=1)
    while 1:
        print(f"Selection: {colorama.Fore.LIGHTWHITE_EX}{fuel} {colorama.Fore.WHITE}(₹ {cpl} per. Liter){colorama.Fore.RESET}")
        print(f"Please enter in units (Liters) how much fuel you wish to purchase {colorama.Fore.YELLOW}(maximum of 50){colorama.Fore.RESET}\n")

        choice = int()

        try:
            choice = int(input(" >> "))
        except Exception:
            util.line_break(1)
            continue

        if choice > 50:
            util.line_break(1)
            continue
        elif choice <= 0:
            util.line_break(1)
            continue

        return cpl * choice

    
def main():
    
    sys.argv()
    
    if '--help' in sys.argv():
        print("See README.md for help")
        sys.exit()

    while looping:
        try:
            util.clear_screen()

            print(f""" Digital Fuel Station ⛽

      {colors['BLUE']} 1. Petrol
      {colors['YELLOW']} 2. Diesel
      {colors['MAGENTA']} 3. CNG
      {colors['GREEN']} 4. Autogas

     {colors['RED']}Exit (CTRL + C){colorama.Fore.RESET}

            """)

            fuel = select_fuel(colored=False)
        except Exception:
            util.line_break(1)
            continue

        cost = ask_for_amount(fuel)
        print(f"Order: {cost} Litres of {fuel}")
        print(f"Total: {colorama.Fore.LIGHTWHITE_EX}₹{cost}{colorama.Fore.RESET}")
        input()

if __name__ == "__main__":
    main()

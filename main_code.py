import datetime
import random
from fpdf import FPDF
import sys
from email_pass import mail, pass_mail
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders 
from petrol_todays_rate import petrol_rate,petrol_price
from diesel_todays_rate import diesel_rate,diesel_price
from CNG_todays_rate import CNG_rate, CNG_price
from Autogas_todays_rate import autogas_rate ,autogas_price

try:
    print("\t\t\t\t\tWELCOME TO DIGITAL FUEL STATION ")

    print("******List Of Available Fuels******")
    print("1]Petrol")
    print("2]Diesel")
    print("3]CNG")
    print("4]Autogas")
    print("4]Exit")

    while (True):
        choice = int(input("Enter Your Choice [1/2/3/4/5] = "))
        if choice in [1,2,3,4,5]:
            if (choice == 1):
                print("You Have Selected PETROL")
                fuel = 'petrol'
                print(petrol_rate)
                print(petrol_price)
                amount = float(input("Enter Amount = "))
                qauntity = 0.0
                qauntity = amount/(petrol_price)   
                print(f"You Got {round(qauntity)} Liters PETROL of Rs.{amount}")
            
            elif (choice == 2):
                print("You Have Selected DIESEL")
                fuel = 'Diesel'
                print(diesel_rate)
                print(diesel_price)
                amount = float(input("Enter Amount = "))
                qauntity = 0.0
                qauntity = amount/(diesel_price)   
                print(f"You Got {qauntity} Liters DIESEL of Rs.{amount}")

            elif (choice == 3):
                print("You Have Selected CNG")
                fuel = 'CNG'
                print(CNG_rate)
                print(CNG_price)
                amount = float(input("Enter Amount = "))
                qauntity = 0.0
                qauntity = amount/(CNG_price)   
                print(f"You Got {qauntity} Liters of CNG of Rs.{amount}")
            
            elif (choice == 4):
                print("You Have Selected Autogas")
                fuel = 'Autogas'
                print(autogas_rate)
                print(autogas_price)
                amount = float(input("Enter Amount = "))
                qauntity = 0.0
                qauntity = amount/(autogas_price)   
                print(f"You Got {qauntity} Liters Autogas of Rs.{amount}")
                
            elif (choice == 5):
                print("EXIT...")
        print('-'*60)
        chc =input('Do you want your bill pdf [yes/no] : ')
        if chc =='yes':
            print('-'*60)
            email =input('enter your mail address : ')

            #current date time
            date_time = datetime.datetime.now()
            print(date_time)

            #creating bill
            bill_no = random.randint(999999,9999999)

            pdf = FPDF()
            pdf.add_page()
            pdf.set_font('Times', size=15) 
            pdf.text(30,25,txt = f"Digital fuel Station")
            pdf.text(30,30,txt = f"Date & Time - {date_time}")
            pdf.text(30,35,f"Bill no - {bill_no}")
            pdf.text(30,40,txt = f"You Got - {round(qauntity,2)} Liters {fuel}")
            pdf.text(30,45,txt = f"Amount is - {amount}")
            pdf.text(30,50,txt = "Thank You... Visit Again !!!")
            bill = f"DFS {bill_no}.pdf"
            pdf.output(bill)
            record =("D:/petrol_pump/{bill}")

            #send email pdf
            
    # Send Created Bill PDF In Gmail 

            fromaddr = mail
            pwd =  pass_mail
            toaddr = email
            msg = MIMEMultipart() 
            msg['From'] = fromaddr 
            msg['To'] = toaddr
            msg['Subject'] = "Regarding fuel bill"
            body = "This is auto-generated mail regarding the fuel bill"
            msg.attach(MIMEText(body,'plain'))
            attachment = open(f"D:/petrol_pump/{bill}", "rb")

            # instance of MIMEBase and named as p
            p = MIMEBase('application', 'octet-stream')

            # To change the payload into encoded form
            p.set_payload((attachment).read()) 
            encoders.encode_base64(p)   
            p.add_header('Content-Disposition', "attachment; filename= %s" % bill)
            msg.attach(p)
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(fromaddr,pwd) 
            text = msg.as_string()
            s.sendmail(fromaddr, email , text)
            s.quit()
            
            print("Pdf of bill is successfully sent to your mail address")
            break

        else :
            print("visit again ....have a nice day")
                    
except BaseException as ex:
    print(ex)
finally:
    print("THANK YOU....PLEASE VISIT AGAIN")
    

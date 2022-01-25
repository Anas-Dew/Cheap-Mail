import smtplib 
from os import system, name
import pyfiglet
from termcolor import cprint


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')
           
title = pyfiglet.figlet_format("CHEAP-MAIL")
cprint(str(title),'blue')
cprint("\t\t\t\tFastest Mail Service",'green')

dec = input("\nEnter Anykey to Login")
clear()
cprint('Gmail : ','red')
gmailaddress = input()
cprint('Password : ','red')
gmailpassword = input()
cprint('Contact Email :','red')
mailto = input()
cprint('Message Here :','green')
msg = input()
try :
    mailServer = smtplib.SMTP('smtp.gmail.com' , 587)
    mailServer.starttls()
    mailServer.login(gmailaddress , gmailpassword)
    mailServer.sendmail(gmailaddress, mailto , msg)
    clear()

    print(" \nEmail Sent!")
    mailServer.quit()
except:
    cprint('Email Failed !!!','red')

out = pyfiglet.figlet_format("THANKS BUDDY !!!")
cprint(str(out),'green')

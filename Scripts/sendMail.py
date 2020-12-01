import os
import smtplib
from datetime import datetime


def sendEmail(fun_of, dict_of):
    EMAIL_ADDRESS = dict_of["address"]
    EMAIL_PASSWORD = dict_of["password"]

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        now = datetime.now()
        current_time = now.strftime("%H:%M%S")

        subject = "Task finished"
        body = fun_of.__name__ + " finished at " + current_time

        msg = f'Subject:{subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, dict_of['to'], msg)

def doAndEmail(fun_of, dict_of, *argv, **kwargs):
    fun_of(*argv, **kwargs)
    sendEmail(fun_of, dict_of)


def dummy(test):
    print("Hello "+ test)


def test():
    dict_of = dict()
    dict_of["address"] = ""
    dict_of["password"] = ""
    dict_of["to"] = ""
    
    doAndEmail(dummy, dict_of, test = "Neverland")

if __name__ == "__main__":
    test()

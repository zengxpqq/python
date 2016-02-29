#!usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
import sys

GMAIL_SMTP_SERVER = "smtp.gmail.com"
GMAIL_SMTP_PORT = 587

GMAIL_EMAIL = "zengxp@in-mail.base-fx.com"
GMAIL_PASSWORD = "ZXP$^+032"

def initializa_smtp_server():
    smtpserver = smtplib.SMTP(GMAIL_SMTP_SERVER, GMAIL_SMTP_PORT)
    smtpserver.ehlo()
    smtpserver.atarttls()
    smptserver.ehlo()
    smtpserver.login(GMAIL_EMAI, GMAIL_PASSWORD)
    return smtpserver
    
def send(email):
    to_email = email
    from_email = GMAIL_EMAIL
    subj = 'hey man, what\'up'
    
    header = "To: %s \nfrom: %s \nsubject: %s \n" %(to_email, from_email, subj)
    
    msg_body = "thank you" 
    content = header + "\n" + msg_body
    smtpserver = initializa_smtp_server()
    smtpserver.sendmail(from_email, to_email, content)
    smtpserver.close()
    
if __name__ == "__main__":
    email = "zengxp@in-mail.base-fx.com"
    send(email)
    print 'done!'

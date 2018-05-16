#!/usr/bin/env python
# -*- coding: utf-8 -*-

# send mail utf-8 using gmail smtp server

from email.mime.text import MIMEText
from email.Header import Header
from email.Utils import formatdate
import smtplib

import RPi.GPIO as GPIO
import dht11
from time import sleep
from datetime import datetime
import csv


# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=14)

def send_email(from_addr, to_addr, subject, body, server='smtp.gmail.com', port=587):
    encoding='utf-8'
    msg = MIMEText(body.encode(encoding), 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    _user = "GMAIL_USER_NAME"
    _pass = "GMAIL_PASSWORD"

    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('team.pronoob123', 'yuki1238')
    smtp.sendmail(from_addr, [to_addr], msg.as_string())
    smtp.close()

f=open("data_temperature_mail.csv","w")

try:
    while True:
        result = instance.read()
        if result.is_valid():
            print("Last valid input: " + str(datetime.now()))
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
            t=result.temperature
            h=result.humidity
            time=datetime.now()
            data=[time,t,h]
            writer=csv.writer(f,lineterminator="\n")
            writer.writerow(data)
	    
	    body=str(data)
	    send_email('team.pronoob123@gmail.com', 's14517@salesio-sp.ac.jp',u'センサーデータ', body)
	    
            sleep(30)
except KeyboardInterrupt:
    print("end")
    f.close()
    pass

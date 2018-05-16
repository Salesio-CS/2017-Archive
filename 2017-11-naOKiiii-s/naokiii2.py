# -*- coding: utf-8 -*-
import traceback
from functools import wraps
import time
import RPi.GPIO as GPIO
import picamera
import smtplib
from email import Encoders
from email.Utils import formatdate
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
import os.path
import datetime

__author__ = 'isann'

def create_message(from_addr, to_addr, subject, body, attach_file):
    """
    Mailのメッセージを構築する
    """
    msg = MIMEMultipart()
    msg["Subject"] = subject
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()

    body = MIMEText(body)
    msg.attach(body)

    # 添付ファイルのMIMEタイプを指定する
    attachment = MIMEBase("image","jpeg")
    # 添付ファイルのデータをセットする
    file = open(attach_file)
    attachment.set_payload(file.read())
    file.close()
    Encoders.encode_base64(attachment)
    msg.attach(attachment)
    attachment.add_header("Content-Disposition","attachment", filename=attach_file)

    return msg


def wrapper(func):
    @wraps(func)
    def _func(*args, **keywords):
        try:
            func(*args, **keywords)
        except Exception:
            traceback.print_exc()

    return _func


@wrapper
def main():
    sensor_pin = 18
    sleeptime = 5

   # GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(sensor_pin, GPIO.IN)

    cam = picamera.PiCamera()
    cam.resolution = (1920, 1080)

    try:
        print "App Start"
        print "ctrl+c  :  if you want to stop app"
        while True:
            if (GPIO.input(sensor_pin) == GPIO.HIGH):
                print('shot!!!!')
                filename = 'naoki.jpg'
                save_file = '/home/pi/Public' + '/' + filename
                cam.capture(save_file)
                msg = create_message(me, you, subject, body, save_file)
                print('wait...')
                s.sendmail(me,you,msg.as_string())
                print('OK!!')
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        print "Quit"
    finally:
        print "clean up"
        GPIO.cleanup()
        s.quit()

if __name__ in '__main__':
    me = "raspi.naoki@gmail.com"
    username=me
    passwd="raspberry"
    you = "raspi.naoki2@gmail.com"
    subject =  "Sensor was reaction."
    body = time.strftime('%Y/%m/%d/%H/%M/%S')  
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, passwd)
    main()

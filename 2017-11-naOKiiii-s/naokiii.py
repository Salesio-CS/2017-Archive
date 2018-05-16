# -*- coding: utf-8 -*-
# 2016/12/20 0:51
import traceback
from functools import wraps
import time
import RPi.GPIO as GPIO
import picamera
import smtplib
from email.mime.text import MIMEText

__author__ = 'isann'

if __name__ == '__main__':

    # 以下の内容を変更する
    # me : 自分のGmail アドレス, you : 送信先のアドレス, passwd : Gmailパスワード
    me = "raspi.naoki@gmail.com"
    passwd = "raspberry"
    you = "s14528@salesio-sp.ac.jp"
    titletext = "タイトル"
    body = "本文"

    msg = MIMEText(body)
    msg['Subject'] = titletext
    msg['From'] = me
    msg['To'] = you

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, passwd)

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
                filename = time.strftime('%Y%m%d%H%M%S') + '.jpg'
                save_file = '/home/pi/Public' + '/' + filename
                cam.capture(save_file)
                s.sendmail(me,you,msg.as_string())
                time.sleep(sleeptime)
                print('wait...')
            else:
                time.sleep(1)
    except KeyboardInterrupt:
        print "Quit"
    finally:
        print "clean up"
        GPIO.cleanup()
        s.quit()

if __name__ in '__main__':
    main()

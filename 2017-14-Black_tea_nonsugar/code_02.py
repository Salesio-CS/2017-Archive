#/usr/bin/env python
#-*- coding utf-8 -*-

import numpy as np
import time
import PRi.GPIO as GPIO
import cv2
import smtplib
from email.MIMEText import MIMEText
from email.Header import Header

INTAVAL = 10
SLEEPTIME = 1.5
SENSOR_PIN = 18
c = cv2.VideoCapture(0)
i = 0

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN,GPIO.IN)

def create_msg(from_address,to_address,subjecct,body,encode):
	meg = MIMEText(body,`plain`,encode)
	msg[`Subject`] = Header(subject,encode)
	msg[`from`] = from_address
	msg[`to`] = to_adrress
	return msg

def send_by_local(from_address,to_address,msg):
	s = smtplib.SMTP()
	s.connect()
	s.sendmail(from_addess,[to_address],msg,as_string())
	s.close()
st = time.time() - INTAVAL

while Ture:
	print GPIO.input(SENSOR_PIN)
	if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
		st = time.time()
		r,img = c.read()
		ret,frame = c.read()
		frame = cv2.Canny(frame,324,200)
		cv2.imwrite(`22{}.jpg`,format(i),img)
		cv2.imshow(`fram.jpg`,frame)
		i = i + 1
		print(`worning`)

		if __name__  == `__main__`:
			from_addr = `mikkusupizza@gmail.com`
			to_addr = `mikkusupizza@gmail.com`
			subject = u`’Ê’m`
			body = u`•sRŽÒ‚ª‚¢‚½`
			enode = `ISO-2022-JP`

			msg = create_msg(from_addr,to_addr,subject,body,encode)
			
			send_by_local(from_addr,to_addr,msg)]

	time.sleep(SLEEPTIME)
	cv2.destroyAllWindows()

#!/usr/bin/env python
#-*- coding utf-8 -*-

import numpy as np
import time
import RPi.GPIO as GPIO
import cv2

INTAVAL = 10
SLEEPTIME = 1.5
SENSOR_PIN = 18
c = cv2.VideoCapture(0)
i = 0

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

st = time.time() - INTAVAL

while Ture:
	print GPIO.input(SENSOR_PIN)
	if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
		st = time.time()
		r, img = c.read()
		ret, frame = c.read()
		frame = cv2.Canny(frame, 324, 200)
		cv2.imwrite(`test{}.jpg`.format(i), img)
		cv2.imshow(`frame`, frame)
		i = i + 1
		print("warning")
	time.sleep(SLEEPTIME)
	cv2.destroyAllWindows()

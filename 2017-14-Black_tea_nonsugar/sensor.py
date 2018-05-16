#!/usr/bin/env python
#-*- coding utf-8 -*-

import time
import RPi.GPIO as GPIO

INTAVAL = 0.1
SLEEPTIME = 5
SENSOR_PIN = 18

GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

st = time.time() -INTAVAL

while Ture:
  print GPIO.input(SENSOR_PIN)
  if(GPIO.input(SENSOR_PIN) == GPIO.HIGH) and (st + INTAVAL < time.time()):
    st = time.time()
    print('worning')
  time.sleep(SLEEPTIME)

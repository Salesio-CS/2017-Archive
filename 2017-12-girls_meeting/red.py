# -*- coding: utf-8 -*-

import webiopi

GPIO = webiopi.GPIO

RED   = 22
GREEN = 17
BLUE  = 27
 
def setup():
    # GPIOをPWMに設定
    GPIO.setFunction(RED  , GPIO.PWM)
    GPIO.setFunction(GREEN, GPIO.PWM)
    GPIO.setFunction(BLUE , GPIO.PWM)

def destroy():
   # 消灯
    GPIO.pwmWrite(RED  , 0)
    GPIO.pwmWrite(GREEN, 0)
    GPIO.pwmWrite(BLUE , 0)

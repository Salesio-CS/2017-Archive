# coding: utf-8
import wiringpi                    # GPIO control Library
import time                          # timer Library

led_pin = 23 #GPIOの端子番号 
                     #GPIO terminal number
                     # Pin 16

wiringpi.wiringPiSetupGpio() # Initialize GPIO

wiringpi.pinMode( led_pin, 1 ) # GPIOを出力モード（1）に設定
                                                 #Set GPIO to output mode (1)
while True:               #while loop
    wiringpi.digitalWrite( led_pin, 1 )　# GPIOを3.3VにしてLEDを点灯
                                                            #Lights the LED with GPIO set to 3.3 V
    time.sleep(1)                  # wait 1 sec
   
    wiringpi.digitalWrite( led_pin, 0 )  # GPIOを0VにしてLEDを消灯
                                                            #Lights the LED with GPIO set to 0 V
    time.sleep(1)                 # wait 1 sec
# coding: utf-8
import wiringpi                    # GPIO control Library
import time                          # timer Library

led_pin = 23 #GPIO�̒[�q�ԍ� 
                     #GPIO terminal number
                     # Pin 16

wiringpi.wiringPiSetupGpio() # Initialize GPIO

wiringpi.pinMode( led_pin, 1 ) # GPIO���o�̓��[�h�i1�j�ɐݒ�
                                                 #Set GPIO to output mode (1)
while True:               #while loop
    wiringpi.digitalWrite( led_pin, 1 )�@# GPIO��3.3V�ɂ���LED��_��
                                                            #Lights the LED with GPIO set to 3.3 V
    time.sleep(1)                  # wait 1 sec
   
    wiringpi.digitalWrite( led_pin, 0 )  # GPIO��0V�ɂ���LED������
                                                            #Lights the LED with GPIO set to 0 V
    time.sleep(1)                 # wait 1 sec
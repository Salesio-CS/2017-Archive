import wiringpi
import time

led_pin=0

wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(led_pin,1)

while True:
    wiringpi.digitalWrite(led_pin,1)
    time.sleep(5)

    wiringpi.digitalWrite(led_pin,0)
    time.sleep(5)

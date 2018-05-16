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

f=open("data_temperature.csv","w")

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

            sleep(10)
except KeyboardInterrupt:
    print("end")
    f.close()
    pass

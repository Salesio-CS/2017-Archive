#coding: utf-8
 
import RPi.GPIO as GPIO
import dht11
import datetime
from upload_Values import upload_data

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# pin 14を読み込む
instance = dht11.DHT11(pin=14)

result=instance.read()
if result.is_valid():
    #データを格納
    temp = result.temperature
    hum = result.humidity
 
    print temp
    print hum
 
    #webへPOST
    upload_data(temp,hum);

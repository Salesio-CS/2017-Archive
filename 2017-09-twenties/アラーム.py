import RPi.GPIO as GPIO
import time

SOUNDER = 21
DOREMI_Hz = [
            830 ,830 , 5 ,783 , 5,698,
            698,5 ,698 , 5, 5, 5,
            830 ,830, 5,783, 5, 698,
 
            698, 698, 698, 5, 5, 5,
            830 ,830, 5 ,783, 5,698,
            698, 5,698, 5, 5,5,

            830, 830, 5,783, 5 ,698,
            783, 783, 783, 5 ,5, 5,
            783, 783, 5, 698, 5, 622,

            622, 5, 622, 5, 5, 5,
            783, 783, 5, 698, 5,622,
            622, 5,622, 5, 5, 5,

            783 ,783, 5, 698, 5,622,
            622, 5, 622, 5, 5, 5,
            698, 830, 5, 783, 5, 698,

            698 ,698, 698, 698, 698 ,698]


GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)

p = GPIO.PWM(SOUNDER, 21)
p.start(1)


for Hz in DOREMI_Hz :
    p.ChangeFrequency(Hz)
    time.sleep(0.18)

p.stop()
GPIO.cleanup()

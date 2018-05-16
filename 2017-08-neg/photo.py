import picamera
import time
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(2)
camera.capture('/home/pi/Desktop/output.bmp')

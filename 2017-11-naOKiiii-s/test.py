import time
import picamera
with picamera.PiCamera() as camera:
	camera.resolution=(1920,1080)
	camera.start_preview()
	time.sleep(2)
	camera.capture('unmo.jpg')
# 2017-11-naOKiiii-s
# 2017-11-na0Kiiii-s

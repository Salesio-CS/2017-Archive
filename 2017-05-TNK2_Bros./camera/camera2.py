import datetime
import picamera
import os
import time

now = datetime.datetime.now()
dir_name = now.strftime('%Y%m%d')
dir_path = '/home/pi/nas/'+dir_name
file_name = now.strftime('%H%M%S')

if not os.path.exists(dir_path):
        os.makedirs(dir_path)
        os.chmod(dir_path,0777)

picamera = picamera.PiCamera()

x = 0        
while x < 10:
        now = datetime.datetime.now()
        dir_name = now.strftime('%Y%m%d')
        dir_path = '/home/pi/nas/'+dir_name
        file_name = now.strftime('%H%M%S')
	
	time.sleep(20)	

        picamera.capture(dir_path+'/'+file_name+'.jpg')
        x+=1

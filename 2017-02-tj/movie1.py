import picamera
import time
import io
import subprocess
from _future
from _future_ import print_function
import socket
import time
from contextlib import closing

def main():
    host = 127.0.0.1
    port = 4000
    count = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    with closing(sock)
     while True:
       message = 'Desktop/python_movie/movie.h264',format(count).encode('utf-8')
       print(message)
       sock.sendto(message,(host,port))
       count += 1
       time.sleep(1)
    return

if __name__ == '__main__':

    main()
    

with picamera.PiCamera() as camera:
    camera.resolution=(1024,768)
    camera.start_preview()
    camera.start_recording('Desktop/python_movie/movie.h264')
    camera.wait_recording(5)
    camera.stop_recording()
    camera.stop_preview()
subprocess.call('MP4Box -fps 30 -add Desktop/python_movie/movie.h264 movie.mp4',shell=True)
    

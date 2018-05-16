from img_trim import KnowledgeImgTrim
import csv_time as take
from ftplib import FTP
import datetime
import picamera
import calendar
import time
import os


print("")
print("============================")
print("===== KNOWLEDGE START ======")
print("===== TEAM: TNK2.BROS. =====")
print("============================")
print("")

# ftp start
ftp = FTP("192.168.0.116", "pi", passwd="renren")
print("ftp OK")

camera = picamera.PiCamera()
camera.hflip = True # camera rotation
camera.vflip = True # camera rotation

now = datetime.datetime.now()

dir_name = now.strftime('%Y%m%d')
dir_path = '/home/pi/data/'+dir_name # time->dirname

# not found then make dir
if not os.path.exists(dir_path):
    os.makedirs(dir_path)
    os.chmod(dir_path, 0o777)
    ftp.mkd("/var/www/html/img/+dir_name")

now = datetime.datetime.now()
file_name = now.strftime('%H%M%S')

save_path = dir_path+'/'+file_name+'.jpg'
camera.capture(save_path)

prc = KnowledgeImgTrim(dir_name, "img")

for i in range(10):
    with open("data.csv", "wb") as f:
        ftp.retrbinary("RETR /data.csv", f.write)


    #csv_time.pyと時間からフラグ設定
    #強制的に取る場合はa=1
    a = take.take_pic()

    if a == 1:
        now = datetime.datetime.now()

        dir_name = now.strftime('%Y%m%d')
        dir_path = '/home/pi/data/'+dir_name # time->dirname

        # not found then make dir
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            os.chmod(dir_path, 0o777)
            ftp.mkd("/var/www/html/img/+dir_name")

        now = datetime.datetime.now()
        file_name = now.strftime('%H%M%S')

        save_path = dir_path+'/'+file_name+'.jpg'


        camera.capture(save_path)

        # image trimming
        prc.real_trim(dir_name,"img")

        # upload
        with open(save_path, "rb") as f:
            print("upload file:" + str(i))
            ftp.storbinary("STOR /var/www/html/img/"+ dir_name + '/' + file_name + ".jpg", f)



print("\n============================")
print("===== KNOWLEDGE FINISH =====")
print("============================")
print("\n")

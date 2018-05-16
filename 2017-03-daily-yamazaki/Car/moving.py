#coding:utf-8
import reciver
import RPi.GPIO as GPIO
import os
import cv2

index = 0
def pict():
    c=cv2.VideoCapture(0)
    c.read()
    r,img=c.read()
    file_name = 'capture' + index + '.jpg'
    cv2.imwrite(file_name,img)
    os.system('sudo mv ' + file_name + '/var/www/html')
    if index >= 9:
        index = 0
    else:
        index += 1
    c.release()

def func(way, rpin, rpin2, lpin, lpin2):      #方向(string)
    right = False   #右のタイヤの電源
    left = False    #左のタイヤの電源
    if way == "straight":   #前進
        GPIO.output(rpin, True)
        GPIO.output(rpin2, True)
        GPIO.output(lpin, True)
        GPIO.output(lpin2, True)
        right = True
        left = True
    elif way == "right":    #右折
        GPIO.output(rpin, False)
        GPIO.output(rpin2, False)
        GPIO.output(lpin, True)
        GPIO.output(lpin2, True)
        right = False
        left = True
    elif way == "left":     #左折
        GPIO.output(rpin, True)
        GPIO.output(rpin2, True)
        GPIO.output(lpin, False)
        GPIO.output(lpin2, False)
        right = True
        left = False
    elif way == "stop":
        GPIO.output(rpin, False)
        GPIO.output(rpin2, False)
        GPIO.output(lpin, False)
        GPIO.output(lpin2, False)
        GPIO.cleanup()
    elif way == "other":
        GPIO.output(rpin, False)
        GPIO.output(rpin2, False)
        GPIO.output(lpin, False)
        GPIO.output(lpin2, False)
    elif way == "pict":
        pict()

    if right:
        #print("right")
        GPIO.output(rpin ,True)
        GPIO.output(rpin2, True)
    if left:
        #print("left")
        GPIO.output(lpin ,True)
        GPIO.output(lpin2 ,True)
    #GPIO.output(lpin, right)  #右のタイヤの設定を反映
    #GPIO.output(rpin, left)   #左のタイヤの設定を反映
    print((left, right))
    return (left, right)

host = ""  #リモコン側のIPアドレス
rpin, rpin2 = 33, 35   #左右のピン番号
lpin, lpin2 = 23, 21   # 3533, 2123
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)  #ピン番号をボードの番号で指定する宣言
GPIO.setup(rpin, GPIO.OUT)
GPIO.setup(rpin2, GPIO.OUT)
GPIO.setup(lpin, GPIO.OUT)
GPIO.setup(lpin2, GPIO.OUT)
reciver.transmission(host, func, rpin, rpin2, lpin, lpin2)

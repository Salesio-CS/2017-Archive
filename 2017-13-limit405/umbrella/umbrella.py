#coding utf-8
#Apache

import urllib.request
import urllib.parse #URLエンコード
import subprocess
import time

#url=input()
#url=""
HOST = input("HOST?> ")

#加速度センサーによる判定
def is_have_by_acceleration():
    #ここに加速度センサーによる判定を書いてどうぞ．
    dir = "./adxl345-python/adxlex.py"
    cmd = "python " + dir
    print("called: \'" + cmd + "\'")

    adxl = subprocess.check_output(cmd, shell=True)
    adxl = str(adxl)
    adxl = adxl.split("\'")
    adxl = adxl[1].split("\n")
    adxl = list(adxl[0])
    #
    if adxl[0] == "-":
        #print("sashiteru")
        return True
    else:
        #print("no sashiteru")
        return False

#デバイスによる判定
def is_have_by_device():
    #ここにデバイス(イヤホンジャックとかね)
    usb = subprocess.check_output("df | wc -l",shell=True)#(usb = 9:usb無し 10:usbあり)
    usb = str(usb)
    usb = usb.split("\'")#何かで区切ってどうにかしろ
    if usb[1] == "10\\n":
        return False
    else:
        return True

#傘をさしているか否かを送信
#上二つの関数の真偽値のANDをとって判定
def send_have_am_umbrella():
    #HOST = "127.0.0.1"
    #最も簡単なHTTP通信(GETメソッドでURLをリクエストするだけ)
    is_have_an_umbrella = "0"
    if is_have_by_acceleration() and is_have_by_device():
        is_have_an_umbrella = "1"

    #source=発信元(umbrella:0 viewer:1) umbrella=真偽値(0/1)
    url = "http://" + HOST + ":8008/?source=0&umbrella="+is_have_an_umbrella

    print(url)

    with urllib.request.urlopen(url) as response: #この1行で送信

         html = response.read().decode("utf-8")
         print(html)

         #HTTPステータスコードを取得する
         status = response.getcode()
         print("Status code: " + str(status))

         #HTTPヘッダ受信
         headers = response.info()
         print(headers);

#main関数のようなもの
if __name__ == "__main__":
    while True:
        send_have_am_umbrella()
        time.sleep(5)

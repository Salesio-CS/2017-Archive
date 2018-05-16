#coding utf-8

import urllib.request
import urllib.parse #URLエンコード

#HOST = input("HOST?> ")
HOST = "127.0.0.1"
sender = input("from?> ")#発信元
flag = input("is_have_an_umbrella?> ")#傘さしてるかどうか

if sender == "0":
    #umbrella
    if flag == "0":
        #url = "http://192.168.0.125:8008/?source=0&umbrella=0"
        url = "http://" + HOST + ":8008/?source=0&umbrella=0"
    else:
        #url = "http://192.168.0.125:8008/?source=0&umbrella=1"
        url = "http://" + HOST + ":8008/?source=0&umbrella=1"
else:
    #viewer
    #url = "http://192.168.0.125:8008/?source=1"
    url = "http://" + HOST + ":8008/?source=1"


with urllib.request.urlopen(url) as response:
    html = response.read().decode("utf-8")
    print(html)
    #status code received.
    status = response.getcode()
    print("Status code: " + str(status))
    #HTTPヘッダ受信
    headers = response.info()
    print(headers)
    if sender == "1":
        if headers["is_have_an_umbrella"] == "1":
            print("さしているらしい．")
        else:
            print("さしていないらしい．")

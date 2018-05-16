#coding: utf-8

import urllib.request
import urllib.parse

def Viewer():

    #URLの指定
    URL = input()
    #URL = "192.168.0.128:8008"

    #URLの表示
    print(URL)

    #GET
    with urllib.request.urlopen(URL) as response

    #HTMLの表示
    HTML = response.read().decode("utf-8")
    print(HTML)

    #ステータスコードの取得
    status = response.getcode()
    print("Status Code : " + str(status))

    #ヘッダ受信
    headers = response.info()

    #特定のヘッダ表示
    print(headers["linux"])

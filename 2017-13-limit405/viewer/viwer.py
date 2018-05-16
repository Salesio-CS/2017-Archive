#!/usr/bin/env python
#coding: utf-8

import wx
import urllib


def viewer():

    #URLの指定
    URL = input()
    #URL = "192.168.0.128:8008"

    #URLの表示
    #print(URL)

    #GET
    with urllib.request.urlopen(URL) as response:

    #HTMLの表示
        HTML = response.read().decode("utf-8")
    #    print(HTML)

    #ステータスコードの取得
        status = response.getcode()
    #    print("Status Code : " + str(status))

    #ヘッダ受信
    headers = response.info()

    #特定のヘッダ表示
    return headers["linux"]

class TestFrame(wx.Frame):
    def __init__(self,parent,ID,title):

        #ウィンドウの作成
        wx.Frame.__init__(self,parent,-1,title,pos=(0,0),size=(320,240))
        panel=wx.Panel(self,-1)

        #ウィンドウテキスト
        text=wx.StaticText(panel,-1,"Umbrella Viewer",wx.Point(10,5),wx.Size(-1,-1))

class TestApp(wx.App):
    def OnInit(self):

        #条件によるテキスト分岐(0 : 傘が閉じている 1 : 傘が開いている)

        if viewer() == 0:
            StatusText = "The Umbrella is CLOSE !"

        else:
            StatusText = "The Umbrella is OPEN !"

        #テキスト表示
        frame=TestFrame(None,-1,StatusText)
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

#main

if __name__  == '__main__':

    app=TestApp()
    app.MainLoop()

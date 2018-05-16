#coding:utf-8
from __future__ import print_function
import socket
import time
from contextlib import closing

def transmission():
  host = "xxx.xxx.xxx.xxx"  #受信側のIPアドレス
  port = 4000
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    while True:
    　#ここから処理の例
      message = "HELLO"
      print(message)
      sock.sendto(message, (host, port)) #データの送信（ここではmessage
      time.sleep(1) 
      #ここまで
  return

if __name__ == "__main__":
  transmission()

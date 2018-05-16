#coding:utf-8
from __future__ import print_function
import socket
from contextlib import closing

def transmission():
  host = "xxx.xxx.xxx.xxx"    #送信側のIPアドレス
  port = 4000
  bufsize = 4096

  sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sckt):
    sckt.bind((host, port))
    while True:
      #ここから処理の例
      print(sckt.recv(bufsize)) #受け取ったデータの表示
      #ここまで
  return

if __name__ == "__main__":
  transmission()

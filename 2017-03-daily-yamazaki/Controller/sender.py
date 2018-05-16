#coding:utf-8
from __future__ import print_function
import socket
import time
from contextlib import closing

def transmission(host, func):
  port = 4000
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sock):
    while True:
      message = func()
      print(message)
      sock.sendto(message, (host, port)) #データの送信（ここではmessage
      if message == "stop":
          break
  return

def func():
    time.sleep(1)
    return "HELLO"

if __name__ == "__main__":
  transmission("192.168.0.21", func)

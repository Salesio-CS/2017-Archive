#coding:utf-8
from __future__ import print_function
import socket
from contextlib import closing

def transmission(host, func, rpin = False, rpin2 = False, lpin = False, lpin2 = False):
  port = 4000
  bufsize = 4096

  sckt = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  with closing(sckt):
    sckt.bind((host, port))
    while True:
      tmp = sckt.recv(bufsize)
      func(tmp, rpin, rpin2, lpin, lpin2)
      if tmp == "stop":
          break
  return

if __name__ == "__main__":
  transmission("localhost",print)

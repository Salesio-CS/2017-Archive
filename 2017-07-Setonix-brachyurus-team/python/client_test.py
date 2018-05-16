#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket



def main():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

	host = "192.168.1.17"
	port = 4096

	sock.connect((host,port))

	# 最初に受け取るゾ
	rep = sock.recv(1024).decode('utf-8')

	while True:
		mess = input()
		sock.send(mess.encode('utf-8'))
		rep = sock.recv(1024).decode('utf-8')
		print(rep)

		if rep == 'not close':
			break

if __name__ == '__main__':
	main()


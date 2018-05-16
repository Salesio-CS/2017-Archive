#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import signal
import time

import ipip

# ------------------------------------------------------------------------
# グローバルヴァリアヴォ
# ------------------------------------------------------------------------
counter = 0 # 内容量
kill_flag = False # 全体終了フラグ


# ------------------------------------------------------------------------
# 送信ゾ
# ------------------------------------------------------------------------
def send_message_to_client(clientsocket, message):
		while True:
			sent_len = clientsocket.send(message)
			if sent_len == len(message):
				break
			message = message[sent_len:] 


# ------------------------------------------------------------------------
# クライアントとやり取りするゾ
# ------------------------------------------------------------------------
def client_handler(clientsocket, client_address, client_port):
	# 宣言ズ
	global counter
	global kill_flag
	rep_flag = False
	close_flag = False

	# 初期の内容量送信
	rep = 'not upd ' + str(counter) + ' ' + str(ipip.read_circuit())
	send_message_to_client(clientsocket, rep.encode('utf-8'))

	while not close_flag and not kill_flag:
		try:
			message = clientsocket.recv(1024)
		except OSError:
			break

		if len(message) == 0:
			break;

		if message == 'req upd'.encode('utf-8'): # 情報更新要求
			rep = 'not upd ' + str(counter) + ' ' + str(ipip.read_circuit())
		elif message == 'req cw'.encode('utf-8'): # 内容量要求
			rep = 'not cw ' + str(counter)
			send_message_to_client(clientsocket, rep.encode('utf-8'))
		elif message == 'req con'.encode('utf-8'): # 回路オン要求
			rep = 'not cs ' + str(ipip.read_circuit()) + ' ' + str(ipip.write_circuit(True))
			send_message_to_client(clientsocket, rep.encode('utf-8'))
		elif message == 'req cof'.encode('utf-8'): # 回路オフ要求
			rep = 'not cs ' + str(ipip.read_circuit()) + ' ' + str(ipip.write_circuit(False))
			send_message_to_client(clientsocket, rep.encode('utf-8'))
		elif message == 'req cs'.encode('utf-8'): # 回路状態要求
			rep = 'not cs ' + str(ipip.read_circuit())
			send_message_to_client(clientsocket, rep.encode('utf-8'))
		elif message == 'req close'.encode('utf-8'): # 切断要求
			close_flag = True
			rep = 'not close'
			send_message_to_client(clientsocket, rep.encode('utf-8'))
		elif message == 'req finish'.encode('utf-8'): # もう全部死んでしまえ (未実装)
			rep = 'not close'
			send_message_to_client(clientsocket, rep.encode('utf-8'))
			kill_flag = True
		elif message == '':
			break
		else:
			rep = ''

		print('Send: {0} to {1}:{2}'.format(rep, client_address, client_port))

	clientsocket.close()
	print('Bye-Bye: {0}:{1}'.format(client_address, client_port))


# ------------------------------------------------------------------------
# 通信関連の奴ら
# ------------------------------------------------------------------------ 
class Server:
	# コンストラクタ
	def __init__(self):
		self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

	# python の まきつく
	def bind(self):
		host = ''
		port = 50093
		self.serversocket.bind((host, port))

	# listen
	def listen(self):
		self.serversocket.listen(5)

	# 受け入れよう(寛容)
	def accept(self):
		# 相手は誰ゾ
		clientsocket, (client_address, client_port) = self.serversocket.accept()
		print('New client: {0}:{1}'.format(client_address, client_port))

		# いいよ！ 来いよ！
		client_thread = threading.Thread(target=client_handler, args=(clientsocket, client_address, client_port))
		client_thread.daemon = True
		client_thread.start()

# ------------------------------------------------------------------------
# 仕様例的な?
# ------------------------------------------------------------------------ 
#def main():
#	# 宣言ズ
#	global kill_flag
#
#	stenbaai()
#	bind_port()
#	listen()
#	while not kill_flag:
#		accept()
#
#if __name__ == '__main__':
#	main()


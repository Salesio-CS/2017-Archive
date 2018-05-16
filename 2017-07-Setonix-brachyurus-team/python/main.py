#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import threading
import signal
import time

import ipip
import server


# ------------------------------------------------------------------------
# スイッチ関連
# ------------------------------------------------------------------------
# TODO: こ↑こ↓ GPIO動作確認後に要動作確認
def toggle_circuit(value):
	if ipip.read_circuit() != value:
		write_switcher(True)
		write_switcher(False)
		return True
	else:
		return False


# ------------------------------------------------------------------------
# 中身どうかなぁ
# ------------------------------------------------------------------------
def count():
	counting_state = 0
	while True:
		s1 = ipip.read_sensor_one()
		s2 = ipip.read_sensor_two()
		# こ↑こ↓に入ったか出たかの処理
		if counting_state == 0:
			if s1 == True and s2 != True:
				counting_state = 1
			if s1 != True and s2 == True:
				counting_state = -1
		elif counting_state == 1:
			if s1 != True and s2 != True:
				counting_state = 0
			if s1 != True and s2 == True:
				counting_state = 2
		elif counting_state == 2:
			if s1 != True and s2 != True:
				counting_state = 0
				server.counter += 1
			if s1 == True and s2 != True:
				counting_state = 1
		elif counting_state == -1:
			if s1 != True and s2 != True:
				counting_state = 0
			if s1 == True and s2 != True:
				counting_state = -2
		elif counting_state == -2:
			if s1 != True and s2 != True:
				counting_state = 0
				server.counter -= 1
			if s1 != True and s2 == True:
				counting_state = -1
		print('counter: {0}, sensor: {1}, {2}'.format(server.counter, s1, s2))
		time.sleep(0.01) # ここでスリープかける


# こ↑こ↓ counting 処理に使えるかもゾ
"""
def task(arg1, arg2):
	print(time.time())

signal.signal(signal.SIGALRM, task)
signal.setitimer(signal.ITIMER_REAL, 1, 1)
"""


# ------------------------------------------------------------------------
# おめいん
# ------------------------------------------------------------------------ 
# TODO: ラズパイに入れた後にちゃんと動作確認して
def main():
	# ステンバーイ
	god = server.Server()

	# GPIO 準備
	ipip.setup()

	# python の まきつく
	god.bind()

	# 数え上げM@S
	counter_thread = threading.Thread(target=count)
	counter_thread.deamon = True
	counter_thread.start()

	# まだかなまだかなぁ
	god.listen()

	while not server.kill_flag:
		god.accept()
	
	ipip.cleanup()


if __name__ == '__main__':
	main()


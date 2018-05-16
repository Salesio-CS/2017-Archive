#!/usr/bin/env python
# -*- coding: utf-8 -*-

import server

# ------------------------------------------------------------------------
# おめいん
# ------------------------------------------------------------------------ 
def main():
	# ステンバーイ
	god = server.Server()

	# python の まきつく
	god.bind()

	# まだかなまだかなぁ
	god.listen()

	while not server.kill_flag:
		god.accept()

if __name__ == '__main__':
	main()


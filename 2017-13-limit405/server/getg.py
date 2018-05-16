#coding: utf-8
import urllib
import http.server
import os, datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler,BaseHTTPRequestHandler

#server address
#HOST = "192.168.0.125"
#HOST = "127.0.0.1"
HOST = input("HOST?> ")
PORT = 8008
fname = "umbrella.tof"

class GetHandler(BaseHTTPRequestHandler):
	#request ans
	def do_GET(self):
		self.send_response(200) #statuscode
		print("200 ok")
		urls = self.path.split("?")
		print(urls[1])
		query = urllib.parse.parse_qs(urls[1])#クエリ文字列をうまいこと抽出してくれるぞ
		print(query)
		if query["source"] == ["0"]:
			print("傘からの接続")
			fp = open(fname, "w")
			#print("保存用ファイル開いた")
			if query["umbrella"]== ["1"]:
				#さしている
				fp.write("1")
				umbstat='1'
				print("さされている")
			else:
				fp.write("0")
				umbstat='0'
				print("さされていない")
			fp.close()
			print("logファイル書き込み処理開始")
			DATE = datetime.datetime.today()	#現在時刻を取得
			global umbData
			umbData = DATE.strftime("%Y-%m-%d %H:%M:%S, ") + umbstat	#書き込むデータを作成
			dtlg = open('log.txt','a')
			dtlg.write(umbData+'\n')
			print("ファイル書き込み成功   '"+ umbData +"'")
			dtlg.close()
			if sum(1 for line in open("log.txt","r")) >= 359:   #一定数の書き込み(一定時間)ごとにログファイルを分割する
				lgname='[KASA-log]_{0:%y-%m-%d_%H:%M:%S}.csv'.format(DATE)  #リネーム後のファイル名を作成
				print('logファイル分割	出力ファイル名：'+lgname)
				os.rename('log.txt',lgname)
			#print(ファイル書き込み処理ここまで)
		else:
			#viewer
			print("viewerからの接続")
			try:
				fp = open(fname, "r")
			except FileNotFoundError: #viewerが先に来た場合
				print('まだ傘からデータが送られてきていません！')
				print('とりあえずさしていないと判断します')
				fp = open(fname, 'w+')
				fp.write("0")
			is_have_an_umbrella = fp.readline()
			fp.close()
			ornot = "る" if is_have_an_umbrella == "1" else "ない"
			self.send_header("is_have_an_umbrella",is_have_an_umbrella)
			#print("さしてい" + ornot + "と送信")
			umbData = umbData if 'umbData' in globals() else "不明"   #viewerが先に来た場合
			print("傘は差されてい" + ornot + "ようです")
			print("傘からの最新のアクセス日時：" + umbData )
			#'''
			if is_have_an_umbrella == "1":
				self.wfile.write(bytes("傘は差されているようです．\n", "utf-8"))
			else:
				self.wfile.write(bytes("傘は差されていないようです．\n", "utf-8"))
			#'''
		print("通信終了\n")
		self.end_headers()
		return


address = (HOST,PORT)
print(address)
httpd = http.server.HTTPServer(address,GetHandler)
print("sarving http on "+ HOST + ":" + str(PORT))
httpd.serve_forever()

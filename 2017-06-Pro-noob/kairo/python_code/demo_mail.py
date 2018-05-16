# -*- coding: utf-8 -*-
# MCP3208からデジタル値を取得し、ファイルに保存する。
# このコードではMCP3208の8chのうち、0chの値を使用している。


from email.mime.text import MIMEText
from email.Header import Header
from email.Utils import formatdate
import smtplib

import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime

# CP3208からSPI通信で12ビットのデジタル値を取得する。
# 0から7の8チャンネル使用可。
# 引数adcnum：MCP3208の使用するチャンネル
# 引数clockpin：SPI通信クロックピン
# 引数misopin：SPI通信デジタルINピン
# 引数mosipin：SPI通信デジタルOUTピン
# 引数cspin：SPI通信チップセレクトピン
def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if adcnum > 7 or adcnum < 0:
        return -1
    GPIO.output(cspin, GPIO.HIGH)
    GPIO.output(clockpin, GPIO.LOW)
    GPIO.output(cspin, GPIO.LOW)
 
    commandout = adcnum
    commandout |= 0x18  # スタートビット＋シングルエンドビット
    commandout <<= 3    # LSBから8ビット目を送信するようにする
    for i in range(5):
        # LSBから数えて8ビット目から4ビット目までを送信
        if commandout & 0x80:
            GPIO.output(mosipin, GPIO.HIGH)
        else:
            GPIO.output(mosipin, GPIO.LOW)
        commandout <<= 1
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
    adcout = 0
    # 13ビット読む（ヌルビット＋12ビットデータ）
    for i in range(13):
        GPIO.output(clockpin, GPIO.HIGH)
        GPIO.output(clockpin, GPIO.LOW)
        adcout <<= 1
        if i>0 and GPIO.input(misopin)==GPIO.HIGH:
            adcout |= 0x1
    GPIO.output(cspin, GPIO.HIGH)
    return adcout

# 5回計測し、中央値を返す
def getval():
    val_list = []
    for i in range(5):
        val_list.append(readadc(0, SPICLK, SPIMOSI, SPIMISO, SPICS))
        sleep(0.5)
    val_list.sort()
    return val_list[2]
 
GPIO.setmode(GPIO.BCM)
# ピンの名前を定義
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8
# SPI通信用の入出力を定義
GPIO.setup(SPICLK, GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO, GPIO.IN)
GPIO.setup(SPICS, GPIO.OUT)

def send_email(from_addr, to_addr, subject, body, server='smtp.gmail.com', port=587):
    encoding='utf-8'
    msg = MIMEText(body.encode(encoding), 'plain', encoding)
    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    _user = "GMAIL_USER_NAME"
    _pass = "GMAIL_PASSWORD"

    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('team.pronoob123', 'yuki1238')
    smtp.sendmail(from_addr, [to_addr], msg.as_string())
    smtp.close()


# 取得した値をファイルに保存する 
try:
    while True:
        print(datetime.now().strftime('%Y/%m/%d,%H:%M:%S, ') + str(getval()))
	
	d='Soil humidity: ' + str(getval())
	time='Time: ' + str(datetime.now())
	data=[time,d]
	body=str(data)
	send_email('team.pronoob123@gmail.com', 'team2.pronoob123@gmail.com',u'センサーデータ', body)
	
        sleep(60)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()

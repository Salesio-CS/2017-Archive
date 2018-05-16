# -*- coding: utf-8 -*-
# MCP3208からデジタル値を取得し、ファイルに保存する。
# このコードではMCP3208の8chのうち、0chの値を使用している。

import RPi.GPIO as GPIO
from time import sleep
from datetime import datetime
from upload_Values_ug import upload_data

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

# 取得した値をファイルに保存する 
ug = getval()
ughum_origin = str(ug)
print ughum_origin
ughum = ug//40.95
print ughum
#webへpost
upload_data(ughum);

GPIO.cleanup()

#coding: utf-8
import os
import datetime

"""
#////////////////////////////////

import logging

#DATE = str(datetime.datetime.today())
MACAD = 0#useless(VER.PROTO

logging.basicConfig(filename="MACAD.log",level=logging.DEBUG, format='%(asctime)s %(message)s')

logging.debug(MACAD)
logging.info('dead')
logging.warning('TOOOOOOOOOOG')
logging.error('@youjomiruku')
////////////////////////////////
"""

DATE = datetime.datetime.today()
#usrID=



dtlg = open('logdata.txt','a')

dtlg.write(DATE.strftime("%Y-%m-%d %H:%M:%S, ") +'userID(準備中), ' + '状態(準備中), \n')
#usrID：α版では未使用
#状態：傘が差されているか否かを記録 TorF

dtlg.close()
#[状態(準備中)]＝Fになれば(或いはFが一定数連続すれば)ファイルを閉じる
#その後，現在時刻を元に出力データのリネームを行う

os.rename('logdata.txt', '[KASA-ID]_{0:%y-%m-%d_%H:%M}.txt'.format(DATE))



###改善案

#os.rename('logdata.txt', 'I_d.txt') #1st%d=ID 2nd%d=DATE?







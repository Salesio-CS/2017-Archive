#coding:utf-8
import csv
import datetime

def take_pic():
    # ファイルを読み込みモードでオープン
    f = open('data.csv', 'r')
    reader = csv.reader(f) # readerオブジェクトを作成
    header = next(reader)  # 最初の一行をヘッダーとして取得

    print ''.join(header)  # ヘッダーをスペース区切りで表示

    d = datetime.datetime.today()
    h = d.strftime("%H")
    m = d.strftime("%M")
    h = str(10)

    print "hour:" + h
    print "minute:" + m

    nowtime = h + m

    print(nowtime)

    camera = 0
    # 行ごとのリストを処理する
    for row in reader:
        schjuretime1 = row[1] + row[2]
        schjuretime2 = row[3] + row[4]
        if (schjuretime1 < nowtime and schjuretime2 > nowtime):
            camera = 1
    print camera
    f.close()
    return camera

#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Gmailでメール送信

import os.path
import smtplib
from email import Encoders
from email.Utils import formatdate
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
#宛先アドレスの変更
global addr
addr = "s14514@salesio-sp.ac.jp"
#Gmailアカウント
ADDRESS = "gselfver.2@gmail.com"
PASSWARD = "Gself-ver.2"

#SMTPサーバの設定(Gmail用)
SMTP = "smtp.gmail.com"
PORT = 587

#メッセージの作成
def create_message(from_addr, to_addr, subject, body, mime=None, attach_file=None):

    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Date"] = formatdate()
    msg["Subject"] = subject
    body = MIMEText(body)
    msg.attach(body)

    # 添付ファイル
    if mime != None and attach_file != None:

        attachment = MIMEBase(mime['type'],mime['subtype'])
        file = open(attach_file['path'])
        attachment.set_payload(file.read())
        file.close()
        Encoders.encode_base64(attachment)
        msg.attach(attachment)
        attachment.add_header("Content-Disposition","attachment", filename=attach_file['name'])

    return msg

#メールの送信
def send(from_addr, to_addrs, msg):

    smtpobj = smtplib.SMTP(SMTP, PORT)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    smtpobj.login(ADDRESS, PASSWARD)
    smtpobj.sendmail(from_addr, to_addrs, msg.as_string())
    smtpobj.close()

        #宛先アドレス
to_addr = addr

    #件名と本文
subject = "warning"
body = "G発見"

#添付ファイル設定(bmpファイルを添付)
mime={'type':'image', 'subtype':'bmp'}
attach_file={'name':'output.bmp', 'path':'/Users/onoyosuke/Desktop/output.bmp'}

    #メッセージの作成とメール送信の関数の呼び出し
msg = create_message(ADDRESS, to_addr, subject, body)
send(ADDRESS, [to_addr], msg)

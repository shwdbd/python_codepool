#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   send_html_email.py
@Time    :   2020/02/19 21:09:33
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   发送带有HTML格式的电子邮件

- 使用SSL格式连接

'''
import smtplib
from email.mime.text import MIMEText

# 全局参数:
MAIL_SERVER_HOST = 'smtp.163.com'
MAIL_SERVER_PORT = 465
MAIL_USER = 'shwangjj@163.com'
MAIL_PSW = 'wmc20131107'


def send_html_email():
    # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
    sender = 'shwangjj@163.com'
    receiver = ['shwangjj@163.com']
    body = '<h1>测试用HTML格式</h1><p>内容示范</p>'

    # 邮件内容对象
    msg = MIMEText(body, 'html')
    msg['subject'] = 'HTML格式测试邮件 标题'
    msg['from'] = sender
    msg['to'] = ','.join(receiver)

    try:
        s = smtplib.SMTP_SSL(MAIL_SERVER_HOST, MAIL_SERVER_PORT)
        s.login(MAIL_USER, MAIL_PSW)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        # 发送邮件！
        print('发送HTML格式邮件成功')
    except smtplib.SMTPException as err:
        print('Error.sent email fail ' + str(err))


if __name__ == "__main__":
    send_html_email()

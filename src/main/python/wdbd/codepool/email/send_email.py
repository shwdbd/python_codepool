#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   send_email.py
@Time    :   2020/02/19 13:53:47
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   使用163邮箱发送本文格式的电子邮件

注意：
- 发送简单的text格式邮件
- 500的错误是：DNS
考虑到163邮箱的特殊性，建议新申请邮箱

函数：
- send_mail         发送简单邮件
- send_html_mail    发送HTML格式邮件
- send_ssl_mail     发送ssl加密邮件

官方例子: python-3.8.1-docs-html/library/email.examples.html

'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 全局参数:
MAIL_SERVER_HOST = 'smtp.163.com'
MAIL_SERVER_PORT = 25
MAIL_USER = 'shwangjj@163.com'
MAIL_PSW = 'wmc20131107'


def send_email():
    """发送邮件
    """
    sender = 'shwangjj@163.com'
    receivers = ['shwangjj@163.com']  # 接收邮件，可设置多个地址
    subject = '测试邮件标题'
    mail_context = 'Python 邮件内容 ...'

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText(mail_context, 'plain', 'utf-8')
    message['From'] = sender     # 发送者
    message['To'] = ','.join(receivers)
    message['Subject'] = Header(subject, 'utf-8')

    # 第三方 SMTP 服务
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(MAIL_SERVER_HOST, MAIL_SERVER_PORT)
        # smtpObj = smtplib.SMTP_SSL("smtp.163.com", 465)   # SSL加密模式
        smtpObj.login(MAIL_USER, MAIL_PSW)
        smtpObj.sendmail(from_addr=sender, to_addrs=receivers, msg=message.as_string())
        smtpObj.quit()
        print("邮件发送成功")
    except smtplib.SMTPException as err:
        print("Error: 无法发送邮件:" + str(err))


if __name__ == "__main__":
    send_email()

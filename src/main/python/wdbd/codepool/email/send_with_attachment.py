#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   send_with_attachment.py
@Time    :   2020/02/19 21:20:09
@Author  :   Jeffrey Wang
@Version :   1.0
@Contact :   shwangjj@163.com
@Desc    :   发送带有附件的电子邮件

'''
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# 全局参数:
MAIL_SERVER_HOST = 'smtp.163.com'
MAIL_SERVER_PORT = 465
MAIL_USER = 'shwangjj@163.com'
MAIL_PSW = 'wmc20131107'


def send_html_email():
    # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式，现在一般是SSL方式
    sender = 'shwangjj@163.com'
    receiver = ['shwangjj@163.com']
    content = '<h1>测试用HTML 带附件格式</h1><p>正本部分内容示范</p>'

    # 邮件内容对象
    msg = MIMEMultipart()
    # 正文部分:
    textApart = MIMEText(content, 'html')   # HTML格式的邮件正文内容
    msg.attach(textApart)
    # Word附件
    wordFile = r'src\wdbd\codepool\email\测试用附件1.docx'
    wordApart = MIMEApplication(open(wordFile, 'rb').read())
    wordApart.add_header('Content-Disposition', 'attachment', filename='Word附件1.docx')
    msg.attach(wordApart)
    # 图片附件
    imageFile = r'src\wdbd\codepool\email\测试用照片附件.jpg'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])  # jpg
    imageApart.add_header('Content-Disposition', 'attachment', filename='照片1.jpg')
    msg.attach(imageApart)
    # 标题和其他参数
    msg['subject'] = '带附件格式测试邮件 标题'
    msg['from'] = sender
    msg['to'] = ','.join(receiver)

    try:
        s = smtplib.SMTP_SSL(MAIL_SERVER_HOST, MAIL_SERVER_PORT)
        s.login(MAIL_USER, MAIL_PSW)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        # 发送邮件！
        print('发送带附件格式邮件成功')
    except smtplib.SMTPException as err:
        print('Error.sent email fail ' + str(err))


if __name__ == "__main__":
    send_html_email()

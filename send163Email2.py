#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="xxxxxx@163.com"    #用户名
mail_pass="xxxxxx"   #口令


sender = 'xxxxxx@163.com'
receivers = ['xxxxxx@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
for i in range(len(receivers)):
    receivers[i]='<'+receivers[i]+'>'
receiptPerson=','.join(receivers)

message = MIMEText('邮件正文内容', 'plain', 'utf-8')
message['From'] = Header("name1<zhangbo@trs.com.cn>", 'utf-8') #发件人名
message['To'] =  Header("name2"+receiptPerson, 'utf-8')  #收件人名

subject = '邮件主题名称'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "邮件发送成功"
except smtplib.SMTPException,e:
    print "Error: 无法发送邮件"
    print e
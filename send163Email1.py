#! /usr/bin/env python
#coding:utf-8
import smtplib,sys
from email.mime.text import MIMEText
import  time
'''
发送邮件foxmail接受会有乱码现象。
'''

sys.setdefaultencoding('gb18030')
mailto_list=['xxxxxx@qq.com','xxxxxx@qq.com']           #收件人(列表)
mail_host="smtp.163.com"            #使用的邮箱的smtp服务器地址
mail_user="xxxxxx"                           #用户名
mail_pass="xxxxxx"                             #密码
mail_postfix="163.com"                     #邮箱的后缀
def send_mail(to_list,sub,content):
    me="BourkeZhang"+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)                #将收件人列表以‘；’分隔
    usermial=mail_user+"@"+mail_postfix
    try:
        server = smtplib.SMTP()
        server.connect(mail_host,25)                            #连接服务器
        server.login(usermial,mail_pass)               #登录操作
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False
for i in range(10):                             #发送五封，不过会被拦截的。。。
    time.sleep(2)
    if send_mail(mailto_list,"标题名称","这是机器发送的邮件!这是第%d" %(i+1)+'封信件.' ):  #邮件主题和邮件内容
        print "发送成功!"
    else:
        print "发送失败!"
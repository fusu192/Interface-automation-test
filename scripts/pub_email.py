#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.mxhichina.com"  # 设置服务器
mail_user = "xiaoming@xiaohong.com"  # 用户名
mail_pass = "xiaoming-de-mima"  # 口令

sender = 'from@runoob.com'
receivers = ['forlearnsth@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message = MIMEText('<html><body><h1>Hello</h1>' +
                   '<p>查看 <a href="http://www.python.org">测试报告</a>...</p>' +
                   '</body></html>', 'html', 'utf-8')
# message['From'] = Header("Automation", 'utf-8')
# message['To'] =  Header("all", 'utf-8')


message['From'] = Header("Automation")
message['To'] = Header("all")
subject = 'Api automation test report'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(mail_user, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)
    print("Error: 无法发送邮件")

# 参考：
# https://www.runoob.com/python3/python3-smtp.html
# https://www.runoob.com/python/python-email.html

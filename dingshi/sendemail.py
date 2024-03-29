#!/usr/bin/python
# -*- coding: UTF-8 -*-


# ModuleNotFoundError: No module named 'email.mime'; 'email' is not a package
# 第一：未导入包   第二：包名和文件名冲突
# 该功能不能与导入的模块名称相同

import sys
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "mickey_qiangzi@163.com"  # 用户名
mail_pass = "yanqiang94"  # 口令

sender = 'mickey_qiangzi@163.com'
receivers = ['mickey_qiangzi@163.com', 'www.1152508526@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# receivers = 'm1310@foxmail.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱


message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("菜鸟教程", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
message['From'] = sender

print("receivers长度：",len(receivers))
if len(receivers) > 1:
    message['To'] = ';'.join(receivers)
else:
    message['To'] = receivers


subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    # 发送邮件
    smtpObj.sendmail(sender, receivers, message.as_string())
    print()
    smtpObj.quit()
    print("邮件发送成功")

# except OSError as err:
#     print("OS error: {0}".format(err))
except smtplib.SMTPException:
    print("Unexpected error:", sys.exc_info()[0])
    print("Error: 无法发送邮件")
    # 当程序出现错误，python会自动引发异常，也可以通过raise显示地引发异常。一旦执行了raise语句，raise后面的语句将不能执行。
    raise

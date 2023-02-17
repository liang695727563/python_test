#coding=utf-8
# 或者你也可以在消息体中指定 Content-type 为 text/html,如下实例:

import smtplib

message = """ From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

This is an e-mail message to be sent in HTML format

<b>This is HTML message.</b>
<h1>THis is headline.</h1>
"""

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
    print "Sucessfully sent email"
except SMTPException:
    print "Error: unable to send email"

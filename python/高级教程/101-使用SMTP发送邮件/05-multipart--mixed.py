#coding=utf-8
# 以下实例指定了 Content-type header 为 multipart/mixed，并发送 /tmp/test.txt 文本文件：

import smtplib
import base64
filename = '/tmp/test.txt'

# 读取文件内容并使用 base64
fo = open(fileame, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'webmaster@tutorialpoint.com'
reciever = 'amrood.admin@gmail.com'

marker = 'AUNIQUEMARKER'

body = """
This is a test email to send an attachement.
"""

# 定义头部信息
part1 = """From: From Person <me@fromdomain.net>
To: To person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multpart/mixed; boundary=%s
--%S
""" % (marker,marker)

# 定义消息动作
part2 = """Content-Type: text/plain
Cotent-Transfer-Encoding:Bbit

%s
--%s
""" % (body, marker)

# 定义附件部分
part3 = """Content-Type: multipart/mixed; name=\"%s\"
Content-Transfer-Encoding:base64
Content-Disposition: attachment; filename=%s

%s
--%s--
""" %(filename, filename, encodedcontent, marker)
message = part1 + part2 + part3

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, reciever, message)
    print "Successfully sent email"
except Exception:
    print "Error: unable to send email"






















































































































































































































































































































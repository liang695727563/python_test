#coding=utf-8
# ����ʵ��ָ���� Content-type header Ϊ multipart/mixed�������� /tmp/test.txt �ı��ļ���

import smtplib
import base64
filename = '/tmp/test.txt'

# ��ȡ�ļ����ݲ�ʹ�� base64
fo = open(fileame, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64

sender = 'webmaster@tutorialpoint.com'
reciever = 'amrood.admin@gmail.com'

marker = 'AUNIQUEMARKER'

body = """
This is a test email to send an attachement.
"""

# ����ͷ����Ϣ
part1 = """From: From Person <me@fromdomain.net>
To: To person <amrood.admin@gmail.com>
Subject: Sending Attachement
MIME-Version: 1.0
Content-Type: multpart/mixed; boundary=%s
--%S
""" % (marker,marker)

# ������Ϣ����
part2 = """Content-Type: text/plain
Cotent-Transfer-Encoding:Bbit

%s
--%s
""" % (body, marker)

# ���帽������
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






















































































































































































































































































































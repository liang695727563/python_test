#coding=utf-8
# ���ʹ��������ʼ�������Ҫ���� MIMEMultipart() ʵ����Ȼ���츽��������ж�������������ι��죬������� smtplib.smtp ���͡�

from email.mime.text import MIMEText
from email.mime.multipart imort MIMEMultipart
import smtplib

# ����һ����������ʵ��
msg = MIMEMultipart()

# ���츽��1
att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64','gb2312')
att1["Content-type"] = 'application/octet-stream'
attq["Content-Disposition"] = 'attachment; filename="123.doc"'  # �����filename��������д��дʲô���֣��ʼ�����ʾʲô����
msg.attach(att1)

# ��������2
att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

# ���ʼ�ͷ
msg['to'] = 'YYY@YYY.com'
msg['from'] = 'XXX@XXX.com'
msg['subject'] = 'hello world'
# �����ʼ�
try:
    server = smtplib.SMTP()
    server.connect('smtp.XXX.com')
    server.login('XXX','XXXX') # XXXΪ�û����� XXXXΪ����
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()
    print '���ͳɹ�'
except Exception, e:
    print str(e)
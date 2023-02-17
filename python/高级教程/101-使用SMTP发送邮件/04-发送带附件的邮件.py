#coding=utf-8
# 发送带附件的邮件，首先要创建 MIMEMultipart() 实例，然后构造附件，如果有多个附件，可依次构造，最后利用 smtplib.smtp 发送。

from email.mime.text import MIMEText
from email.mime.multipart imort MIMEMultipart
import smtplib

# 创建一个带附件的实例
msg = MIMEMultipart()

# 构造附件1
att1 = MIMEText(open('d:\\123.rar', 'rb').read(), 'base64','gb2312')
att1["Content-type"] = 'application/octet-stream'
attq["Content-Disposition"] = 'attachment; filename="123.doc"'  # 这里的filename可以任意写。写什么名字，邮件中显示什么名字
msg.attach(att1)

# 构建附件2
att2 = MIMEText(open('d:\\123.txt', 'rb').read(), 'base64', 'gb2312')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="123.txt"'
msg.attach(att2)

# 加邮件头
msg['to'] = 'YYY@YYY.com'
msg['from'] = 'XXX@XXX.com'
msg['subject'] = 'hello world'
# 发送邮件
try:
    server = smtplib.SMTP()
    server.connect('smtp.XXX.com')
    server.login('XXX','XXXX') # XXX为用户名， XXXX为密码
    server.sendmail(msg['from'], msg['to'], msg.as_string())
    server.quit()
    print '发送成功'
except Exception, e:
    print str(e)
#coding=utf-8
# Python 发送 HTML 格式的邮件与发送纯文本消息的邮件不同之处就是将 MIMEText 中 _subtype 设置为 html。

import smtplib
from email.mime.text import MIMEText
mailto_list = ["YYY@YYY.com"]
mail_host = "smtp.XXX.com"  #设置服务器
mail_user = "XXX"   # 用户名
mail_pass = "XXXX"  # 口令
mail_postfix = "XXX.com"    # 发送前的后缀

def send_mail(to_list.sub,content):     # to_list: 收件人, sub: 主题, content: 新邮件内容
    me = "hello"+"<"+mail_user+"@"+mail_posfix+">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='gb2312')   #创建一个实例，这里这个是为html格式邮件
    msg['Subject'] = sub    # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)    # 链接smtp服务器
        s.login(mail_user,mail_pass)    # 登录服务器
        s.sendmail(me, to_list, msg.as_string())    #发送邮件
        s.clone()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list, "hello","<a href='http://www.W3cschool.cn/'>W3Cschool</a>"):
        print "发送成功"
    else：
        print "发送失败"
#coding=utf-8
# Python ���� HTML ��ʽ���ʼ��뷢�ʹ��ı���Ϣ���ʼ���֮ͬ�����ǽ� MIMEText �� _subtype ����Ϊ html��

import smtplib
from email.mime.text import MIMEText
mailto_list = ["YYY@YYY.com"]
mail_host = "smtp.XXX.com"  #���÷�����
mail_user = "XXX"   # �û���
mail_pass = "XXXX"  # ����
mail_postfix = "XXX.com"    # ����ǰ�ĺ�׺

def send_mail(to_list.sub,content):     # to_list: �ռ���, sub: ����, content: ���ʼ�����
    me = "hello"+"<"+mail_user+"@"+mail_posfix+">"  # �����hello�����������ã��յ��ź󣬽�����������ʾ
    msg = MIMEText(content,_subtype='html',_charset='gb2312')   #����һ��ʵ�������������Ϊhtml��ʽ�ʼ�
    msg['Subject'] = sub    # ��������
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)    # ����smtp������
        s.login(mail_user,mail_pass)    # ��¼������
        s.sendmail(me, to_list, msg.as_string())    #�����ʼ�
        s.clone()
        return True
    except Exception, e:
        print str(e)
        return False
if __name__ == '__main__':
    if send_mail(mailto_list, "hello","<a href='http://www.W3cschool.cn/'>W3Cschool</a>"):
        print "���ͳɹ�"
    else��
        print "����ʧ��"
#coding=utf-8

import socket       # ���� socket ģ��

s = socket.socket()         # ���� socket ����
host = socket.gethostname() # ��ȡ����������
port = 12345                # ���ö˿�
s.bind((host, port))        # �󶨶˿�

s.listen(5)                 # �ȴ��ͻ�������
while True:
    c, addr = s.accept()    # �����ͻ������ӡ�
    print '���ӵ�ַ��', addr
    c.send('��ӭ����W3Cschool�̳̣�')
    c.close()               # �ر�����
#coding=utf-8

import socket           # ���� socket ģ��

s = socket.socket()     # ���� socket ����
host = socket.gethostname() # ��ȡ����������
port = 12345                # ���ö˿ں�

s.connect((host, port))
print s.recv(1024)
s.close()
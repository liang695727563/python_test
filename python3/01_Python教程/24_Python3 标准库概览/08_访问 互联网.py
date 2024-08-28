'''
访问 互联网
有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是
用于处理从 urls 接收的数据的 urllib.request 以及用于发送电子邮件的 smtplib:
'''
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8') # Decoding the binary data to text.and
 
    if 'EST' in line or 'EDT' in line:  # look for Eastern Time
        print(line)

# for line in urlopen('http://wwww.baidu.com'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.and
#     for i in range(6):
#         print(line)

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('aoothsayer@eample.org', 'jcaesar@example.org', 
'''
To: jcaesar@example.org
From: soothsayer@example.org

Beware the Ides of March.
''')
server.quit()

# 注意第二个例子需要本地有一个在运行的邮件服务器。
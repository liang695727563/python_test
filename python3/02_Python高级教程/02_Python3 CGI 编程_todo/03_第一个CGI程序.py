'''
第一个CGI程序
我们使用 Python 创建第一个 CGI 程序，文件名为 hello.py，文件位于 /var/www/cgi-bin目录中，内容如下：
'''
print("Content-type:text/html") # 指定返回的类型，没有这行代码会报错

print()              # 空行，告诉服务器结束头部

# 以下是要返回的HTML正文
print ('<html>')

print ('<head>')

print ('<title>Hello Word - 我的第一个 CGI 程序！</title>')

print ('</head>')

print ('<body>')

print ('<h2>Hello Word! 我的第一CGI程序</h2>')

print ('</body>')

print ('</html>')

'''
文件保存后修改 hello.py，修改文件权限为 755（linux和macos需要在webpy文件夹下使用下面的命令来修改文件读写权限，在Windows环境下需要修改文件的读写权限）：

这个的 hello.py 脚本是一个简单的 Python 脚本，脚本第一行的输出内容"Content-type:text/html"发送到浏览器并告知浏览器显示的内容类型为"text/html"。

用 print 输出一个空行用于告诉服务器结束头部信息。
'''

'''
注：如果此处出现乱码，可以在打印html的时候打印​​,在下文部分代码中有所体现（注意，这里不使用UTF-8的原因是小编在这里使用utf-8出现乱码，这是因为小编的系统是Windows系统，系统默认字符集是GBK，所以会出现乱码）。

另外：请注意第一行代码，在linux中需要在py文件中正确指定python解释器的路径才能运行 。在Windows中使用Python CGI文件也需要正确指定python解释器的路径才能运行
'''

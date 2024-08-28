'''
Web 服务器支持及配置
在你进行 CGI 编程前，确保您的 Web 服务器支持 CGI 及已经配置了 CGI 的处理程序。

Apache 支持 CGI 配置（这里使用PHPstudy集成的Apache）：

打开Apache的配置文件​httpd-conf​，在文件中找到如下内容：

首先找到ScriptAlias

修改为项目地址​ ScriptAlias /cgi-bin/ "F:/phpstudy/phpstudy_pro/WWW/webpy"​ （之前的项目都放在​F:/phpstudy/phpstudy_pro/WWW/​下,这个文件夹是PHPstudy的apache默认项目文件夹，将路径改为这样可以方便localhost访问）。

然后找到Directory，将其修改为

<p><Directory "<span style="background-color: initial; font-size: inherit;">F:/phpstudy/phpstudy_pro/WWW/webpy</span><span style="background-color: initial; font-size: inherit;">"></span></p><p>    AllowOverride None
</p><p>    Options +ExecCGI
</p><p>    Order allow,deny
</p><p>    Allow from all
</p><p> </Directory></p>

注意：这里的路径和上面设置的路径是一样的。

接着找到AddHandler
添加​.py​。使apache识别.py文件为cgi程序（图中已添加）。

接下来我们就可以在webpy文件夹下写pythonCGI程序了。
'''
'''
操作系统接口
os 模块提供了不少与操作系统相关联的函数。
'''
import os
print(os.getcwd()) # 返回当前的工作目录

# os.chdir('/server/accesslogs') # 修改当前的工作目录
# os.system('mkdir today')    # 执行系统命令 mkdir

'''
建议使用 "import os" 风格而非 "from os import *"。这样可以保证随操作系统不同而有所变化的 os.open() 不会覆盖内置函数 open()。
在使用 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用
'''
import os
print(dir(os))
print('-' * 30)
print(help(os))

'''
针对日常的文件和目录管理任务，:mod:shutil 模块提供了一个易于使用的高级接口：
'''
import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')


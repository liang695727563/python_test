# coding=utf-8
import os;

# 重命名文件test1.txt到test2.txt。
# rename之前要先用chdir()函数进入到目标文件所在的路径，告诉python编译器要重命名的文件在哪儿，然后才可以修改；
os.chdir(os.path.dirname("E:/python/11-模块/test1.txt"))
# os.rename("test1.txt", "test2.txt");

# 删除一个已经存在的文件test2.txt
os.remove("test2.txt");
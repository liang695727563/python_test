# coding=utf-8
import os;

# �������ļ�test1.txt��test2.txt��
# rename֮ǰҪ����chdir()�������뵽Ŀ���ļ����ڵ�·��������python������Ҫ���������ļ����Ķ���Ȼ��ſ����޸ģ�
os.chdir(os.path.dirname("E:/python/11-ģ��/test1.txt"))
# os.rename("test1.txt", "test2.txt");

# ɾ��һ���Ѿ����ڵ��ļ�test2.txt
os.remove("test2.txt");
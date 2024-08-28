# 使用pickle模块从文件中重构 python 对象

import pprint, pickle

pk1_file = open('19_Python3 输入和输出/temp/dat.pk1', 'rb')

data1 = pickle.load(pk1_file)
pprint.pprint(data1)

data2 = pickle.load(pk1_file)
pprint.pprint(data2)

pk1_file.close()
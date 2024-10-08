'''
Python 中，支持两种类型相同的序列使用“+”运算符做相加操作，它会将两个序列进行连接，但不会去除重复的元素。
这里所说的“类型相同”，指的是“+”运算符的两侧序列要么都是列表类型，要么都是元组类型，要么都是字符串。
'''

protocol = "https://"
url = "www.w3cschool.cn"
print(protocol+url)         #用“+”运算符连接 2 个（甚至多个）字符串
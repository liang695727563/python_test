'''
pickle 模块
Python 的 pickle 模块实现了基本的数据序列和反序列化。
通过 pickle 模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久保存。
通过 pickle 模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
基本接口：
pickle.dump(obj, file, [,protocol])
有了 pickle 这个对象，就能对 file 以读取的形式打开：
x = pickle.load(file)
注解： 从 file 中读取一个字符串，并将它重构为原来的 Python 对象。
file: 类文件对象，有read() 和 readline() 接口。

'''

'''
抛出异常
Python 使用 raise 语句抛出一个指定的异常。
'''
raise NameError('HiThere')

'''
raise 唯一的一个参数指定了要被抛出的异常。它必须是一个异常的实例或者是异常的类（也就是 Exception 的子类）。
如果你只想知道这是否抛出了一个异常，并不想去处理它，那么一个简单的 raise 语句就可以再次把它抛出。
'''
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise

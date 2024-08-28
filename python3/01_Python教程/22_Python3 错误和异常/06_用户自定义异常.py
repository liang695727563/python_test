'''
用户自定义异常
你可以通过创建一个新的 exception 类来拥有自己的异常。异常应该继承自 Exception 类，或者直接继承，或者间接继承。
'''
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

try:
    raise MyError(2*2)
except MyError as e:
    print('My exception occurred, value:', e.value)

'''
在这个例子中，类 Exception 默认的 __init__() 被覆盖。
异常的类可以像其他的类一样做任何事情，但是通常都会比较简单，只提供一些错误相关的属性，
并且允许处理异常的代码方便的获取这些信息。
当创建一个模块有可能抛出多种不同的异常时，一种通常的做法时为这个包建立一个基础异常类，
然后基于这个基础类为不同的错误情况创建不同的子类：

'''
class Error(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(Error):
    """Exception raised for errors in the input.
    
    Attributes:
        expression -- input expression in whick the error occurrd
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(Error):
    """Raised when an operation attempts a state transition that's not allowd.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message

'''
大多数的异常的名字都以 "Error" 结尾，就跟标准的异常命名一样。
'''

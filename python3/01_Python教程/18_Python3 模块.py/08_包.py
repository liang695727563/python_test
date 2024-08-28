'''
包
包是一种管理 Python 模块命令空间的形式，采用“点模块名称”。
比如一个模块的名称是 A.B, 那么他表示一个包 A 中的子模块 B 。
就好像使用模块的时候，你不用担心不同模块之间的全局变量相互影响一样，采用点模块名称这种形式也不用担心不同库之间的模块重名的情况。
这样不同的作者都可以提供 NumPy 模块， 或者是 Python 图形库。
不妨将设你想设计一套统一处理声音文件和数据的模块（或者称之为一个“包”）。
现存很多不同的音频文件格式（基本上都是通过后缀名区分的，例如：.wav,:file:.aiff,:file:.au,）,
所以你需要有一组不断增加的模块，用来在不同的格式之间转换。
并且针对这些音频数据，还有很多不同的操作（比如混音，添加回声，增加均衡器功能，创建人造立体声效果），所以你还需要一组怎么也写不完的模块来处理这些操作。
这里给出了一种可能的包结构（在分层的文件系统中）：

sound/                          顶层包
      __init__.py               初始化 sound 包
      formats/                  文件格式转换子包
              __init__.py
              wavread.py
              wavwrite.py
              aiffread.py
              aiffwrite.py
              auread.py
              auwrite.py
              ...
      effects/                  声音效果子包
              __init__.py
              echo.py
              surround.py
              reverse.py
              ...
      filters/                  filters 子包
              __init__.py
              equalizer.py
              vocoder.py
              karaoke.py
              ...


在导入一个包的时候，Python 会根据 sys.path 中的目录来寻找这个包中包含的子目录。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包， 主要是为了避免一些滥俗的名字（比如叫做 string）不小心的影响搜索路径中的有效模块。
最简单的情况放一个空的：file:__init__.py 就可以了。当然这个文件中也可以包含一些初始化代码或者为（将在后面介绍的）__all__ 变量赋值。
用户可以每次只导入一个包里面的特定模块，比如：

'''
import sound.effects.echo
# 这将会导入子模块：mod: sound.effects.echo。 他必须使用全名去访问：
sound.effects.echo.echofilter(imput, output, delay=0.7, atten=4)

# 还有一种导入子模块的方法是：
from sound.effects import echo
# 这样会导入子模块 echo，并且他不需要哪些冗长的前缀，所以他可以这样使用：
echo.echofilter(input, output, delay=0.7, atten=4)

# 还有一种变化就是直接导入一个函数或者变量：
from sound.effects.echo import echofilter

# 同样的，这种方式会导入子模块 echo，并且可以直接使用他的 echofilter() 函数：
echofilter(input, output, delay=0.7, atten=4)
'''
注意当使用 from package import item 这种形式的时候， 对应的 item 既可以是包里面的子模块 （子包），
或者包里面定义的其他名称，比如函数，类或者变量。
import 语法会首先把 item 当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，
恭喜，一个：exc:ImportError 异常被抛出了。
反之，如果使用形如 import item.subitem.subsubitem 这种导入形式，除了最后一项，都必须是包，
而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字。
'''
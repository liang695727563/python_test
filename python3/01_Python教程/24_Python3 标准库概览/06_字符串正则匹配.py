'''
字符串正则匹配
re 模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案：
'''

import re
print(re.findall(r'\bf[a-z]', 'which foot or hand fell fastest'))
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))

print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
'''
如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试：
'''
print('tea for too'.replace('too', 'two'))
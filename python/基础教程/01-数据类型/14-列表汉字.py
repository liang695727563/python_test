# encoding=utf-8
import json
#一下代码是用来保证在线环境中运行不报错的。
# import sys # 导入sys库
# reload(sys)
# sys.setdefaultencoding('utf-8') # 设置默认的编码字符集为uft-8，避免第14行的print在 在线情况下报错
# 本地环境可以不需要这部分代码

list_words = ['你', '我', '他']
print( list_words)    # 无法正常显示汉字cl
print( str(list_words).decode('string_escape'))  # 正常显示汉字

# 注意区分‘utf-8’的大小写问题
list_words_result = json.dumps( list_words, encoding='utf-8', ensure_ascii=False )
print(list_words_result)
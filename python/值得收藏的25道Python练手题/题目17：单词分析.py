# -*- coding: UTF-8 -*-

# 输入一段字符串后，得到当前字符串出现最多的字母和它的次数

def analyse_words(words):
    word_dict = {}
    for i in words:
        if i in word_dict:
            word_dict[i] += 1
        else:
            word_dict[i] = 1
    max_key = max(word_dict, key = word_dict.get)
    print max_key
    print word_dict[max_key]

analyse_words('helloworld')
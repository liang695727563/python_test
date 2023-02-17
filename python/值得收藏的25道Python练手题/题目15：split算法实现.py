#coding=utf-8
# split 是 python 字符串内置的一个非常有用的方法

# 它可以将一个字符串通过分隔符切成我们想要的列表

# 比如现在我们有个字符串 life-is-short-you-need-python 每一个单词之间使用分隔符“-”进行分割

# 当我们去调用字符串 split 的方法之后传入我们的分隔符“-”，那我们就会得到一个列表列表里面每个元素其实就是通过分隔符切出来的子字符串

# 那这个算法该怎么样去实现呢？python 内置的 split 方法是通过 C 语言实现的，我们今天去写一个函数，去实现和 split 相同的功能

# 我们先来讲下算法该怎么样去实现，这个算法需要我们对字符串进行迭代，我们先去定义一个初始化的指针，因为我们切片的时候需要从哪一个开始的位置进行切

# 所以我们先要初始化一个指针我们可以定义一个指针变量，默认值为 0，紧接着我们开始对字符串进行迭代

# 当碰到第一个分隔符的时候，我们是不是会获取到当前分隔符的索引，那这个时候，我们就把初始的指针开始到分隔符结束对字符串进行切片

# 因为我们字符串是遵守左闭右开的，你的结束索引写的是分隔符的索引，所以只会切到 life，我们并把它添加到列表里面

# 紧接着添加完之后呢，我们需要把初始化的指针修改一下位置，修改到哪个地方呢？修改到我们第一次碰到的分隔符的下一个位置也就是 i，紧接着继续进行迭代

# 迭代之后发现第二个分隔符，是不是还有一个分隔符的索引，这个时候我们继续向字符串进行切片，切片的开始位置是你的 i 这个位置的指针，结束的位置是第二个 - 的指针，那遵循左闭右开，所以我们 is 这个单词，也可以添加进列表

# 就这样一直到最后呢，当我们去迭代到最后一个字符 n 的时候，发现后面是没有横杆分隔符了，这个时候我们需要进行处理一下，需要进行去判断一下，如果我们迭代到的字符是最后一个字符，那么我们进行切片的时候，就应该从哪个地方切呢？

# 从 p 开始 ，如果切到 n，我们只能取到 pytho，少切一个 n，所以到 n + 1 的位置，好，知道这个流程我们就用代码去实现这个算法

def split_s(string, sep="", num =0):
    split_words = []
    last_index = 0
    count = 0
    for index, char in enumerate(string):
        if count == num and num >0:
            split_words.append(string[last_index:len(string)])
            break
        if char == sep:
            split_words.append(string[last_index:index])
            last_index = index +1
            count += 1
        elif index +1 == len(string):
            split_words.append(string[last_index:index + 1])
    return split_words

print split_s('life-is-short-you-need-python','-')

print split_s("life-is-short-you-need-python",'-',2)

print split_s("happy new year!", " ")
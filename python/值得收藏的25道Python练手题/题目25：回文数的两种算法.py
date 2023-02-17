#coding=utf-8
# 回文数是指正序(从左向右)和倒序(从右向左)都是一样的整数。例如，1221 是回文，而 1222 不是。

# 解法一：通过逆转字符串进行比对
def is_palindrome(x):
    if x < 0 or x > 0 and x % 10 == 0:
        return False
    str_x = str(x)
    return str_x == str_x[::-1]

print is_palindrome(121)
print is_palindrome(120)

print '*' *30
# 解法二：反转一半数字和前半部分的数字进行比较
# 流程

# 对于整数 x，将后半部分反转，保存到变量 reverted
# 每次循环 x%10 拿到末尾数字
# 然后 x/10 去除末尾的数字
# 循环结束条件 x<=reverted
# 数字长度（奇数） 12321
# 数字长度（偶数） 1221

def is_palindrome2(x):
    if x < 0 or x > 0 and x % 10 == 0:
        return False
    reverted = 0
    while x > reverted:
        # 我们看下 1221
        # 第一次循环我们需要把末尾数字1取出来 第二次取末尾数字2 我们需要把21变成12
        reverted = reverted * 10 + x % 10
        # 把x的末尾数字删除掉
        x //= 10
    return x == reverted or x == reverted // 10

print is_palindrome2(1221)
print is_palindrome2(1223)
print is_palindrome2(123321)
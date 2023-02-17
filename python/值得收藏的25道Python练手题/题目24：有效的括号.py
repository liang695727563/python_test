#coding=utf-8
# 给定一个只包括'('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

# 有效字符串需满足：

# 左括号必须用相同类型的右括号闭合

# 左括号必须以正确的顺序闭合

# 空字符串可被认为是有效字符串
# 示例 1：    输入："()"  输出：True

# 示例 2：    输入："()[]{}"  输出：True

# 示例 3：    输入："(]"  输出：False

# 示例 4：    输入："([)]"    输出：False

# 解法一：字符串替换法 在字符串中找成对的()、[]、{}，找到后替换成空 使用 while 循环，不停判断是否存在成对的小括号中括号大括号，如果存在就使用 replace 替换成空 直到无法再替换的时候，再判断下当前的字符串是否为空，如果为空说明字符串是有效的，如果不为空说明字符串是无效的

def valid_str(string):
    if len(string) % 2 == 1:
        return False
    while '()' in string or '[]' in string  or '{}' in string:
        string = string.replace('()','')
        string = string.replace('[]','')
        string = string.replace('{}','')
    return string == ''

print valid_str('()')
print valid_str('()[]{}')
print valid_str('()[]{[()]}')
print valid_str('()[]{[(})]}')




# 解法二：利用栈的后进先出原则 先去定义一个空栈，对当前栈进行循环遍历，遇到左括号我们就把当前的左括号添加到栈里面，遇到右括号，我们就和栈顶元素进行比对 看它们是不是成对的括号，如果是，就把当前的元素出栈，直到字符串遍历结束之后，我们再来看下字符串是不是空的，如果是空的说明字符串是有效的，如果不为空说明字符串是无效的
print '*'*30
def valid_str2(string):
    if len(string) % 2 ==1:
        return False
    stack = []
    char_dict = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in string:
        if char in char_dict:
            # 右括号
            if not stack or char_dict[char] != stack.pop():
                return False
        else:
            # 左括号
            stack.append(char)
    return not stack

print valid_str2('(){}[({[]})]')
print valid_str2('(){}[({[)})]')
print valid_str2('')

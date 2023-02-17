#coding=utf-8
# ����һ��ֻ����'('��')'��'{'��'}'��'['��']' ���ַ������ж��ַ����Ƿ���Ч��

# ��Ч�ַ��������㣺

# �����ű�������ͬ���͵������űպ�

# �����ű�������ȷ��˳��պ�

# ���ַ����ɱ���Ϊ����Ч�ַ���
# ʾ�� 1��    ���룺"()"  �����True

# ʾ�� 2��    ���룺"()[]{}"  �����True

# ʾ�� 3��    ���룺"(]"  �����False

# ʾ�� 4��    ���룺"([)]"    �����False

# �ⷨһ���ַ����滻�� ���ַ������ҳɶԵ�()��[]��{}���ҵ����滻�ɿ� ʹ�� while ѭ������ͣ�ж��Ƿ���ڳɶԵ�С���������Ŵ����ţ�������ھ�ʹ�� replace �滻�ɿ� ֱ���޷����滻��ʱ�����ж��µ�ǰ���ַ����Ƿ�Ϊ�գ����Ϊ��˵���ַ�������Ч�ģ������Ϊ��˵���ַ�������Ч��

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




# �ⷨ��������ջ�ĺ���ȳ�ԭ�� ��ȥ����һ����ջ���Ե�ǰջ����ѭ���������������������ǾͰѵ�ǰ����������ӵ�ջ���棬���������ţ����Ǿͺ�ջ��Ԫ�ؽ��бȶ� �������ǲ��ǳɶԵ����ţ�����ǣ��Ͱѵ�ǰ��Ԫ�س�ջ��ֱ���ַ�����������֮���������������ַ����ǲ��ǿյģ�����ǿյ�˵���ַ�������Ч�ģ������Ϊ��˵���ַ�������Ч��
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
            # ������
            if not stack or char_dict[char] != stack.pop():
                return False
        else:
            # ������
            stack.append(char)
    return not stack

print valid_str2('(){}[({[]})]')
print valid_str2('(){}[({[)})]')
print valid_str2('')

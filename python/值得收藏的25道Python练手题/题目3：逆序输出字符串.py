#coding=utf-8
# д�� 1����Ƭ��ʽ
str = raw_input("�������ַ�����")
# str = input("�������ַ�����")  # Ϊʲô������ַ�����ɱ����ˣ�

print str
print (str[::-1])

# д�� 2��ѭ��ת��
str = raw_input("�������ַ���:")
print str
list = []
for x in range(len(str) -1, -1, -1):
    list.append(str[x])
print ''.join(list)

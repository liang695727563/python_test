#coding=utf-8
print "���"

key1= "Alice"
value1 = '2341'
key2 = 'Beth'
value2 = '9102'
d = {key1 : value1, key2 : value2}
print d;

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1 = {'abc': 456}
dict2 = {'abc': 123, 98.6: 37}
print dict,dict2,dict2

# �����ֵ����ֵ
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
print "dict['Name']: ",dict['Name'];
print "dict['age']:", dict['Age'];
print "dict['Class']:", dict['Class'];

#�޸��ֵ�
dict['Age'] = 8;    # update existing entry
dict['School'] = "DPS School"; # Add new entry

print "dict['Age']:", dict['Age'];
print "dict['Sclool'];", dict['School'];
print 'dict:', dict;

#ɾ���ֵ�Ԫ��
del dict['Name'];   # ɾ������'name'����Ŀ
print 'dict:', dict;
dict.clear();       # ��մʵ�������Ŀ
print 'dict:', dict;
del dict;           # ɾ���ʵ�
print 'dict', dict;
# print "dict['School']:", dict['School']

#�ֵ��������
# �ֵ�ֵ����û�����Ƶ�ȡ�κ� Python ���󣬼ȿ����Ǳ�׼�Ķ���Ҳ�������û�����ģ��������С�
# ������Ҫ�ĵ���Ҫ��ס��
# 1) ������ͬһ�����������Ρ�����ʱ���ͬһ��������ֵ���Σ�ֻ�ᱣ���һ�θ�ֵ
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']:", dict["Name"];
# 2) �����벻�ɱ䣬���Կ����������ַ�����Ԫ��䵱���������б�Ͳ���
dict = {('Name'): 'Zara', 'Age': 7}
print "dict1['Name']:", dict['Name']
# dict = {['Name']: 'Zara', 'Age': 7} # �б�������Ϊ��
# print "dict['Name']:", dict['Name']


# ʵ����

# ʹ��Python��д�ֵ����
#   �û���ӵ��ʺͶ���
#   ������Щ����
#   ����鲻���������û�֪��
#   ѭ��

# �ֵ䴴�� while���� �ֵ����  �ֵ����
dictionary = {}
flag = 'a'
page = 'a'
while flag == 'a' or 'c':
    flag = raw_input("��ӻ���ҵ��� ?(a/c)")
    if flag == 'a':                             # ����
        word = raw_input('���뵥��(key):')
        defintion = raw_input("���붨��ֵ(value):")
        dictionary[str(word)] = str(defintion)  # ����ֵ�
        print "��ӳɹ���"
        page = raw_input("���Ƿ�Ҫ�����ֵ�?(a/0)") # read
        if page == 'a':
            print dictionary
        else:
            continue
    elif flag == 'c':
        off = 'a'
        check_word = raw_input("Ҫ���ҵĵ��ʣ�")    # ���
        for key in sorted(dictionary.keys()):
            if str(check_word) == key:
                print "�õ��ʴ���!", key, dictionary[key]
                break
            else:
                off = 'b'
        if off == 'b':
            print "��Ǹ����ֵ�����ڣ�"
    else:                               # ֹͣ
        print "error type"
        break


print "Good bye"
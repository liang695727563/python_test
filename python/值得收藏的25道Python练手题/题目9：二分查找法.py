#coding=utf-8

# ���ַ��������

# ��������������С�
# ����������С��Ҫ��
# ������̫С���ʺ϶��ֲ��ң���ֱ�ӱ������Ч�����������ԡ�
# ������̫��Ҳ���ʺ��ö��ֲ��ң���Ϊ������Ҫ�����Ĵ洢�ռ䣬��������̫�������Ҳ����洢��˴��ģ���ݵ������ڴ�ռ�

# �㷨˼·��

# ������һ�������б�[5,7,11,22,27,33,39,52,58]

# �������� 11 �Ƿ��ڴ��б��У��������������ֵΪ���٣�

# ��������ȡ�����б���м�λ�� 27 �� 11 ���бȽ� ���Ƿ��� 11 ��С�� 27 ��
# ���������ų� 27 �ұߵ����֣������б�Ϊ��[5,7,11,22]
# ��������ȡ [5,7,11,22] λ���м�� 7 �� 11 �Ƚ� ���� 11 �Ǵ��� 7 �� ���������ų� 7 ��ߵ����֣������б�Ϊ��[11,22]
# �������ȡ 11 �� 22 ���м�λ��
# �պõ��� 11 ��ʱ��Ϳ��Է��� 11 ������ֵ�ˣ����û���ҵ�����ʾ������

# ��1�� ���㷨�ķ�ʽ
arr_list = [5,7, 11, 22, 27, 33, 39, 52, 58]
number =11
count = 0
left = 0
right = len(arr_list) - 1
while left <= right:
    middle = (left + right)//2
    count += 1
    if number > arr_list[middle]:
        left = middle +1
    elif number < arr_list[middle]:
        right = middle -1
    else:
        print "����",number, "���ҵ�������ֵΪ", middle
        break
else:
    print "����",number, "û���ҵ�"
print "һ������",count,"�β���"

print "#"*30

# ��2�� �ݹ麯���ķ�ʽ
arr_list = [5,7, 11, 22, 27, 33, 39, 52, 58]

def binary_search(number,left,right):
    if left <= right:
        middle = (left + right) // 2
        if number < arr_list[middle]:
            right = middle -1
        elif number > arr_list[middle]:
            left = middle +1
        else:
            return middle
        return binary_search(number,left,right)
    else:
        return -1

print binary_search(11,0,len(arr_list)-1)
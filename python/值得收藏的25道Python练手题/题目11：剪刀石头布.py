#coding=utf-8
# ��Ϸ��ʼ����ʼ״̬���û��͵��Զ��� 100 �֣�Ӯһ��+10 �֣���һ��-10 �֡�

# ���û�Ϊ 0 ��ʱ����Ϸ��������ʾ��Ϸ��������������

# ���û�Ϊ 200 ��ʱ����Ϸ��������ʾ��Ϸ������Ӯ�ñ�����ÿ�ֱ����������ǰ�ķ���

# 1 ������� 2 ����ʯͷ 3 ����

import random as rd
print '=' * 30
print ' ' * 20, '����ʯͷ����Ϸ'
print '1������� 2 ����ʯͷ 3����'

game_info = {1: "����", 2: "ʯͷ", 3: "��"}
score = 100

while True:
    robots_choice = rd.randint(1, 3)
    user_choice = input("���ȭ")
    if user_choice not in {1,2,3}:
        print "��ȭ����,�����³�ȭ"
        continue
    user_choice = int(user_choice)
    print "*" * 30
    print "���Գ�",game_info[robots_choice]
    print "���",game_info[user_choice]
    print '*' * 60
    if user_choice ==1 and robots_choice ==3 \
        or user_choice ==2 and robots_choice ==1 \
            or user_choice == 3 and robots_choice ==2:
        score +=10
        print '��Ӯ�ñ�����Ϸ����ǰ����Ϊ',score
    elif user_choice == robots_choice:
        print "������Ϸƽ�֣���ǰ����Ϊ", score
    else:
        score -=10
        print '�����˱�����Ϸ����ǰ����', score
    if score >= 200:
        print '��Ӯ�˱�����Ϸ����ǰ����',score
        break
    elif score <= 0:
        print '��Ϸ������������'
        break
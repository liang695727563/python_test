# _*_ coding: UTF-8 _*_
# �����ռ��������
'''
 global VarName �ı��ʽ����� Python�� VarName ��һ��ȫ�ֱ�����
 ���� Python �Ͳ����ھֲ������ռ���Ѱ����������ˡ�

 ���磬������ȫ�������ռ��ﶨ��һ������ money���������ں����ڸ����� money ��ֵ��
 Ȼ�� Python ��ٶ� money ��һ���ֲ�������Ȼ�������ǲ�û���ڷ���ǰ����һ���ֲ����� money��
 ������ǻ����һ�� UnboundLocalError �Ĵ���ȡ�� global ����ע�;��ܽ��������⡣
'''
Money = 2000
def AddMoney():
    # ����������ȡ������ע�ͣ�
    global Money
    Money = Money + 1

print Money;
AddMoney();
print Money

# dir() ���� һ���ź�����ַ����б�������һ��ģ���ﶨ��������֡�
# ���ص��б���������һ��ģ���ﶨ�������ģ�飬�����ͺ������磺
# ��������mathģ��
import math

content = dir(math);
print content

# ����������ַ������� __name__ ָ��ģ������֣�__file__ ָ���ģ��ĵ����ļ���
print math.__name__
# print math.__file__

print "------------------------------------"
# globals() �� locals() ����
# print global()
print "locals():",locals()

# reload() ����
# ��һ��ģ�鱻���뵽һ���ű���ģ�鶥�㲿�ֵĴ���ֻ�ᱻִ��һ�Ρ�

# ��ˣ������������ִ��ģ���ﶥ�㲿�ֵĴ��룬������ reload() �������ú��������µ���֮ǰ�������ģ�顣
print '++++++++++++++++++++++++++'
reload(math) # reload() ��Ҫֱ�ӷ�ģ������֣�������һ���ַ�����ʽ������Ҫ����helloģ�飬�� reload(hello)
print reload(math)





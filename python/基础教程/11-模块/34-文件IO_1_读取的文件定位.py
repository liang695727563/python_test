#coding=utf-8

# ��һ���ļ�
fo = open("foo.txt", "r+")
str = fo.read(10);
print "��ȡ���ַ����ǣ�", str

# ���ҵ�ǰλ��
position = fo.tell();   # tell() �����������ļ��ڵĵ�ǰλ��
print "��ǰ�ļ�λ�ã�", position

#��ָ���ٴ����¶�λ���ļ���ͷ
position = fo.seek(0, 0);
# seek��offset [,from]�������ı䵱ǰ�ļ���λ�á�
# Offset ������ʾҪ�ƶ����ֽ�����From ����ָ����ʼ�ƶ��ֽڵĲο�λ�á�

str = fo.read(10);
print "���¶�ȡ�ַ�����", str
# �رմ򿪵��ļ�
fo.close()

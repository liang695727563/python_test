# encoding=utf-8
import json
#һ�´�����������֤���߻��������в�����ġ�
# import sys # ����sys��
# reload(sys)
# sys.setdefaultencoding('utf-8') # ����Ĭ�ϵı����ַ���Ϊuft-8�������14�е�print�� ��������±���
# ���ػ������Բ���Ҫ�ⲿ�ִ���

list_words = ['��', '��', '��']
print( list_words)    # �޷�������ʾ����cl
print( str(list_words).decode('string_escape'))  # ������ʾ����

# ע�����֡�utf-8���Ĵ�Сд����
list_words_result = json.dumps( list_words, encoding='utf-8', ensure_ascii=False )
print(list_words_result)
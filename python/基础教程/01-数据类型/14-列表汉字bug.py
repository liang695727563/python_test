#encoding=utf-8
import json
#���´�����������֤���߻��������в�����ġ�
import sys  # ����sys��
reload(sys)
sys.setdefaultencoding('utf-8')  # ����Ĭ�ϵı����ַ���Ϊutf-8,�����14�е�print����������±���
#���ػ������Բ���Ҫ�ⲿ�ִ���

list_words = [ '��', '��', '��' ]
print( list_words )                                        # �޷�������ʾ����
print( str(list_words).decode( 'string_escape' ) )         # ������ʾ����

list_words_result = json.dumps( list_words, encoding='UTF-8', ensure_ascii=False )
print( list_words_result )
# encoding:gbk


# ���������
from skill import \
    shutdown, \
    screencut, \
    analyzeWeChat, \
    logout, \
    rcmd,\
    novel


# ��������ĵ�
def help_doc():
    return \
        '�һ������ùһ�\n' \
        '���ߣ���������\n' \
        '�˳����˳�����\n' \
        '״̬���鿴��΢�ŵ�״̬\n' \
        '�ػ����ػ�\n' \
        '��Ϣ���鿴΢�ŵ���Ϣ\n' \
        'ͼ�飺����Ϊͼ�������\n' \
        '��᣺����Ϊ��������\n' \
        'rcmd [code]��Զ��cmd����\n' \
        '��������ȡ����������ͼ\n' \
        'С˵ [name]������С˵'


# �������ʽ
def plug_in(friend_data, msg):

    # һЩ������ڲ����ֱ�ӵ��õĲ���:
    # msg: �����ļ����ֵ�ʵʱ��Ϣ
    # friend_data����������

    if msg == '�ػ�':
        shutdown.main()
    if msg == '����':
        screencut.cut()
    if msg == '��Ϣ':
        analyzeWeChat.use_it(friend_data)
    if msg == '�˳�':
        logout.main()
    if msg[:5] == 'rcmd ':
        rcmd.main(msg)
    if msg[:2] == 'С˵':
        novel.main(msg)
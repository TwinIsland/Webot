# encoding:gbk
# coder: Wyatt Huang
# web: good for you to visit my blog: overfit.ml

# �����
import itchat
import replySystem
import skillConfig
import traceback

# ��ӭ����
f = open('skill/__init__.py','r')
print(f.read().split('# Coding')[0])


# ��½΢�ţ����Ҫ�ڷ�������CMD���ã���һ��������enableCmdQR=True��
itchat.auto_login(hotReload=True)

# ��ʼ�� -- ���Զ��嵫����ɾ������Ҫ��Ϊʲô
itchat.send('���� WeChat Pro �������ɹ�\n��������鿴����', 'filehelper')

# ��ȡ�û���Ϣ
friend = itchat.get_friends()
friendNum = len(friend)-1
myName = friend[0]['UserName']
myNickName = friend[0]['NickName']

# ��ʼ��״̬Ϊ������ (1��ʾ�һ�)
mode = 0

# ��ʼ������apiΪͼ��api
modeAPI = 0

# ����ϵͳ


# ����װ����
@itchat.msg_register(itchat.content.TEXT)
def main(msg):

    # return para: FromUserName ToUserName Content
    # test para: @9b9d4b50f318ba228068a732a3s3da54sd4as3d21as4a59cfeb3e7b55dfe8

    # ����״̬����ȫ�� ��Ҫ����
    global mode,modeAPI,friend

    # ����С����
    if msg['ToUserName'] == 'filehelper':

        # �����ĵ�
        help_doc = skillConfig.help_doc()

        if msg['Content'] == '����':
            itchat.send(help_doc, 'filehelper')

        ##########################################################################################
        # ��Ҫ�Ķ����ڳ��򣡣�
        if msg['Content'] == '�һ�':
            mode = 1
            itchat.send('���ùһ��ɹ���', 'filehelper')

        elif msg['Content'] == '����':
            mode = 0
            itchat.send('�������߳ɹ���', 'filehelper')

        elif msg['Content'] == 'ͼ��':
            modeAPI = 0
            itchat.send('ͼ��api���óɹ���','filehelper')

        elif msg['Content'] == '���':
            modeAPI = 1
            itchat.send('���api���óɹ���','filehelper')

        elif msg['Content'] == '״̬':
            if mode == 1:
                itchat.send('΢�Ŵ��ڹһ�״̬�����˸��㷢�ĵ���Ϣ���Զ��ظ�','filehelper')
                if modeAPI == 0:
                    itchat.send('����ʹ��ͼ������˵�api', 'filehelper')
                if modeAPI == 1:
                    itchat.send('����ʹ���������˵�api', 'filehelper')
            if mode == 0:
                itchat.send('΢�Ŵ�������״̬�����˸��㷢�ĵ���Ϣ�����Զ��ظ�','filehelper')
        ##########################################################################################

        # �Զ��������ã�
        try:
            skillConfig.plug_in(friend, msg['Content'])

        except BaseException:
            itchat.send('�������δ�ܳɹ����У�' + traceback.format_exc(), 'filehelper')

    # ������˷�����Ϣ��������ҷ��������Ϊ����ģʽ
    if mode == 1 and msg['FromUserName'] != myName:
        print(msg['FromUserName'])

        if modeAPI:

            response = replySystem.get_reply_free(msg['Content'])

        else:
            response = replySystem.getReply(msg['Content'])

            # api �쳣����
            if response == 3:
                # �޸�ģʽ
                modeAPI = 1
                # ���ͱ�����Ϣ
                itchat.send('ͼ��api�����ˣ����Զ�Ϊ���л�Ϊ�����api��', 'filehelper')
                # ���»�ȡresponse
                response = replySystem.get_reply_free(msg['Content'])

        # ͨ�����û�����api���Ǹ��˷���Ϣ��ȥ
        itchat.send("[�����˻ظ�]��" + response, msg['FromUserName'])
        # �ٸ�����˷�һ����Ϣ
        itchat.send("����Ϣ��\nsender: " + itchat.search_friends(userName=msg['FromUserName'])['NickName'],'filehelper')


# ��ʼ����
itchat.run()

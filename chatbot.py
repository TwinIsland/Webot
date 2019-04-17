# encoding:gbk
# coder: Wyatt Huang
# web: good for you to visit my blog: overfit.ml

# 导入库
import itchat
import replySystem
import skillConfig
import traceback

# 欢迎界面
f = open('skill/__init__.py','r')
print(f.read().split('# Coding')[0])


# 登陆微信（如果要在服务器或CMD上用，加一个参数：enableCmdQR=True）
itchat.auto_login(hotReload=True)

# 初始化 -- 可自定义但不能删除，不要问为什么
itchat.send('开启 WeChat Pro 服务器成功\n输入帮助查看帮助', 'filehelper')

# 获取用户信息
friend = itchat.get_friends()
friendNum = len(friend)-1
myName = friend[0]['UserName']
myNickName = friend[0]['NickName']

# 初始化状态为：在线 (1表示挂机)
mode = 0

# 初始化调用api为图灵api
modeAPI = 0

# 监听系统


# 配置装饰器
@itchat.msg_register(itchat.content.TEXT)
def main(msg):

    # return para: FromUserName ToUserName Content
    # test para: @9b9d4b50f318ba228068a732a3s3da54sd4as3d21as4a59cfeb3e7b55dfe8

    # 设置状态参数全局 重要！！
    global mode,modeAPI,friend

    # 配置小功能
    if msg['ToUserName'] == 'filehelper':

        # 帮助文档
        help_doc = skillConfig.help_doc()

        if msg['Content'] == '帮助':
            itchat.send(help_doc, 'filehelper')

        ##########################################################################################
        # 不要改动框内程序！！
        if msg['Content'] == '挂机':
            mode = 1
            itchat.send('设置挂机成功！', 'filehelper')

        elif msg['Content'] == '在线':
            mode = 0
            itchat.send('设置在线成功！', 'filehelper')

        elif msg['Content'] == '图灵':
            modeAPI = 0
            itchat.send('图灵api设置成功！','filehelper')

        elif msg['Content'] == '社会':
            modeAPI = 1
            itchat.send('社会api设置成功！','filehelper')

        elif msg['Content'] == '状态':
            if mode == 1:
                itchat.send('微信处于挂机状态，别人给你发的的消息会自动回复','filehelper')
                if modeAPI == 0:
                    itchat.send('正在使用图灵机器人的api', 'filehelper')
                if modeAPI == 1:
                    itchat.send('正在使用社会机器人的api', 'filehelper')
            if mode == 0:
                itchat.send('微信处于在线状态，别人给你发的的消息不会自动回复','filehelper')
        ##########################################################################################

        # 自定义插件调用：
        try:
            skillConfig.plug_in(friend, msg['Content'])

        except BaseException:
            itchat.send('插件错误！未能成功运行！' + traceback.format_exc(), 'filehelper')

    # 如果有人发撒消息给服务端且服务端设置为离线模式
    if mode == 1 and msg['FromUserName'] != myName:
        print(msg['FromUserName'])

        if modeAPI:

            response = replySystem.get_reply_free(msg['Content'])

        else:
            response = replySystem.getReply(msg['Content'])

            # api 异常处理
            if response == 3:
                # 修改模式
                modeAPI = 1
                # 发送报错信息
                itchat.send('图灵api出错了！已自动为您切换为“社会api”', 'filehelper')
                # 重新获取response
                response = replySystem.get_reply_free(msg['Content'])

        # 通过调用机器人api给那个人发消息回去
        itchat.send("[机器人回复]：" + response, msg['FromUserName'])
        # 再给服务端发一条消息
        itchat.send("新消息！\nsender: " + itchat.search_friends(userName=msg['FromUserName'])['NickName'],'filehelper')


# 开始监听
itchat.run()

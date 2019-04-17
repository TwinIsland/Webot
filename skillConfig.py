# encoding:gbk


# 引入配件区
from skill import \
    shutdown, \
    screencut, \
    analyzeWeChat, \
    logout, \
    rcmd,\
    novel


# 配件帮助文档
def help_doc():
    return \
        '挂机：设置挂机\n' \
        '在线：设置在线\n' \
        '退出：退出服务\n' \
        '状态：查看您微信的状态\n' \
        '关机：关机\n' \
        '信息：查看微信的信息\n' \
        '图灵：设置为图灵机器人\n' \
        '社会：设置为社会机器人\n' \
        'rcmd [code]：远程cmd命令\n' \
        '截屏：截取服务器窗口图\n' \
        '小说 [name]：搜索小说'


# 插件唤起方式
def plug_in(friend_data, msg):

    # 一些你可以在插件中直接调用的参数:
    # msg: 来自文件助手的实时消息
    # friend_data：好友数据

    if msg == '关机':
        shutdown.main()
    if msg == '截屏':
        screencut.cut()
    if msg == '信息':
        analyzeWeChat.use_it(friend_data)
    if msg == '退出':
        logout.main()
    if msg[:5] == 'rcmd ':
        rcmd.main(msg)
    if msg[:2] == '小说':
        novel.main(msg)
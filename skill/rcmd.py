# encoding:gbk

import itchat
import os


def main(msg):
    itchat.send('开始执行命令：' + msg[5:], 'filehelper')
    os.system(msg[5:])
# encoding:gbk

import itchat
import os


def main(msg):
    itchat.send('��ʼִ�����' + msg[5:], 'filehelper')
    os.system(msg[5:])
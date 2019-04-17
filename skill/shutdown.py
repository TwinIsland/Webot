# encoding:gbk
import os
import itchat


def main():
    os.system('shutdown -s -t 100')
    itchat.send('已计划关机', 'filehelper')

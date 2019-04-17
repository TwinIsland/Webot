# encoding:gbk

import itchat
from PIL import ImageGrab


def cut():
    im = ImageGrab.grab()
    im.save('data.jpg')
    itchat.send_image('data.jpg','filehelper')
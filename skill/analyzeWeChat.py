# encoding:gbk

import itchat
import matplotlib.pyplot as plt


def statistic_friends_sex(friends_dict):
    """
    该函数功能为实现 friends_dict 中性别统计
    """
    result = [0, 0, 0]
    for friend in friends_dict[1:]:
        # 好友列表第一个是自己，所以统计真正好友要从第二个开始
        sex = friend['Sex']
        if sex == 1:
            result[0] += 1
        elif sex == 2:
            result[1] += 1
        else:
            result[2] += 1

    return result


def sex_pie_chart(sex_num):
    """
    该函数功能为实现画出性别统计的饼图
    """
    labels = ['男', '女', '不明']
    colors = ['green', 'pink', 'yellow']
    # 设置字体样式
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = [u'SimHei']

    plt.pie(sex_num, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8)
    plt.title(u"你的微信好友性别情况\nPower By Wyatt", bbox={'facecolor': '0.8', 'pad': 5})
    plt.savefig('data.jpg')


def use_it(my_friends):
    statistic_result = statistic_friends_sex(my_friends)
    result = "男性好友人数："+ str(statistic_result[0])+ "\n" +"女性好友人数："+ str(statistic_result[1]) + "\n" +"不明性别好友："+ str(statistic_result[2])
    sex_pie_chart(statistic_result)
    itchat.send(result,'filehelper')
    itchat.send_image('data.jpg','filehelper')
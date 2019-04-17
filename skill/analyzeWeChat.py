# encoding:gbk

import itchat
import matplotlib.pyplot as plt


def statistic_friends_sex(friends_dict):
    """
    �ú�������Ϊʵ�� friends_dict ���Ա�ͳ��
    """
    result = [0, 0, 0]
    for friend in friends_dict[1:]:
        # �����б��һ�����Լ�������ͳ����������Ҫ�ӵڶ�����ʼ
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
    �ú�������Ϊʵ�ֻ����Ա�ͳ�Ƶı�ͼ
    """
    labels = ['��', 'Ů', '����']
    colors = ['green', 'pink', 'yellow']
    # ����������ʽ
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = [u'SimHei']

    plt.pie(sex_num, colors=colors, labels=labels, autopct='%1.1f%%', pctdistance=0.8)
    plt.title(u"���΢�ź����Ա����\nPower By Wyatt", bbox={'facecolor': '0.8', 'pad': 5})
    plt.savefig('data.jpg')


def use_it(my_friends):
    statistic_result = statistic_friends_sex(my_friends)
    result = "���Ժ���������"+ str(statistic_result[0])+ "\n" +"Ů�Ժ���������"+ str(statistic_result[1]) + "\n" +"�����Ա���ѣ�"+ str(statistic_result[2])
    sex_pie_chart(statistic_result)
    itchat.send(result,'filehelper')
    itchat.send_image('data.jpg','filehelper')
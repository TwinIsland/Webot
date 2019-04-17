#encoding:gbk

# Warning: the model: novelHelper is under constructed
#          and what you use is unfinished version

import itchat
from skill.novelEngine import novelEngine


def main(msg):
    #itchat.send('开始查询：'+ msg[6:] + '....','filehelper')
    result = novelEngine.solve_main(msg[3:])
    total = result['Total']
    url = list(map(lambda x:'https://www.owllook.net/chapter?url='+x,result['resource']))
    final_url = ''
    for i in url:
        final_url = final_url + str(i) + "\n" + '============' +'\n'
    succeed = len(url)
    log = '查询小说：' + msg[3:] + '\n' + \
          '总结果：' + str(total) + '\n' + \
          '成功：' + str(succeed) + '\n' + \
          '结果网址：\n' + final_url
    #print(log)
    itchat.send(log,'filehelper')
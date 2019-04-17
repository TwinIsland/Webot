# encoding:gbk
import json
import requests


# 图灵 api 调用
def getReply(say):

    # set the config
    f = json.load(open('turingConfig.json'))
    api_key = f['apiKey']
    password = f['password']

    # connect the server
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'

    post_stuff = {
        "perception": {
            "inputText": {
                "text": say
            }
        },
        "userInfo": {
            "apiKey": api_key,
            "userId": password
        }
    }
    result = requests.post(apiUrl,json.dumps(post_stuff)).content.decode('utf-8')

    # 如果api异常
    if json.loads(result)['intent']['code'] == 4007 or json.loads(result)['intent']['code'] == 4003:
        return 3

    return json.loads(result)['results'][0]['values']['text']

    # {"intent":{"code":4007},"results":[{"groupType":0,"resultType":"text","values":{"text":"apiKey格式不合法!"}}]}
    # {"intent":{"actionName":"","code":10020,"intentName":""},"results":[{"groupType":1,"resultType":"text","values":{"text":"你可以"}}]}


# 社会聊天 API
def get_reply_free(say):
    apiUrl = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg='
    requestBody = apiUrl + say
    return json.loads(requests.get(requestBody).content.decode('utf-8'))['content']


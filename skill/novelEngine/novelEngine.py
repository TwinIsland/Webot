#encoding:gbk

import requests
import lxml.etree as etr


def get_page_content(url):
    p = requests.get(url).content
    return etr.HTML(p)

#/html/body/div[1]/div/div/div[1]/####源div[1]###/li/div[2]/span[3]
# /html/body/div[1]/div/div/div[1]/div[1]/li/a
# 解析前缀：/html/body/div[1]/div/div/div[1]/
# 解析源：源div[1]
# 解析结果：li/div[2]/span[3]


def page_source_count(cont):
    # 返回资源数量
    return int(cont.xpath('/html/body/div[1]/div/div/p/text()')[0][3])

def source_exist(cont,where):
    result = cont.xpath('/html/body/div[1]/div/div/div[1]/div['+str(where)+']/li/div[2]/span[3]/text()')
    if result == []:
        return 0
    else:
        if result[0] == '已解析':
            return 1
    return 0
    # /html/body/div[1]/div/div/div[1]/div[1]/li/div[2]/span[3]

def page_in_source(cont):
    count = page_source_count(cont)
    resource = []
    for i in range(0,count):
        if source_exist(cont,i):
            resource.append(cont.xpath('/html/body/div[1]/div/div/div[1]/div['+str(i)+']/li/a/@href')[0])

    return list(map(lambda x:x[13:],resource))

# 搜索api: https://www.owllook.net/search?wd=

def solve_main(search_for):
    p = get_page_content('https://www.owllook.net/search?wd=' + search_for)

    return {
        'Total':page_source_count(p),
        'resource':page_in_source(p) # ['https://www.qu.la/book/59384/&novels_name=三体'
    }


# CPT Engine
def cpt(resource_url):

    solve_domian = 'https://www.owllook.net/owllook_content?url='
    main_domain = resource_url.split('?url=')[1].split('/')[0]
    cpt_num = 1
    cpt_index= {}

    p = get_page_content(resource_url)

    # 章节名：/html/body/div[2]/div[1]/dl/dd[16]/a/text()

    while True:
        # /html/body/div[2]/div[1]/dl/dd[251]/a
        count = p.xpath('/html/body/div[2]/div[1]/dl/dd['+str(cpt_num)+']/a/text()')
        url = p.xpath('/html/body/div[2]/div[1]/dl/dd['+str(cpt_num)+']/a/@href')
        cpt_num += 1
        if count != []:
            cpt_index[count[0]] = url
            continue
        break
    return cpt_index


'''
a = 'https://www.owllook.net/chapter?url=https://www.biqukan.com/3_3037/&novels_name=%E6%96%97%E7%A0%B4%E8%8B%8D%E7%A9%B9'

print(cpt(a))

print(test.split('/')[0]+'//'+test.split('/')[2])
'''


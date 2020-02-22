import requests
import time
import json

#目标网址
url = 'http://data.stats.gov.cn/easyquery.htm'

#获取时间戳
def gettime():
    return int(round(time.time() * 1000))

#爬取人口数据模块
def getpopula_data():

    #自定义头部
    headers = {}
    #传递参数
    keyvalue = {}
    #头部填充
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) ' \
                            'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                            'Version/12.0 Safari/605.1.15'
    #参数填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A0301"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r = s.post(url, params=keyvalue, headers=headers)
    return json.loads(r.text)

#爬取人民币汇率
def getexchange_rate():
    headers = {}
    keyvalue = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) ' \
                            'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                            'Version/12.0 Safari/605.1.15'
    #参数填充
    keyvalue['m'] ='QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A060J01"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r1 = s.post(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A060J02"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r2 = s.post(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A060J03"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r3 = s.post(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A060J04"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r4 = s.post(url, params=keyvalue, headers=headers)

    return json.loads(r1.text),json.loads(r2.text),json.loads(r3.text),json.loads(r4.text)

#爬取财政数据模块
def  getfinance_data():

    #自定义头部
    headers = {}
    #传递参数
    keyvalue = {}
    #头部填充
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14) ' \
                            'AppleWebKit/605.1.15 (KHTML, like Gecko) ' \
                            'Version/12.0 Safari/605.1.15'

    #参数填充
    keyvalue['m'] = 'QueryData'
    keyvalue['dbcode'] = 'hgnd'
    keyvalue['rowcode'] = 'zb'
    keyvalue['colcode'] = 'sj'
    keyvalue['wds'] = '[]'
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A080101"}]'
    keyvalue['k1'] = str(gettime())


    #建立一个Session
    s = requests.session()
    #在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    #打印返回过来的状态码
    print(r.status_code)
    #修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    #再次进行请求
    r1 = s.post(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A080102"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r2 = s.post(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A080103"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r3 = s.post(url, params=keyvalue, headers=headers)
    keyvalue['dfwds'] = '[{"wdcode":"zb","valuecode":"A080104"}]'
    keyvalue['k1'] = str(gettime())

    # 建立一个Session
    s = requests.session()
    # 在Session基础上进行一次请求
    r = s.post(url, params=keyvalue, headers=headers)
    # 打印返回过来的状态码
    print(r.status_code)
    # 修改dfwds字段内容
    keyvalue['dfwds'] = '[{"wdcode":"sj","valuecode":"LAST20"}]'
    # 再次进行请求
    r4 = s.post(url, params=keyvalue, headers=headers)

    return json.loads(r1.text),json.loads(r2.text),json.loads(r3.text),json.loads(r4.text)


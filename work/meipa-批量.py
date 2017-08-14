#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64,time,csv
import requests,random
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq




headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Cache-Control':'no-cache, must-revalidate',
    'Connection':'keep-alive',
    'Cookie':'MUSID=8vri72q8k1q7c0ij5mocv02a87; virtual_device_id=60c7a018731a82abc1aef2dbd746030a; pvid=WGaWkSZjv01Vs1ggAFMm2kTMn%2FP6wcaR; sid=8vri72q8k1q7c0ij5mocv02a87; UM_distinctid=15dbfaf7f10128-0d0848ad115148-474b0921-1fa400-15dbfaf7f111f7',
}
#使用代理服务器
proxy_list=[
    'http://42.81.11.22:8080',#好的
    'http://111.13.7.117:80',#好的
    'http://183.222.102.105:80',#好的
    'http://183.222.102.104:8080',
    'http://183.222.102.99:80',
    # 'http://183.222.102.101:80',
    'http://183.222.102.94:80',
    'http://218.201.98.196:3128',
    'http://120.52.21.132:8082',#被办的IP
    'http://121.40.199.105:80',
    'http://219.153.76.77:8080',
    # 'http://58.49.110.50:8080',#慢
    'http://119.36.92.42:81',
    'http://61.160.208.222:8080',
    'http://119.36.92.41:81',
    'http://42.81.11.22:8080',
    'http://111.13.7.117:80',
    'http://111.13.7.122:80',
    # 'http://101.200.44.5:8888',
    'http://124.89.33.75:9999',
    ]
proxy_ip = random.choice(proxy_list)
proxies = {'http':proxy_ip}
print(proxy_ip)

time_list=[1,2,3,4]
random.choice(time_list)


from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s'%str(proxy_ip))
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.meipai.com/square/18?p=9')
time.sleep(2)
for i in range(1,6):
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(2)
    # print(driver.page_source)
urls=[]
soup=BeautifulSoup(driver.page_source,'lxml')
articles=[]
for link in soup.select('a.content-l-p.pa'):
    item_link = 'http://www.meipai.com' + link.get('href')
    urls.append(item_link)
    print(item_link)

class Decode:
    def getHex(self,param1):
        return {
            'str': param1[4:],
            'hex': ''.join(list(param1[:4])[::-1]),
        }

    def getDecimal(self, param1):
        loc2 = str(int(param1, 16))
        print('loc2',loc2)#
        return {
            'pre': list(loc2[:2]),
            'tail': list(loc2[2:]),
        }

    def substr(self, param1, param2):
        loc3 = param1[0: int(param2[0])]
        loc4 = param1[int(param2[0]): int(param2[0]) + int(param2[1])]
        print("loc4",loc4)
        return loc3 + param1[int(param2[0]):].replace(loc4, "")

    def getPosition(self,param1, param2):
        param2[0] = len(param1) - int(param2[0]) - int(param2[1])
        return param2

    def decode(self, code):
        dict2 = self.getHex(code)
        dict3 = self.getDecimal(dict2['hex'])
        print("dict3", dict3['pre'])  #
        str4 = self.substr(dict2['str'], dict3['pre'])
        time.sleep(1)
        return base64.b64decode(self.substr(str4, self.getPosition(str4, dict3['tail'])))

    def crawl_video_url(self, url):
        results=[]
        response = requests.get(url,proxies=proxies,headers=headers).content
        print(url)
        d = pq(response)
        code= d('meta[property="og:video:url"]').attr('content')
        print(code)
        result = self.decode(code)
        results.append(result)
        print(result)
        time.sleep(1)

# with open('meipai_page1.csv','w',newline='') as f:  #newline='' 标示在csv里不空行
#     writer=csv.writer(f)
#     writer.writerow(['链接',])
#     for row in articles:
#         writer.writerow(row)


if __name__ == '__main__':
    for url in urls:
# url = "http://www.meipai.com/media/815287106"
        try:
            Decode().crawl_video_url(url)
        except:
            # print('解析:',url,' 出现错误')
            continue





# f8d0aHRNGYo0 cDovL212dmlkZW8xMS5tZWl0dWRhdGEuY29tLzU5OGFl YjdkNDE4NjQzNTk5LMm1wNA
#
# fa50aHWjVHR0 cDovL212dmlkZW8xMS5tZWl0dWRhdGEuY29tLzU5OGFl YjdkNDE4NjQzNTk5Lm1kXR7LwNA
#
# 5f01aHR0FF9  cDovL212dmlkZW8xMS5tZWl0dWRhdGEuY29tLzU5OGFl OGRiNjlmYmY4ODA3Lm1wuNA
#
# cdc1aHR0cDoNdxvL212dmlkZW8xLm1laXR1ZGF0YS5jb20vNTk4YWU0YTVkODQ1Yzc4exqczmdiOTQubXA0
#
# 0409
# 8247

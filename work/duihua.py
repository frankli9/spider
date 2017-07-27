#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
from lxml import etree
import re,random


headers={
    'User-Agent':'ozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'prov=cn010; city=010; weather_city=bj; region_ip=182.50.113.x; region_ver=1.2; __gads=ID=282899b909c82fa9:T=1499047786:S=ALNI_MaicV_P3CPTRMYlX24RxBVg2CrKdA; UM_distinctid=15d06368b3252-0e1cc3d39188b5-474b0921-1fa400-15d06368b33b2d; userid=1499047825880_qmtdvd9543; vjuids=20d3662a0.15d06370c48.0.4eaffd0ce18c2; __dns__=%7B%22HTTP_X_FORWARDED_FOR%22%3A%22%22%2C%22REMOTE_ADDR%22%3A%22182.50.113.242%22%2C%22SERVER_HOST%22%3A%22276392890.nstool.ifengcdn.com%22%2C%22DNS_RESOLVE%22%3A%22218.30.106.242%22%7D; vjlast=1499047857.1499736539.13',}
#使用代理服务器
proxy_list=[
    'http://113.123.19.152:808',
    'http://114.231.104.176:808',
    'http://119.39.68.61:808',
    ]
proxy_ip = random.choice(proxy_list)
proxies = {'http':proxy_ip}


url='http://www.datiegun.com/xiangshengxiaopin/472119.html'
def get_item_info(url):
    html = requests.get(url).content.decode('gb18030')#,headers=headers,proxies=proxies
    dom_tree = etree.HTML(html)
    word = dom_tree.xpath('//div[@class="content"]/p//text()')
    file_object = open('E:\\Chinese\\duihua.txt', 'a', encoding='utf-8')
    time.sleep(1)
    for a in word:
        file_object.write(a)
        print(a)
    file_object.close()

get_item_info(url)

# def get_links_from(page):
#     urls=[]
#     # list_view='http://www.datiegun.com/xiangshengxiaopin/{}.html'
#     list_view='http://www.datiegun.com/xiangshengxiaopin/{}.html'.format(str(page))
#     wb_data = requests.get(list_view,headers=headers,proxies=proxies)
#     soup=BeautifulSoup(wb_data.text,'lxml')
#     # time.sleep(1)
#     for link in soup.select('div.news_list > a'):
#         item_link=link.get('href')
#         url=item_link
#         urls.append(url)

#     print(urls)
#     print(len(urls))
    # for i in urls:
    #     get_item_info(i)

# get_links_from(2)

# for i in range(100,150):
#      get_links_from(i)
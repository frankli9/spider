#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
from lxml import etree
import os
import re,random
#
#
headers={
    'User-Agent':'ozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.8',
    'Connection':'keep-alive',
    'Cookie':'prov=cn010; city=010; weather_city=bj; region_ip=182.50.113.x; region_ver=1.2; __gads=ID=282899b909c82fa9:T=1499047786:S=ALNI_MaicV_P3CPTRMYlX24RxBVg2CrKdA; UM_distinctid=15d06368b3252-0e1cc3d39188b5-474b0921-1fa400-15d06368b33b2d; userid=1499047825880_qmtdvd9543; vjuids=20d3662a0.15d06370c48.0.4eaffd0ce18c2; __dns__=%7B%22HTTP_X_FORWARDED_FOR%22%3A%22%22%2C%22REMOTE_ADDR%22%3A%22182.50.113.242%22%2C%22SERVER_HOST%22%3A%22276392890.nstool.ifengcdn.com%22%2C%22DNS_RESOLVE%22%3A%22218.30.106.242%22%7D; vjlast=1499047857.1499736539.13',}
#使用代理服务器
# # proxy_list=[
#     # 'http://125.45.87.12:9999',#好的
#     # 'http://218.75.149.207:3128',
#     # 'http://222.89.82.19:808',
#     # 'http://200.43.138.196:8080',
#     # 'http://190.212.129.218:80',
#     # 'http://89.187.217.114:80',
#     # 'http://95.79.45.18:8080',
#     # 'http://191.101.12.210:8080',
#     # 'http://36.80.221.63:8080',
#     # 'http://168.228.220.195:8080',
#     # 'http://219.94.78.161:8080',
#
# #     ]
# # proxy_ip = random.choice(proxy_list)
# # print(proxy_ip)
# # proxies = {'http':proxy_ip}
#
#
# url='http://sc.chinaz.com/tupian/161118118331.htm'

# def get_item_info(url):
#
#     html = requests.get(url).content.decode('utf-8')#,headers=headers,proxies=proxies
#     dom_tree = etree.HTML(html)
#     word = dom_tree.xpath('//div[@class="imga"]/a/@href')[0]
#     print(word)
#     time.sleep(1)
#     img_content = requests.get(word).content
#
#     # i = 1
#     # file_name = str(i) + '.jpg'
#     with open(os.getcwd()+'/'+file_name, 'wb') as wf:
#         wf.write(img_content)



    # file_object = open('E:\\Chinese\\.txt', 'a', encoding='utf-8')
    # time.sleep(1)
    # for a in word:
    #     file_object.write(a+'\n')
    #     print(a)
    # file_object.close()
#
# get_item_info(url)

def get_links_from(page):
    urls=[]
    # list_view='http://www.datiegun.com/xiangshengxiaopin/{}.html'
    list_view='http://aspx.sc.chinaz.com/query.aspx?keyword=%E5%BB%BA%E7%AD%91%E7%89%A9&classID=11&page={}'.format(str(page))
    wb_data = requests.get(list_view,headers=headers,)#proxies=proxies
    soup=BeautifulSoup(wb_data.text,'lxml')
    # time.sleep(1)
    for link in soup.select('#container > div > p > a'):
        item_link=link.get('href')
        urls.append(item_link)
    print(urls)
    print(len(urls))
    i = 145
    for url in urls:
        html = requests.get(url).content.decode('utf-8')  # ,headers=headers,proxies=proxies
        dom_tree = etree.HTML(html)
        word = dom_tree.xpath('//div[@class="imga"]/a/@href')[0]
        print(word)
        time.sleep(1)
        # img_content = requests.get(word).content
        file_name = str(i) + '.jpg'
        with open(os.getcwd() + '/' + file_name, 'wb') as wf:
            img_content = requests.get(word).content
            wf.write(img_content)
            i += 1
# print(len(os.listdir("E:\\Chinese")))

get_links_from(7)

#
#     print(urls)
#     print(len(urls))
#     for i in urls:
#         get_item_info(i)


# for i in range(4,10):
#      get_links_from(i)


# import requests
# from bs4 import BeautifulSoup
# import os
# #获取html
# f = requests.get('http://sc.chinaz.com/tupian/richutupian_2.html',headers=headers).text
# print(f)
# #用BS解析html
# s = BeautifulSoup(f,'lxml')
# s_imgs = s.find_all('img',pic_type='0')
# #逐个将图片保存到本地
# i=1
# for s_img in s_imgs:
#     img_url = s_img['src']
#     img_content = requests.get(img_url).content
#     file_name = str(i) + '.jpg'
#     with open(os.getcwd()+'/'+file_name, 'wb') as wf:
#         wf.write(img_content)
#     i += 1
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests
import time
import pymongo


client = pymongo.MongoClient('localhost',27017)
ganji = client['ganji']
url_list_ganji = ganji['url_list_ganji']
item_info_ganji = ganji['item_info_ganji']

def get_links_from(channel,pages):
    #http://bj.ganji.com/shouji/o3/
    list_view = '{}o{}/'.format(channel,str(pages))
    wb_data = requests.get(list_view)
    time.sleep(3)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link = link.get('href').split('?')[0]
            url_list_ganji.insert_one({'url':item_link})
            print(item_link)
            get_item_info(item_link)
    else:
        pass

# get_links_from('http://bj.ganji.com/chuangdian/',12)

def get_item_info(url):
    wb_data=requests.get(url)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('span','soldout_btn'):        #查找页面中的span标签的class类，如果存在，就pass，代表下架页面
        pass
    else:
        soup = BeautifulSoup(wb_data.text, 'lxml')
        title = soup.select('h1.info_titile')[0].text.strip()
        price = soup.select('span.price_now > i')[0].text
        area = soup.select('div.palce_li > span > i')[0].text.split('-')[1]
        view = soup.select('span.look_time')[0].text.strip('次浏览')
        item_info_ganji.insert_one({'title':title,'price':price,'area':area,'view':view,'url':url})
        print({'title':title,'price':price,'area':area,'view':view,'url':url})

# get_item_info('http://zhuanzhuan.ganji.com/detail/804304851916125192z.shtml')
# get_item_info('http://zhuanzhuan.ganji.com/detail/855760974003617800z.shtml')

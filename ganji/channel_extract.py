#!/usr/bin/env python
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup
import requests

start_url = 'http://bj.ganji.com/wu/'
host_url = 'http://bj.ganji.com'

def get_channel_urls(url):
    wb_data = requests.get(start_url)
    wb_data.encoding = 'utf-8'   #解决打印乱码
    soup = BeautifulSoup(wb_data.text,'lxml')
    links = soup.select('div.content > div > div > dl > dd > a')
    for link in links:
        page_url = host_url + link.get('href')
        print(page_url)
# get_channel_urls(start_url)

channel_list='''
    http://bj.ganji.com/chuangdian/
    http://bj.ganji.com/guizi/
    http://bj.ganji.com/zhuoyi/
    http://bj.ganji.com/shafachaji/
    http://bj.ganji.com/zixingchemaimai/
    http://bj.ganji.com/diandongche/
    http://bj.ganji.com/motuoche/
    http://bj.ganji.com/iphone/
    http://bj.ganji.com/nokia/
    http://bj.ganji.com/htc/
    http://bj.ganji.com/sanxingshouji/
    http://bj.ganji.com/motorola/
    http://bj.ganji.com/shouji/_%E5%B0%8F%E7%B1%B3/
    http://bj.ganji.com/shouji/_%E9%AD%85%E6%97%8F/
    http://bj.ganji.com/tongxuntaocan/
    http://bj.ganji.com/qqhao/
    http://bj.ganji.com/bangongjiaju/
    http://bj.ganji.com/jiguangyitiji/
    http://bj.ganji.com/dayinji/z1/
    http://bj.ganji.com/shipinjiagongshebei/
    http://bj.ganji.com/shengchanjiamengshebei/
    http://bj.ganji.com/jichuang/
    http://bj.ganji.com/tuolaji/
    http://bj.ganji.com/dianshi/
    http://bj.ganji.com/bingxiang/
    http://bj.ganji.com/kongtiao/
    http://bj.ganji.com/reshuiqi/
    http://bj.ganji.com/xiyiji/
    http://bj.ganji.com/diancilu/
    http://bj.ganji.com/weibolu/
    http://bj.ganji.com/yueqiyinxiang/
    http://bj.ganji.com/pingbandiannao/z1/
    http://bj.ganji.com/ershoubijibendiannao/z1/_%E8%8B%B9%E6%9E%9C/
    http://bj.ganji.com/ershoubijibendiannao/z1/_%E8%81%94%E6%83%B3/
    http://bj.ganji.com/ershoubijibendiannao/z1/_Thinkpad/
    http://bj.ganji.com/ershoubijibendiannao/z1/_%E7%B4%A2%E5%B0%BC/
    http://bj.ganji.com/ershoubijibendiannao/z1/_%E6%88%B4%E5%B0%94/
    http://bj.ganji.com/ershoubijibendiannao/z1/_%E5%8D%8E%E7%A1%95/
    http://bj.ganji.com/ershoubijibendiannao/z1/_%E6%83%A0%E6%99%AE/
    http://bj.ganji.com/yueqi/
    http://bj.ganji.com/yinxiang/
    http://bj.ganji.com/yundongqicai/
    http://bj.ganji.com/tongche/
    http://bj.ganji.com/tongzhuang/
    http://bj.ganji.com/yingerche/
    http://bj.ganji.com/yingerchuang/z1/
    http://bj.ganji.com/niaobushi/
    http://bj.ganji.com/wanju/
    http://bj.ganji.com/naifen/
    http://bj.ganji.com/taishidiannaozhengji/
    http://bj.ganji.com/xianka/
    http://bj.ganji.com/cpu/
    http://bj.ganji.com/yingpan/
    http://bj.ganji.com/luyouqi/
    http://bj.ganji.com/3gwangka/
    http://bj.ganji.com/shoucangpin/
    http://bj.ganji.com/qitalipinzhuanrang/
    http://bj.ganji.com/baojianpin/
    http://bj.ganji.com/xiaofeika/
    http://bj.ganji.com/fushi/
    http://bj.ganji.com/xiangbao/
    http://bj.ganji.com/xuemao/
    http://bj.ganji.com/shoubiao/
    http://bj.ganji.com/shipin/
    http://bj.ganji.com/huazhuangpin/
    http://bj.ganji.com/hufupin/
    http://bj.ganji.com/shumaxiangji/
    http://bj.ganji.com/shumashexiangji/
    http://bj.ganji.com/youxiji/
    http://bj.ganji.com/suishenting/
    http://bj.ganji.com/yidongcunchu/
    http://bj.ganji.com/zibubaojian/z2/
    http://bj.ganji.com/anmobaojian/z1/
    http://bj.ganji.com/bawanwujian/
'''
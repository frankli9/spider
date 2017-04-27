from multiprocessing import Pool
from channel_extract import channel_list
from page_parsing import get_links_from
import time

def get_all_links_from(channel):
    for num in range(1,20):
        time.sleep(3)
        get_links_from(channel,num)

#get_all_links_from('http://bj.ganji.com/chuangdian/')  将chuangdian频道下面的20个页面中的链接取出

if __name__=='__main__':
    pool = Pool()
    pool.map(get_all_links_from,channel_list.split())    #将chuangdian频道下面的20个页面中的链接取出

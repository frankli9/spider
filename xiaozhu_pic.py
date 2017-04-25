from bs4 import BeautifulSoup
import requests,urllib.request
import time

info=[]
# url = 'http://bj.xiaozhu.com/search-duanzufang-p3-0/'
# urls=['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,2)]
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Cookie':'abtest_ABTest4SearchDate=b; gr_user_id=0b8ec401-b77b-4aa8-ad72-73d5a1535e0c; __utmt=1; xzuuid=d1f42dbe; OZ_1U_2282=vid=v8fe170962e308.0&ctime=1493093407&ltime=1493093404; OZ_1Y_2282=erefer=http%3A//bzclk.baidu.com/adrc.php%3Ft%3D06KL00c00fZc7KC0hgdm0F-7F6AGzO4m000002IB_H300000TEJ0lD.THLfCIUVV_1g36K85yF9pywdpAqVuNqsusK15ywBPjIBn1N9nj0snWPBP1n0IHdjwH0zPHb4rjIAn1FKP1mLnWm3rDF7wD77wjwKwj-DPfK95gTqFhdWpyfqnWbzPHDsnjT1nBusThqbpyfqnHm0uHdCIZwsrBtEILILQM9GmyqlpZR8mvqV0APzm1Y1P1R1n6%26tpl%3Dtpl_10085_14394_1%26l%3D1051812519%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525B0%25258F%2525E7%25258C%2525AA%2525E7%25259F%2525AD%2525E7%2525A7%25259F%2525E2%252580%252594%2525E5%2525B1%252585%2525E4%2525BD%25258F%2525E8%252587%2525AA%2525E7%252594%2525B1%2525E4%2525B8%2525BB%2525E4%2525B9%252589%2525EF%2525BC%25258C%2525E7%25259F%2525AD%2525E7%2525A7%25259F%2525E6%2525B0%252591%2525E5%2525AE%2525BF%2526xp%253Did%28%252522m294177ae%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D148%26ie%3Dutf-8%26f%3D3%26tn%3Dbaiduhome_pg%26wd%3D%25E5%25B0%258F%25E7%258C%25AA%25E7%259F%25AD%25E7%25A7%259F%26oq%3D%25E5%25B0%258F%25E7%258C%25AA%25E7%259F%25AD%25E7%25A7%259F%26issp%3D1%26inputT%3D2381&eurl=http%3A//www.xiaozhu.com/&etime=1493093287&ctime=1493093407&ltime=1493093404&compid=2282; _ga=GA1.2.516362266.1493047050; __utma=29082403.516362266.1493047050.1493047053.1493093288.2; __utmb=29082403.5.10.1493093288; __utmc=29082403; __utmz=29082403.1493093288.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E5%B0%8F%E7%8C%AA%E7%9F%AD%E7%A7%9F; gr_session_id_59a81cc7d8c04307ba183d331c373ef6=3e64f1cb-290b-4631-8bef-4dca8a55a56f'
}
#
# def get_info(url):
#     wb_data = requests.get(url,headers=headers)
#     time.sleep(2)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     titles = soup.select('span.result_title.hiddenTxt')
#     prices = soup.select('span.result_price > i')
#
#     for title,price in zip(titles,prices):
#         data={
#             'title':title.get_text(),
#             'price':price.get_text(),
#         }
#         info.append(data)
#
# for single_url in urls:
#     get_info(single_url)            #将每一个列表页带入
#
#
# for i in info:
#     if float(i['price'])<300:       #判断价格
#         print(i['title'],i['price'])

url='http://'
download_links=[]

def get_pci(url):
    wb_data=requests.get(url,headers=headers)
    time.sleep(2)
    soup=BeautifulSoup(wb_data.text,'lxml')
    pic_links=soup.select('div.text > p > a')  #根据网址修改图片地址
    for pci_tag in pic_links:
        data='http:'+pci_tag.get('href')        #根据网址修改图片地址
        download_links.append(data)
        print('done')
get_pci(url)

folder_path = 'D:\\pachong\\'   #保存图片到本地
for item in download_links:
    urllib.request.urlretrieve(item,folder_path + item[-10:])




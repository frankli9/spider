
from bs4 import BeautifulSoup

info=[]
with open('D:\\BaiduYunDownload\\Python3实战：四周实现爬虫系统（重要）\\课程资料\\课程源码及作业参考答案\\Plan-for-combating-master\\week1\\1_2\\1_2answer_of_homework\\1_2_homework_required\\index.html','r') as wb_data:
    soup=BeautifulSoup(wb_data,'lxml')
    titles = soup.select('div.caption > h4:nth-of-type(2)')
    images = soup.select('div.thumbnail > img')
    stars  = soup.select('div.ratings > p:nth-of-type(2)')

for title,image,star in zip(titles,images,stars):
    data={
        'title':title.get_text().strip('\n'),                   #str.strip("\r\n"," ") 去掉末尾的\n
        'image':image.get('src'),
        'star':len(star.find_all('span',class_='glyphicon glyphicon-star'))  #使用find_all可以找到所有的星
    }
    info.append(data)

for i in info:
    if float(i['star'])>3:    #提取三颗星以上的数据
        print(i['title'],i['star'])


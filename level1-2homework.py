

from bs4 import BeautifulSoup

with open('\\index.html','r') as wb_data:
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
    print(data)
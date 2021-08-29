
'''
# 对象的实例化
# 第一种：将本地中的html文档中的数据加载到该对象中
f = open('./test.html', 'r', encoding='utf-8')
soup = BeautifulSoup(f, 'lxml')

# 第二种：将互联网上获取的页面源码加载到该对象中
page_text = response.text
soup = BeautifulSoup(page_text, 'lxml')

# print(soup.a)  # soup.tagName返回的是文档中第一次出现的tagName标签
# print(soup.find('div'))  # 等同于soup.div
# print(soup.find('div', class_='song'))  # 属性定位
# print(soup.find_all('a'))  # 符合要求的所有标签（列表）
# print(soup.select('.tang'))

select('某种选择器(id, class, 标签...选择器)')，返回的是一个列表
层级选择器：
    soup.select('.tang > ul > li > a'):>表示的是一个层级
    soup.select('.tang > ul a'):空格表示的多个层级
'''

import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    # 对首页的页面数据进行爬取
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    page_text = requests.get(url=url, headers=headers).text

    # 在首页中解析出章节的标题和详情页的url
    # 1、实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text, 'lxml')
    # 2、解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    f = open('./sanguo.txt', 'w', encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_li = 'http://www.shicimingju.com' + li.a['href']
        # 对详情页发起请求，解析出章节内容
        detail_page_text = requests.get(url=detail_li, headers=headers).text
        detail_soup = BeautifulSoup(detail_page_text, 'lxml')
        div_tag = detail_soup.find('div', class_='chapter_content')
        # 解析到了章节内容
        content = div_tag.text

        f.write(title + ':' + content + '\n')
        print(title, '爬取成功')








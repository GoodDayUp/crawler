
'''
    # 实例化一个etree对象，且将被解析的源码加载到了该对象中
    tree = etree.parse('./test.html')
    tree.xpath('/html/body/div')  # /表示的是从根节点开始定位，表示的是一个层级
    tree.xpath('/html//div')   # //表示的是多个层级
    tree.xpath('//div')  # //可以表示从任意位置开始定位
    tree.xpath('//div[@class="song"]')  # 属性定位tag[@attrName='attrValue']
    tree.xpath('//div[@class="song"]/p[3]')  # 索引定位，索引从1开始
    获取文本：
        /text()：获取的是标签中直系的文本内容
        //text()：获取的是标签中非直系的文本内容（所有的文本内容）

'''



from lxml import etree
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    url = 'https://www.58.com/ppkchuzu671/index.html/'
    page_text = requests.get(url=url, headers=headers).text

    # 数据解析
    tree = etree.HTML(page_text)
    # 存储的就是li标签对象
    li_list = tree.xpath('//div[@class="list-part"]/ul/li')
    f = open('./58.txt', 'w', encoding='utf-8')
    for li in li_list:
        # 局部解析
        title = li.xpath('./a/div/span[@class="mark"]/text()')[0]
        print(title)
        f.write(title + '\n')








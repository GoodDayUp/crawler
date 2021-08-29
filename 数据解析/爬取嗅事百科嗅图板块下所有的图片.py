
import requests
import re
import os

if __name__ == '__main__':
    if not os.path.exists('./qiutuLibs'):
        os.mkdir('./qiutuLibs')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    url = 'https://www.qiushibaike.com/imgrank/'
    # text(字符串)  content(二进制)  json(对象)
    page_text = requests.get(url=url, headers=headers).text

    ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    img_src_list = re.findall(ex, page_text, re.S)
    for src in img_src_list:
        src = 'https:' + src
        # 请求得到了图片的二进制数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        imgPath = './qiutuLibs/' + img_name
        with open(imgPath, 'wb') as f:
            f.write(img_data)

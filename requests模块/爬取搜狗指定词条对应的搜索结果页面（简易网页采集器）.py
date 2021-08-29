
import requests

"""
    User-agent 请求载体的身份标识
    UA伪装：伪装成某一款浏览器
"""



if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装在字典中
    kw = input('enter a word: ')
    param = {
        'query':kw
    }
    response = requests.get(url=url, params=param, headers=headers)
    page_text = response.text
    fileName = kw+'.html'
    with open(fileName, 'w', encoding='utf-8') as f:
        f.write(page_text)
    print(fileName, '保存成功')
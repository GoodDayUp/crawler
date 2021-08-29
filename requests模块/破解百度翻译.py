
import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    url = 'https://fanyi.baidu.com/sug'
    word = input('enter a word: ')
    data = {
        'kw':word
    }
    # 请求发送
    response = requests.post(url=url, data=data, headers=headers)
    # json返回的是对象  如果确认响应数据是json类型，才可以用json
    dic_obj = response.json()
    fileName = word+'.json'
    f = open(fileName, 'w', encoding='utf-8')
    json.dump(dic_obj, fp=f, ensure_ascii=False)
    print('结束！')



import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'1',  # 从库中得第几部电影去取
        'limit':'20',  # 一次取出的个数
    }
    response = requests.get(url=url, params=param, headers=headers)
    list_data = response.json()
    f = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=f, ensure_ascii=False)
    print('done!')






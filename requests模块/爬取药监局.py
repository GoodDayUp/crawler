
import requests
import json
'''
通过对详情页url的观察发现：
    url的域名是一样的，只有携带的参数id不一样
    id值可以从首页对应的ajax请求到的json串中获取
    域名和id值拼接处一个完整的企业对应的详情页的url
详情页的企业详情数据也是动态加载出来的
    所有的post请求的url是一样的，只有参数id值不同
    如果我们可以批量获取多家id，就可以将id和url形成一个完整的详情页对应详情
'''


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    id_list = []  # 详情企业的id
    all_data_list = []  # 存储所有的企业详情数据
    # 批量获取不同企业的id值
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1, 6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize':' 15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }
        json_ids = requests.post(url=url, data=data, headers=headers).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    # 获取企业详情
    post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        all_data_list.append(detail_json)
    f = open('./化妆品公司.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=f, ensure_ascii=False)


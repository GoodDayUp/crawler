

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
url = 'https://www.baidu.com/s?wd=ip'

page_text = requests.get(url=url, headers=headers, proxies={'代理ip'}).text

with open('/ip.html', 'w', encoding='utf-8') as f:
    f.write(page_text)

# 反爬机制
# 反反爬策略：使用代理进行请求发送


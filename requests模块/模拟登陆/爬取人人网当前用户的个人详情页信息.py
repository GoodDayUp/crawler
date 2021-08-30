
import requests
from lxml import etree
import YDMHttp

# 封装识别验证码图片的函数
def getcodeText(imgPath, codeType):
    # 云打码平台普通用户用户名和密码
    username = ''
    password = ''

    appid = 6003
    appkey = ''

    filename = imgPath

    codetype = codeType

    timeout = 20  # s
    result = 0
    if username == 'username':
        print('请设置好相关参数在测试')
    else:
        yundama = YDMHttp(username, password, appid, appkey)
        uid = yundama.login()
        print('uid: %s' % uid)
        balance = yundama.balance()
        print('balance: %s' % balance)
        cid, result = yundama.decode(filename, codeType, timeout)
        print('cid:%s, result:%s' % (cid, result))
    return result



# 创建一个session对象
session = requests.Session()

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 1、对验证码进行捕获和识别
url = 'http://www.renren.com/SysHome.do'
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
code_img_data = requests.get(url=code_img_src, headers=headers).content
with open('./code.jpg') as f:
    f.write(code_img_data)

# 2、使用云打码提供的示例代码对验证码识别
result = getcodeText('./code.jpg', 2004)

# 3、请求的发送（模拟登陆）
login_url = ''
data = {
    'email':'',
    'icode':result,
    'orginURL':'http://www.renren.com/home',
    'domin':'renren.com',
    'key_id':'1',
    'captcha_type':'web_login',
    'password':'',
    'rkey':'',
    'f':'',
}
# 使用session进行post请求的发送
response = session.post(url=login_url, headers=headers, data=data)
print(response.status_code)

# 爬取当前用户个人详情页的信息
detail_url = ''
# 使用携带cookie的session进行get请求的发送
detail_page_text = session.get(url=detail_url, headers=headers).text
# # 手动cookie处理
# headers = {
#     'Cookie':''
# }
with open('./gerenxinxi.html', 'w', encoding='utf-8') as f:
    f.write(detail_page_text)





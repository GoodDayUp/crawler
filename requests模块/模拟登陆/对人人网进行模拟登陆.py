import requests
from lxml import etree
import YDMHttp

'''
点击登录之后会发起一个post请求，该请求会携带相关的登录信息（用户名、密码、验证码等）
验证码：动态，每次请求会发生变化
'''

# 封装识别验证码图片的函数
def getcodeText(imgPath, codeType):
    # 云打码平台普通用户用户名和密码
    username = ''
    password = ''

    # 软件ID和软件密钥，开发者分成必要参数，登录开发者后台【我的软件】获得
    appid = 6003
    appkey = ''

    # 图片文件：被识别的验证码路径
    filename = imgPath

    # 验证码类型
    codetype = codeType

    # 超时时间
    timeout = 20  # s
    result = 0
    # 检查
    if username == 'username':
        print('请设置好相关参数在测试')
    else:
        # 初始化
        yundama = YDMHttp(username, password, appid, appkey)

        # 登录云打码
        uid = yundama.login()
        print('uid: %s' % uid)

        # 查询余额
        balance = yundama.balance()
        print('balance: %s' % balance)

        # 开始识别，图片路径，验证码类型id，超时时间，识别结果
        cid, result = yundama.decode(filename, codeType, timeout)
        print('cid:%s, result:%s' % (cid, result))
    return result



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
response = requests.post(url=login_url, headers=headers, data=data)
print(response.status_code)

# login_page_text = response.text
# with open('./renren.html', 'w', encoding='utf-8') as f:
#     f.write(login_page_text)





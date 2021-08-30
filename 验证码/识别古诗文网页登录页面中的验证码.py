
import requests
from lxml import etree
import YDMHttp

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

# 将验证码图片下载到本地
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
page_text = requests.get(url=url, headers=headers).text

# 解析验证码图片img中src属性值
tree = etree.HTML(page_text)
code_img_src = 'https://so.gushiwen.org' + tree.xpath('//*[@id="imgCode"]/@src')
img_data = requests.get(url=code_img_src, headers=headers).content
# 将验证码图片保存到了本地
with open('./code.jpg', 'wb') as f:
    f.write(img_data)

# 通用打码平台的示例程序进行验证码图片数据识别
code_text = getcodeText('code.jpg', 1004)  #  1004:4位字母数字
print(code_text)





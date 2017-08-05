from http import cookiejar
from urllib import request, parse
from PIL import Image
import requests
import json

username = input('Please Input ID: ')
password = input('Please Input password: ')

postUrl = 'http://ssfw1.hlju.edu.cn/ssfw/j_spring_ids_security_check'
openUrl = 'http://ssfw1.hlju.edu.cn/ssfw/login/ajaxlogin.do'
captchaUrl = 'http://ssfw1.hlju.edu.cn/ssfw/jwcaptcha.do'

cookie = cookiejar.CookieJar()
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)

picture = opener.open(captchaUrl).read()

local = open('image.jpg', 'wb')
local.write(picture)
local.close()

print(Image.open('image.jpg', 'r').show())
validateCode = input('Please Input validateCode: ')

postData = {
    'j_username': username,
    'j_password': password,
    'validateCode': validateCode
}

haeders = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,en-US;q=0.8,en;q=0.6,zh-TW;q=0.4,zh;q=0.2',
    'Connection': 'keep-alive',
    'Content-Length': '57',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data = parse.urlencode(postData).encode('utf-8')

# requestC = request.Request(postUrl, data, haeders)
# responseC = opener.open(requestC)

r = requests.get(postUrl, headers=haeders)
print(r.content)
print(r.headers)
if r.status_code == requests.codes.ok:
    for k, v in r.json().items():
        print(k, v)
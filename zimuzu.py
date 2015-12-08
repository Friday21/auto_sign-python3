# author: Friday
import urllib.request
import http.cookiejar
import urllib.parse
import gzip
import time
import json


def ungzip(data):
    try:        # unzip data
        print('正在解压.....')
        data = gzip.decompress(data)
        print('解压完毕!')
    except:
        print('未经压缩, 无需解压')
    return data


def getOpener(head):
    # deal with the Cookies
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def sign(username, password):
    url = 'http://www.zimuzu.tv/'
    header = {
        'Accept': 'application/json, text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.73'
                      ' Safari/537.36',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3'
    }
    opener = getOpener(header)
    try:
        op = opener.open(url)
    except:
        print("Can't open 'http://www.zimuzu.tv', please check your connection")
        return False
    url += 'User/Login/ajaxLogin'
    postDict = {
        'account': id,
        'password': password,
        'remember': 1,
        'url_back': 'http://www.zimuzu.tv/'
    }
    postData = urllib.parse.urlencode(postDict).encode()
    op = opener.open(url, postData)
    data = op.read()
    data = ungzip(data)
    data = json.loads(data.decode('utf-8'))
    if data['status'] != 1:
        print('wrong username or password, login error')
        return False
    url = 'http://www.zimuzu.tv/user/sign'
    op = opener.open(url)
    data = op.read()
    time.sleep(20)
    url = 'http://www.zimuzu.tv/user/sign/dosign'
    op = opener.open(url)
    data = op.read()
    data = ungzip(data)
    data = json.loads(data.decode('utf-8'))
    if data['status'] == 0:
        print('sign error, maybe you have already signed today')
        return False
    if data['status'] == 1:
        return True

if __name__ == '__main__':
    if sign('your_username', 'your_password'):
        print('sign success')

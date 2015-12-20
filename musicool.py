import http.cookiejar
import gzip
import random
import urllib
from urllib.request import urlopen
import re


def ungzip(data):
    try:        # unzip data
        data = gzip.decompress(data)
    except:
        pass
    return data


# head: dict of header
cj = http.cookiejar.CookieJar()


def make_my_opener(head=None):
    if not head:
        head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Cookie': '此处改为自己登录后的cookie'
        }
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def sign_and_comment():
    oper = make_my_opener()
    op = oper.open('http://bbs.musicool.cn/', timeout=1000)
    op = oper.open('http://bbs.musicool.cn/forum-14-1.html', timeout=1000)
    data = op.read()
    data = ungzip(data)
    data = data.decode('gbk')
    num = re.findall(r'"http://bbs.musicool.cn/thread-(.{1,10})-1-1.html".{1,100}每日幸运数0----9', data)
    url = 'http://bbs.musicool.cn/forum.php?mod=post&action=reply&fid=14&tid='+str(num[0])+'&extra=page%3D1&replysubmit=yes&i' \
          'nfloat=yes&handlekey=fastpost&inajax=1'
    postDict = {
        'message': '%s            %s' % (random.randint(0, 9), random.randint(0, 9)),
        'posttime': '1505507639',
        'formhash': 'b3680929'
    }
    postData = urllib.parse.urlencode(postDict).encode()
    op = oper.open(url, postData, timeout=1000)
    data = op.read()
    data = ungzip(data)
    data = data.decode('gbk')
    if re.findall(r'非常感谢', data):
        print('回复成功')
        return True
if __name__ == '__main__':
    if sign_and_comment():
        pass
    else:
        print('自动登录或回复失败，请检查cookie重试')

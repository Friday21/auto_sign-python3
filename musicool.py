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
    'Cookie': 'Iy5o_c91e_saltkey=k11GB8kS; Iy5o_c91e_lastvisit=1450306120; Iy5o_c91e_auth=e35dpA%2FCKdQLUUiHfy6961JZAeI'
              'i0WmnI7omB0lfevlTvTHj8HUOKgxg0MUxAqqBqZUnajQ4x3yFD5Xj9yk8JjHlqenm; Iy5o_c91e_visitedfid=14; Iy5o_c91e_'
              'forum_lastvisit=D_14_1450309822; Iy5o_c91e_smile=1D1; Iy5o_c91e_onlineusernum=2688; Iy5o_c91e_sid=49z9zV;'
              ' Iy5o_c91e_ulastactivity=e30e7eepY37dOV9LY2sYTQkx3SteHw90NcUybzG0waWs4boX8Cbv; Iy5o_c91e_checkpm=1; Iy5o_'
              'c91e_lastact=1450397120%09home.php%09misc; Iy5o_c91e_sendmail=1; CNZZDATA2690073=cnzz_eid%3D1324583947-14'
              '42270967-http%253A%252F%252Fbbs.musicool.cn%252F%26ntime%3D1450392407'
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
    url = 'http://bbs.musicool.cn/forum.php?mod=post&action=reply&fid=14&tid=598441&extra=page%3D1&replysubmit=yes&i' \
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

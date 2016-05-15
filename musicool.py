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
    'Cookie': 'Iy5o_c91e_smile=1D1; Iy5o_c91e_saltkey=MaQGIAeq; Iy5o_c91e_lastvisit=1463318267; '
              'Iy5o_c91e_seccodeSAqY6c2Z0=e14c1cJJHR%2Fs3FzUk3TCh7zcGc2qYfCtP9LOMTfkwIjzWy4l%2BMDKL%'
              '2Fq6%2FP%2BJdqX7JhGbLhGvz87l8oguEjhp; Iy5o_c91e_auth=986fHta0EPO20d1kIFcEEFyjjM9tuWodzt6'
              'EG%2BVXT0x%2BmIENrwZ8yVyyPhmFUmQm0TtFTrgoDBYKK%2B7aba7wrKDdkH3L; '
              'Iy5o_c91e_onlineusernum=4590; Iy5o_c91e_sid=JbzD1T; Iy5o_c91e_ulastactivity=e794PzdvIEZnkEMzctrj'
              'y3dCsbV0guAYkTgbYmpAtOa5fM1coqP9; Iy5o_c91e_sendmail=1; Iy5o_c91e_checkpm=1; CNZZDATA2690073=cnz'
              'z_eid%3D1142367028-1447427636-http%253A%252F%252Fbbs.musicool.cn%252F%26ntime%3D1463317565; Iy5o'
              '_c91e_lastact=1463321886%09home.php%09spacecp'}
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def sign_and_comment():
    oper = make_my_opener()
    try:
        op = oper.open('http://bbs.musicool.cn/', timeout=1000)
        op = oper.open('http://bbs.musicool.cn/forum-14-1.html', timeout=1000)
    except:
        return False
    data = op.read()
    data = ungzip(data)
    data = data.decode('gbk')
    num = re.findall(r'"http://bbs.musicool.cn/thread-(.{1,10})-1-1.html".{1,100}每日幸运数0----9', data)
    url = 'http://bbs.musicool.cn/forum.php?mod=post&action=reply&fid=14&tid='+str(num[0])+'&extra=page%3D1&replysubmit=yes&i' \
          'nfloat=yes&handlekey=fastpost&inajax=1'
    postDict = {
        'message': '%s            %s' % (random.randint(0, 9), random.randint(0, 9)),
        'posttime': '1505507639',
        'formhash': '9a5ec7fa'
    }
    postData = urllib.parse.urlencode(postDict).encode()
    try:
        op = oper.open(url, postData, timeout=1000)
        data = op.read()
        data = ungzip(data)
        data = data.decode('gbk')
    except:
        return False
    if re.findall(r'非常感谢', data):
        print('回复成功')
        return True
if __name__ == '__main__':
    for i in range(6):
        if sign_and_comment():
           break

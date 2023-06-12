import requests
import re
import base64
import inspect

class SubDomain:
    def __init__(self, url):
        self.url = url
        self.subs_filtered = []
        self.subs_filtered_domain = []
        self.ports = []
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36',
            'Referer': 'http://www.baidu.com/',
            }
        self.subs = self.get_all()
    # ip138接口
    def ip138(self):
        print('[+] 正在使用 ' + inspect.stack()[0][3] + ' 接口')
        res = requests.get('http://site.ip138.com/{}/domain.htm'.format(self.url), headers=self.headers)
        p = re.compile(r'target="_blank">(.*?)</a></p>')
        sub = p.findall(res.text)
        # print(res.text)
        if (len(sub) == 0):
            print('[+] ip138接口可能出现问题!')
        print('[+] ' + inspect.stack()[0][3] + ' 接口查询完毕: 共 ' + str(len(sub)) + ' 条')
        return sub

    # fofa api，要钱的
    def fofa_api(self):
        print('[+] 正在使用 ' + inspect.stack()[0][3] + ' 接口')
        email = 'jcbafs21sx@protonmail.com'
        key = '2c088d5276e9f7bba23c50d392bc6079'
        size = 10000
        s = 'domain=\"{}\"'.format(self.url)
        s = base64.b64encode(s.encode('utf-8')).decode()
        res = requests.get('https://fofa.so/api/v1/search/all?email={}&key={}&qbase64={}&size={}'.format(email, key, s, size))
        res = res.json()
        if "error" in res and res["error"] == True:
            print(res)
            print('[+] fofa api可能出现问题!')
            return res["errmsg"]
        else:
            return res

    # 汇总并去重
    def get_all(self):
        subs = []
        sub = self.ip138()
        subs.extend(sub)
        sub = self.fofa_api()
        subs.extend(sub)
        # 去重
        subs = list(set(subs))
        print('[+] 去重完毕: 共 ' + str(len(subs)) + ' 条')
        return subs

    # save the results



if __name__ == '__main__':
     domain='hupu.com'
     SubDomain(domain)
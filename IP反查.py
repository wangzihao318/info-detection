# Mr wang
import requests
import re
import sys

def ip138(url):
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    re_ip = re.search(r"([0-9]{1,3}\.){3}[0-9]{1,3}",url)
    if re_ip:
        target = re_ip.group()
        api = "http://site.ip138.com/%s/" % target
    try:
        req = requests.get(api,headers=headers,timeout=10)
        html = req.text
        re_domains = re.findall(r"</span><a href=\"/(.*?)/\"",html)
        returnlist = re_domains
    except Exception as e:
        returnlist=[]
    return returnlist
if __name__ == '__main__':
    print(ip138('104.31.70.89'))
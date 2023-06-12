# Mr wang
import json
import  socket
import  requests
def get_ip(domain):
   try:
        ip=socket.gethostbyname(domain)
        print(ip)
   except:
        ip=None
   return  ip

def  get_ip_location(ip):
    try:
        url=f'http://ip-api.com/json/{ip}'
        r=requests.get(url)
        result=json.loads(r.text)
        data={
        'country':result['country'],
        'regionName' : result['regionName'],
        'city' : result['city']}
        print(data)
    except:
        data=[]
if __name__ == '__main__':
    ip=get_ip('www.4438x6.com')
    ip_location=get_ip_location(ip)

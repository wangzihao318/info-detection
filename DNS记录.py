from  gevent import  monkey

from dns import  *

def singleQuery(domain):
    data={}
    try:
        answer = resolver.resolve(domain)
        data['ttl']=answer.rrset.ttl
    except Exception as e:
        print(e)
        return None
    try:
        count=0
        A_list = []
        answer = resolver.resolve(domain, 'A')
        for i in answer:
            count+=1
        data['A']=count
    except Exception as e:
        print(e)
        data['A'] =None

    try:
        answer = resolver.resolve(domain, 'CNAME')
        count=0
        for i in answer:
            count+=count
        data['cname'] = count
    except Exception as e:
        print(e)
        data['cname_count'] = None


if __name__ == '__main__':
    domain=input('domain')
    data=singleQuery(domain)
    print(data)




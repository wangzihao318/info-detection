# Mr wang
import json
import asyncio
import dns.resolver
import os

loop = asyncio.get_event_loop()
class get_cdn(object):
    def __init__(self,target):
        self.target=target
        self.records=[]
        self.ip_result=[]
        self.cname_result=[]


    async def query(self,dnsserver):
        try:
            Resolver=dns.resolver.Resolver()
            Resolver.lifetime = Resolver.timeout = 2.0
            Resolver.nameservers = dnsserver
            record = Resolver.resolve(self.target, "A")
            self.records.append(record)
        except Exception as e:
            print(e)
    def check_cdn(self):
        dnsserver = [['114.114.114.114'], ['8.8.8.8'], ['223.6.6.6'],['1.2.4.8'],['208.67.222.222']]
        try:
            for i in dnsserver:
                loop.run_until_complete(self.query(i))
            for record in self.records:
                for m in record.response.answer:
                    for j in m.items:
                        if isinstance(j,dns.rdtypes.IN.A.A):
                            self.ip_result.append(j.address)
                        elif isinstance(j,dns.rdtypes.ANY.CNAME.CNAME):
                            self.cname_result.append(j.to_text())
        except Exception as e:
            print(e)




    def getrules(self):
        path=os.getcwd()
        rules_path=path+'/cdnrules'
        with open(f'{rules_path}/cname',encoding='utf-8') as f :
             cname_rules=json.load(f)
             f.close()
        return  cname_rules

    def run(self):
        cdn_flag=0
        self.check_cdn()
        if len(list(set(self.ip_result))) > 1:
            cdn_flag=1

        if cdn_flag==1:
           cdn_name='Unknow'
           cname_rules=self.getrules()
           for i in self.cname_result:
                domain_spilt=i.split('.')
                cdn_domain='.'.join(domain_spilt[-3:])[:-1]
                if cdn_domain in cname_rules.keys():
                   cdn_name=cname_rules[cdn_domain]['name']
                   break
        else:
            cdn_name='no cdn'
        return  cdn_name
if __name__ == '__main__':
    target='www.hupu.com'
    name=get_cdn(target).run()
    print(name)

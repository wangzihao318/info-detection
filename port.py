import re
import socket
import nmap

def PortScan(host):
    pattern = re.compile('^\d+\.\d+\.\d+\.\d+(:(\d+))?$')
    content = ""
    if not pattern.findall(host):
        host = socket.gethostbyname(host)
        print(host)
    if pattern.findall(host) and ":" in host:
        host=host.split(":")[0]
    nm = nmap.PortScanner()
    try:
        nm.scan(host, arguments='-Pn -A -sV --open -T3 -n --host-timeout=60s --min-rate=1000')
        for proto in nm[host].all_protocols():
            lport = list(nm[host][proto].keys())
            for port in lport:
                if nm[host][proto][port]['state'] == "open":
                    print(nm[host][proto][port])
                    service = nm[host][proto][port]['product']
                    version = nm[host][proto][port]['version']
                    system=nm[host][proto][port]['cpe']
                    content += '[*]主机' + host + ' 协议：' + proto + '\t开放端口号：' + str(port) + '\t端口服务：' + service + '\t版本：' + version + '\t系统'+system+'\n'
        return content
    except Exception as e:
        print(e)

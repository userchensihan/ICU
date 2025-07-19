from scapy.all import *
c=conf.route.route("0.0.0.0")[2]
p=Ether(dst="ff:ff:ff:ff:ff:ff",src="EC:91:61:89:9F:EF")/ARP(pdst=c)
a=srp(p,verbose=0)
for i in a[0].res:
    b=i.answer
    print(b.src)

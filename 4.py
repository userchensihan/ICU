from bluetooth import *
if __name__=="__main__":
    while True:
        try:
            a=discover_devices(lookup_names=True)
            if a:
                b=a[0][0]
                print(b)
                s=find_service(address=b)
                if s:
                    for x in s:
                        k=x['port'] 
                        print(k)
                        c=BluetoothSocket(RFCOMM)
                        c.connect((b,k))
                        c.close()
        except btcommon.BluetoothError:
            continue
"""
import nmap
l=nmap.PortScanner()
l.scan('192.168.0.1/24','445')
d=[]
for y in l.all_hosts():
    if l[y]['tcp'][445]['state']!='closed':
        d.append(y)
print(d)
"""

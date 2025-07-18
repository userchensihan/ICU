import pywifi
import time
print('导入库')
a=pywifi.PyWiFi()
print('定义无线对象')
c=a.interfaces()
if c:
    c=c[0]
    print('定义接口对象')
c.scan()
print('扫描中')
time.sleep(6)
print('扫描后')
for s in c.scan_results():
    if s.ssid=="CMCC-ta9Z":
        print('ESSID为"CMCC-ta9Z"的网络')
        print('信道:'+str((int(s.freq)-2412)/5+1))


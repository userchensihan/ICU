import socket
import fcntl
import struct
print('导入库')
try:
    s=None
    s=socket.socket()
    print('创建套接字')
    r=struct.pack(
        '16sH',
        'wlan0'.encode('utf-8').ljust(16,b'\0'),
        6
    )
    print('已定义iwreq结构体.网卡wlan0')
    fcntl.ioctl(s.fileno(),0x8B06,r)
    print('网卡模式:监控')
except IOError as e:
    print("NetworkManager或wpa_supplicant正在运行.或网卡状态为'下'")

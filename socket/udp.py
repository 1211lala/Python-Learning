"""
学习视频
    https://www.bilibili.com/video/BV1NQ4y1i7VX?p=5&vd_source=582815cfc933bf06a04f3f29f43d7977


实验现象
    建立一个udp接收端,可以通过udp软件连接本机服务端

"""
import socket
from get_ip import get_local_ip

listen_ip = get_local_ip()
listten_port = 10001
print(f"开启{listen_ip, listten_port}的监听")

#创建socket对象 
# SOCK_DGRAM 是套接字(socket)类型的一种，
# 表示该套接字使用的是 UDP（User Datagram Protocol）协议
server_socket  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#创建监听
server_socket.bind((listen_ip, listten_port))

while True:
    
    # recvfrom 用于从未连接的套接字接收数据
    data, addr = server_socket.recvfrom(1024)
    print(f"来自{addr}的连接, 请求的信息为{data.decode()}")
    
    # 可以在这里添加处理逻辑，然后发送响应给客户端
    response = "Hello, client!"
    server_socket.sendto(response.encode("utf-8"), addr)
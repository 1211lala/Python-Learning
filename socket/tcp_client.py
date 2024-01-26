"""
学习视频
    https://www.bilibili.com/video/BV1NQ4y1i7VX?p=3&vd_source=582815cfc933bf06a04f3f29f43d7977


实验现象
    使用tcp通信发送一个http请求, 并获得服务器返回数据并打印
    
    
#创建对象 --> 绑定地址 --> 设置监听 --> 等待链接


"""

import socket


def get_local_ip():
    try:
        # 获取主机名
        host_name = socket.gethostname()
        
        # 通过主机名获取 IP 地址
        local_ip = socket.gethostbyname(host_name)
        
        return local_ip
    except Exception as e:
        print(f"Error: {e}")


connect_ip = get_local_ip()
connect_port = 10003

#创建socket对象 11
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#连接远端
client.connect((connect_ip, connect_port))

while True:
    sendDate = input("请输入发送给服务器端的数据:")
    client.send(sendDate.encode("utf-8"))
    # client.close()
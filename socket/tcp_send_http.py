"""
学习视频
    https://www.bilibili.com/video/BV1NQ4y1i7VX/?p=2&vd_source=582815cfc933bf06a04f3f29f43d7977


实验现象
    使用tcp通信发送一个http请求, 并获得服务器返回数据并打印
    
    
#创建对象 --> 建立连接 --> 发送数据 -->等待数据
"""

import socket

url = "www.pyqt5.cn"
port = 80


#创建对象
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#建立连接(一次性连接)
sk.connect((url, port))

#发送请求
sk.send(b"GET / HTTP/1.1\r\nHost: " + url.encode("utf-8") +b"\r\nConnection: close\r\n\r\n")

#等待数据
rec_list = []
while True:
    rec = sk.recv(1024)
    if rec:
        rec_list.append(rec)
    else:
        break

#转换编码并打印
rec_str = (b"".join(rec_list)).decode("utf-8")
print(rec_str)
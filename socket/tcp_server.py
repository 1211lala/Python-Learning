"""
学习视频
    https://www.bilibili.com/video/BV1NQ4y1i7VX?p=3&vd_source=582815cfc933bf06a04f3f29f43d7977


实验现象
    使用tcp通信发送一个http请求, 并获得服务器返回数据并打印
    
    
#创建对象 --> 绑定地址 --> 设置监听 --> 等待链接


"""
import socket

#获取主机IP
def get_local_ip():
    try:
        # 获取主机名
        host_name = socket.gethostname()
        
        # 通过主机名获取 IP 地址
        local_ip = socket.gethostbyname(host_name)
        
        return local_ip
    except Exception as e:
        print(f"Error: {e}")

#tcp_server端口
server_port = 10003
#tcp_server地址
server_ip = get_local_ip()


print("服务器ip :%s 端口 %d 已开启服务！" %(server_ip, server_port))
# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
server_socket.bind((server_ip, server_port))

# 开始监听，允许最多 5 个连接
server_socket.listen(5)


while True:
    # 等待客户端连接
    client_socket, client_address = server_socket.accept()
    print(f"客户端{client_address}已连接")
    
    # 向客户端发送欢迎消息
    welcome_message = f"Hello, client! this is{(server_ip, server_port)}"
    client_socket.send(welcome_message.encode("utf-8"))

    # 循环接收客户端消息
    while True:
        data = client_socket.recv(1024)
        
        if data == b"":
            break  # 客户端关闭连接，跳出内层循环

        print(f"收到客户端{client_address}的信息: {data.decode('utf-8')}")

    # 连接断开后打印信息
    client_socket.close()
    print(f"已断开与{client_address}的连接.")
    





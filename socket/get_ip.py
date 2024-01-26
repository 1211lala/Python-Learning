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
        

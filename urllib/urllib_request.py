'''
urllib.request  发布请求
urllib.parse    解析数据
urllib.error    异常处理模块
'''
'''
HTTPResponse的
属性
    code:       返回 HTTP 响应的状态码。
    msg:        返回 HTTP 响应的状态消息。
    url:        返回请求的 URL。
    headers:    返回响应头的 http.client.HTTPMessage 对象。   
    length:     返回响应内容的长度（以字节为单位）
    version:    返回 HTTP 版本号。
    reason:     返回 HTTP 响应的状态消息。
    chunked:    如果响应是分块传输编码，则返回 True。
方法
    read(size=-1):      读取指定大小的响应内容，如果未指定大小或大小为负数，则读取整个响应。
    readline(size=-1):  读取一行响应内容，如果未指定大小或大小为负数，则读取整行。
    readlines(hint=-1): 读取多行响应内容，返回一个列表，每个元素是一行。
    getheader(name, default=None): 返回指定头的值，如果不存在则返回默认值
    getheaders():       返回响应头的列表。
    
    
    
    
def urlopen(url, data=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT, *, cafile=None, capath=None, cadefault=False, context=None):
    url: 请求地址
    data:发送请求时携带的参数(bytes),一但携带参数就是post请求
    timeout 连接超时时间 单位s 请求不成功将引发 timeout 异常。
    cafile (str, optional): 指定 CA 证书文件的路径，用于验证服务器证书。
    capath (str, optional): 指定 CA 证书目录的路径，用于验证服务器证书。
    cadefault (bool, optional): 如果设置为 True,将使用系统默认的 CA 证书存储库进行验证。
    context (SSLContext, optional): 如果提供了 context,它应该是一个 SSL 上下文对象，用于自定义 SSL 验证。
    
    返回一个http.client.HTTPResponse 或 http.client.HTTPSResponse 
'''

#!/usr/bin/env python3
import urllib.request
import json

# 嵌入式防火门网页
url = "http://192.168.8.70/get_firedoor_data"

res  = urllib.request.urlopen(url)

print("响应的状态码     %s" % res.code)
print("响应的状态消息   %s" % res.msg)
print("返回请求的       %s" % res.url)
print("响应内容的长度   %d" % res.length)
print("HTTP版本号       %s" % res.version)
print("头部信息:\r\n %s" % res.headers)

json_str = res.read().decode()
print(json_str)
dict_ = json.loads(json_str)
print(dict_["data"]["state"])
print(dict_["data"]["angle"])
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
'''*****************************通过urllib.request模块请求自动门信息并设置自动门开关状态*******************************'''

# import urllib.request
# import json
# import urllib.parse

# ip = "192.168.8.83:8080"

# # # 不带参数的url GET 请求自动门信息
# # url = "http://"+ ip +"/get_firedoor_data"
# # res  = urllib.request.urlopen(url)

# # print("响应的状态码     %s" % res.code)
# # print("响应的状态消息   %s" % res.msg)
# # print("返回请求的       %s" % res.url)
# # print("响应内容的长度   %d" % res.length)
# # print("HTTP版本号       %s" % res.version)
# # print("头部信息:\r\n %s" % res.headers)

# # json_str = res.read().decode()
# # print(json_str)
# # dict_ = json.loads(json_str)
# # print("code : %d" % dict_["code"])
# # print("msg : %s" % dict_["msg"])
# # print("防火门状态 : %d [False:关闭   True:开启]" % dict_["data"]["state"])
# # print("防火门角度 : %d [未使用,保留]" % dict_["data"]["angle"])



# # # 带参数的url请求，设置自动门状态
# # url = "http://"+ ip +"/set_firedoor_data"

# # params = {"angle":0}
# # params["state"] = 1

# # data = urllib.parse.urlencode(params).encode("utf-8")

# # res  = urllib.request.urlopen(url, data=data)

# # json_str = res.read().decode()
# # print(json_str)
# # dict_ = json.loads(json_str)
# # print("code : %d" % dict_["code"])
# # print("msg : %s" % dict_["msg"])
'''**************************************************************************************************************'''





'''***************************通过urllib.request.urlretrieve()函数将请求返回的数据保存在本地************************'''
# import os
# import urllib.request


# # url = "http://www.pyqt5.cn/static/images/logo.jpg"
# # file_name = "picture.jpg"

# # url = "http://192.168.8.70"
# # file_name = "home.html"

# url ="https://vod.v.jstv.com/2024/01/25/JSTV_JSGGNEW_1706182874473_NBn3baX_1928.mp4"
# file_name = "sp.mp4"

# # 失败
# # url = "https://www.bilibili.com/video/BV1se411Y7FU/?spm_id_from=333.1007.tianma.2-1-3.click"
# # file_name = "bili.mp4"

# # 获取当前脚本所在的目录
# script_dir = os.path.dirname(os.path.abspath(__file__))
# # 构建文件夹的相对路径
# folder_path = os.path.join(script_dir, "files")
# # 判断文件夹是否存在
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
# # 构建下载文件的存储路径
# file_path = os.path.join(folder_path, file_name)

# print(file_path)
# urllib.request.urlretrieve(url, filename=file_path)
'''**************************************************************************************************************'''




'''******************************************通过urllib.request模块访问天气网站***********************************'''
# # 天气网站 https://tianqiapi.com/index/doc?version=v61

# import urllib.request
# import json


# url = "http://v1.yiketianqi.com/api?unescape=1&version=v61&appid=88344185&appsecret=58ixdwXt"

# res = urllib.request.urlopen(url)

# res_str = res.read().decode()

# res_dict = json.loads(res_str)

# print(res_dict)
# print("cityid :%s" % res_dict["cityid"])
# print("date : %s:%s" % (res_dict["date"], res_dict["update_time"]))
# print("week : %s" % (res_dict["week"]))
# print("area : %s:%s" % (res_dict["country"], res_dict["city"]))
# print("wea_day: %s" % res_dict["wea_day"])
# print("wea_night: %s"% res_dict["wea_night"])
# print("temp_max : %s" % res_dict["tem1"])
# print("temp_min : %s" % res_dict["tem2"])
# print("win : %s" % res_dict["win"])
# print("win_speed : %s" % res_dict["win_speed"])
# print("win_meter : %s" % res_dict["win_meter"])
# print("air : %s" % res_dict["air"])
# print("air_pm25 : %s" % res_dict["air_pm25"])
# print("air_level : %s" % res_dict["air_level"])
# print("sunrise : %s" % res_dict["sunrise"])
# print("sunset : %s" % res_dict["sunset"])
# print("air_tips : %s" % res_dict["air_tips"])

'''**************************************************************************************************************'''


'''******************************************通过urllib.request模块更改请求头**************************************'''
# from urllib import request


# url = "https://www.baidu.com/"

# header = {
#     #更改请求头信息,可以先用浏览器查看请求头信息
    
#     # HTTP 头部中的一个字段,关于用户代理的信息，使服务器能够适当地响应请求。
#     "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36",
#     # HTTP 头部中的一个字段,告诉服务器用户首选的语言，以便服务器返回相应语言版本的内容。
#     'Accept-Language': 'zh-CN,zh;q=0.9',
# }

# # 构建request对象
# req = request.Request(url, headers=header)
# # request.urlopen()的参数可以是一个url也可以是一个request.Request对象
# res = request.urlopen(req)
# res_str = res.read().decode()
# print(res_str)
'''**************************************************************************************************************'''
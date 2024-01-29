'''

文件读写过程  打开 --> 读写、定位 --> 关闭

w : 写，没有文件自动创造文件，文件指针放在文件的开头
r : 读，文件指针放在文件的开头
a : 添，没有文件自动创造文件，文件指针放在文件的结尾

wb 二进制
rb 二进制
ab 二进制

w+
r+
a+



'''

import json

path = "./os/cfg.json"

msg = {"ssid":"Kean"}
msg["pwd"] = "Kean.2023"
msg["ip"] = "192.168.8.10"
msg["gateway"] = "192.168.8.1"
msg["subney"] = "255.255.255.0"

#写入数据
f = open(path, "w",encoding="utf-8")
json_msg = json.dumps(msg)
f = open(path, "w", encoding="utf-8")
print("写入%d个字节" % f.write(json_msg))
f.close()

#读出数据
f = open(path, "r",encoding="utf-8")
json_msg = f.read()
msg = json.loads(json_msg)
print("读出")
print(msg)


#添加
# f = open(path, "a")
# f.write("这是添加的内容")
# f.close()

# 文件函数
# x = f.tell()  返回当前光标位置
# f.seek(x)     设置光标位置




"""
字典

"""
#赋值
zd1 = {"name":"dgs", "age":13, "height": 178}
zd1["weight"] = 120
#赋值
zd2 = dict(name = "DGS", age = 13, height = 187)
#修改
zd1.update(name = "liuao", age = 70)
#读取
print(zd1["name"])
print(zd1.get("name", "找不到查找的参数返回这个值"))
zd1.setdefault("male", "nan")

keys = zd1.keys()
values = zd1.values()
items = zd1.items()
for i in values:
    print(i)


#删除 如果没有这个值会报错，可以设置一个默认内容
zd1.pop("height", None)
del zd1["weight"]
print(zd1)
zd1.clear()

print(zd1)

print(type(zd1))




#嵌套

zd3 = {"地区":{"海南":38,"湖南":40,"淮南":30}, "时间": "2024-8-8-12:12:12"}
zd4 = {"地区":["海南","湖南","淮南"], "时间": "2024-8-8-12:12:12"}
print(zd3["地区"]["海南"])
print(zd4["地区"][1])
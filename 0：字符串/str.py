"""
字符串
    str.center(count) 居中输出
    str.rjust(count) 右对齐
    str.ljust(count) 左对齐
    str.zfill(count) 
"""

#查找字符出现的个数
str1 = "大海啊，你全是水！"
print(str1.count("海"))
print(str1.find("海"))
str2 = "骏马啊，你有四条腿！"
str3 = "美人啊，你有大大的眼睛，还有一张嘴！"

print(str1.join([str2, str3]))


#格式化字符串
print("1+2 = {}   2*2 = {} {},".format(1+2, 2*2, "this is format"))
print("1+2 = {2}   2*2 = {1} {0},".format(1+2, 2*2, "this is format"))
print("{0:^20}".format("this is format"))
print("{0:>20}".format("this is format"))
print("{0:<20}".format("this is format"))
# .xf 显示小数几位
# .xg 显示一共几位
# . 显示多长的数据
# .% 显示百分比
print("{:.3f}".format(3.1425))
print("{:.3g}".format(3.1425))
print("{:.2%}".format(0.1425))
print("{:.3}".format("hellloees"))
# 'b' 二进制显示
# 'c'
# 'd'
# 'o'
# 'X'
# 'x'
# 'n'
print("{:#b}".format(80))
print("{:c}".format(80))
print("{:d}".format(80))
print("{:#o}".format(80))
print("{:#X}".format(80))

print("当前关键字为{:.{prec}f}".format(80, prec = 2))

year = 3.1415926
print(f"PI值为{year}")
print(f"PI值为%d" % 2010)
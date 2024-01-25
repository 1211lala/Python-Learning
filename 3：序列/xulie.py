"""
对象的三个基本属性
    唯一标志 id 可以使用 is函数判断
    值
    类型

序列运算符
    +
    *
    is()
    in()
    del()删除对象或者可变序列里的元素
序列函数
    将一个可迭代对象转换成列表 list(对象)
    将一个可迭代对象转换成元组 tuple(对象)
    将一个可迭代对象转换成字符串 str(对象)
    找到一个可迭代对象中的最大值 max(对象)
    找到一个可迭代对象中的最小值 min(对象)
    计算可迭代对象的和 sum(对象)
    排序可迭代对象      sorted(对象) 返回的是一个全新的列表，之前的列表不会受影响
                    reverse(对象)返回的是一个全新的列表，之前的列表不会受影响
                    str.sort()  会改变列表的顺序
                    参数 reverse = True
                        key = 函数名
    all()
    any()
    enumerate() 为一个可迭代对象创造一个枚举
    map() 返回一个迭代器
"""

list1 = [i for i in range(5)]
list2 = [i for i in range(5,10)]
print(list1 + list2)
print(list1 * 3)

temp = "Kean"
print(list(temp))
print(tuple(temp))

temp = [1,2,3,4,5]
temp_str = str(temp)
for i in temp_str:
    print(i)

#map函数
list1 = ["1212", "aaaa", "KE"]
mapped = map(len, list1)
print(list(mapped))



"""
集合 -- 无序  不能存储列表
唯一性
"""

jh1 = {"1",433}

if "1" in jh1:
    print("%s在集合中" % "aaaaa" )


#插入
jh1.update([1,2,3,3],{"hel","lo"})
jh1.add("world")
print(jh1)

#删除

jh1.remove("world") #如果没有这个元素会报错
jh1.discard("hel") 
jh1.clear() 
print(jh1.pop()) #随机删除一个
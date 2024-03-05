"""
列表可以容纳不同类型的数据

在列表末尾中添加数据 
    append(添加的数据)  == list[len(list):] = 添加的数据
    extend(添加的数据(必须是可迭代对象)) == list[lem(list):] = 添加的数据
    insert(位置，插入的元素)
删除数据 
    remove(需要删除的元素，存在多个一样的数据，会删除第一个)
    pop(位置)
    clear() 删除所有元素
排序 
    sort() 默认从小到大排序
    sort(reverse=True) 默认从大到小排序

查找元素 
    list.index(产找的)

"""
list = [1,3,4,"aaaa",14577, 1.04564]


print(list[0::1])
print(list[:3])
print(list[3:])
print(list[:])
print(list[::-1])




#内置排序算法
list = [6,7,43,78,100,2]
list.sort()
print(list)
list = [6,7,43,78,100,2]
list.sort(reverse=True)
print(list)




#二维列表
#正确赋值
A = [1]*3
for i in range(3):
    A[i] = [0] *3
print(A)
#错误赋值
B = [[0]*3] *3 #外面的*3的内存地址是一样的
print(A[1] is A[0])
print(B[1] is B[0])


matirx = [[1,2,3],[4,5,6],[7,8,9]]
print(matirx[1])
# for i in matirx:
#     for j in i:
#         print(j)
for i in matirx:
    for j in range(len(i)):
        print(i[j])






#列表的浅拷贝 list.copy & 切片  copy.copy() 对于二维数值不能处理，需要深拷贝
#      深拷贝 copy.deepcopy()
import copy

xx = 11
yy = xx
xx = 99
print(yy)

list4 = [1, 2, 3]
list5 = list4
# list5 = list4.copy
# list5 = list4[::]
list5[1] = 99
print(list4)




#列表的加法
s1 = [i for i in range(0, 4)]
s2 = [i for i in range(4, 7)]
s = s1 + s2
print(s)




#列表推导式
lie = [1,2,3,4,5]
lie = [i *2 for i in lie]
# for i in range(len(lie)):
#     lie[i] = lie[i] * 2
print(lie)

lie1 = [ord(i) for i in "Kean.2023" if i == 'K']
print(lie1)










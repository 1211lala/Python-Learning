"""
私有变量
    没有私有变量
类似私有变量 使用 s.__x 来描述
"""
class A:
    def __init__(self, x):
        self.__x = x
    def set_x(self, x):
        self.__x = x
    def get_x(self):
        return self.__x
    
a = A(4)

print(a.get_x())

# __slots__成员
# class是由字典来完成映射关系，但是字典占用内存大，所以使用__slots__来固定成员变量节省内存
# 但是使用了__slots__的话，就不能在类外添加属性了
# 父类中的__slots__不会再子类中生效
class B:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("初始化x = %d y = %d" % (self.x, self.y))

b = B(5, 7)


#
class A:
    def __init__(self):
        print("a被创造")
    def __del__(self):
        print("a被销毁")
        

a = A()

del a

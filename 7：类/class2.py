"""
构造函数 
重写
"""
#构造函数 
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x * self.y
    
c = C(2, 4)
print(c.add())
print(c.mul())
print(c.__dict__)

#重写
# 直接调用用父类中未被绑定的方法用于子类
class D(C):
    def __init__(self, x, y, z):
        C.__init__(self, x, y)
        self.z = z

    def add(self):
        return C.add(self) + self.z
    def mul(self):
        return C.mul(self) * self.z  
d = D(3, 5, 2)
print(d.add())
print(d.mul())

# 钻石继承
# 现象 A 会被调用两次
# 解决方法 super()
class A:
    def __init__(self):
        print("this is A")

class B1(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print("this is B1")
        
class B2(A):
    def __init__(self):
        # A.__init__(self)
        super().__init__()
        print("this is B2")

class C1(B1, B2):
    def __init__(self):
        # B1.__init__(self)
        # B2.__init__(self)
        super().__init__()
        print("this is C1")
c1 = C1()


print(C1.mro())

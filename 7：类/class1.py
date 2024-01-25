"""
类 --> 对象

    封装
    继承    子类和父类中的相同名称的数据，子类会覆盖父类
            子类继承多个父类，优先级从左向右，依次查找
    
"""

#新键一个类
class Turtle_A:
    head = 1 
    eyes = 2
    legs = 4
    shell = True
    #类中的函数必须有一个self作为第一个参数,self相当于实例化对象本省
    def fun1(self):
        print("this is fun1")
    def fun2(self):
        print("this is fun2")
    def fun3(self):
        print("this is fun3")
    def fun4(self, arg):
        return arg * self.legs

Turtle_A.legs = 100

A1 = Turtle_A()
A2 = Turtle_A()

A1.legs = 4

print(A1.legs)  
print(A2.legs)     

#对父类的引用
class Turtle_B(Turtle_A):
    head = 4
    pass


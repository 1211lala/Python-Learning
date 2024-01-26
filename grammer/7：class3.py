"""
多态

Square 和 Circle 继承了 Shape 的__init__()函数 和 area() 含函数

""" 
class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        pass

class Square(Shape):
    def __init__(self, lenght):
        super().__init__("正方形")
        self.lenght = lenght
    def area(self):
        return self.lenght * self.lenght
    
class Circle(Shape):
    def __init__(self, R):
        super().__init__("圆形")
        self.R = R
    def area(self):
        return 3.14 * self.R * self.R
    
s = Square(5)
print("%s的面积为%d" % (s.name ,s.area()))
c = Circle(6)
print("%s的面积为%d" % (c.name ,c.area()))

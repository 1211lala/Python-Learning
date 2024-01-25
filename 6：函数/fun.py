"""
函数
    不用定义返回值,会自动定义
    关键字参数
        def fun3(name, age, height):
            print("name = %s" % name)
            print("age = %d" % age)
            print("height = %d" % height)
        fun3(name="liuao", age=20, height= 70)
    默认参数
        def fun4(name = "liuao", age = 20, height = 60):
    不定参数(收集参数)

    变量作用域
        global 在函数内修改全局作用域的函数时使用
        nonlocal 在内部函数中修改外部作用域数据时使用

    闭包

    装饰器

    lambda


        
"""


#带参数的函数
def fun1(name, times):
    for i in range(times):
        print("name = %s" % name)
fun1("dgs", 7)



#带返回值的函数
def fun2(x,y):
    return x+y
print(fun2(4,8))


#关键字参数
def fun3(name, age, height):
    print("name = %s" % name)
    print("age = %d" % age)
    print("height = %d" % height)
fun3(name="liuao", age=20, height= 70)


#默认参数
def fun4(name = "liuao", age = 20, height = 60):
    print("name = %s" % name)
    print("age = %d" % age)
    print("height = %d" % height)
fun4(name="dgs")



#变量作用域
x=880
def fun5():
    global x
    x = x + 100
    print(f"x = {x}")
fun5()
print(x)



#嵌套函数
def funA():
    y = 660
    def funB():
        print(f"funB y = {y}")
    return funB
funA()()
funC = funA()
funC()



#闭包函数
def fun6():
    x = 0
    y = 0
    def fun7(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"x = {x}  y={y}")
    return fun7
fun = fun6()

fun(1,2)
fun(-1,7)



#装饰器
import time

def time_master(fun):
    def get_time():
        start = time.time()
        fun()
        stop = time.time()
        print(f"程序运行{(stop-start):.2f}s")
    return get_time

def my_funC():
    print("myfun is runing!")
    time.sleep(0.9)

f = time_master(my_funC)

f()

#lambda
square1 = lambda x : x*x
print(square1(5))


#生成器 每调用一次返回一次数据，并保留当前状态，
def counter():
    i = 0
    while i < 5:
        print("生成器值为%d" % i)
        yield i
        i += 1

for i in counter():
    print(i)




help(print)


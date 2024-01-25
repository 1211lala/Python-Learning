"""
一个py文件就是一个模块
import 模块名称
from 模块名称 import 对象名称
import 模块名称 as 关联名称

__all__
"""

# import hello
# hello.say_hello()
# hello.say_hi()


# from hello import say_hello, say_hi
# say_hello()
# say_hi()


#调用包时用点隔开文件
import pkg.hello as hel
import temp

print(hel.x)
hel.say_hello()
hel.say_hi()


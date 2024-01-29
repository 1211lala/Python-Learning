'''
SyntaxError: 语法错误，通常是因为代码书写错误而引发的异常。
IndentationError: 缩进错误，通常是由于代码块缩进不正确而引发的异常
NameError: 变量或函数名不存在。
TypeError: 数据类型不匹配
ValueError: 数据值不合法
FileNotFoundError: 文件未找到异常，通常在尝试打开不存在的文件时引发
IndexError: 尝试访问列表、元组或字符串等序列中不存在的索引
KeyError: 尝试使用字典中不存在的键

捕获异常及处理
    try:
        异常代码
    except XXXError:
        XXXError处理异常代码
    except XXXError:
        XXXError处理异常代码
    else:
        处理代码
    finally:
        
'''
# 处理异常
number = [i for i in range(4)]
try:
    print(number[3])
except NameError:
    print("变量名不存在")
except ValueError:
    print("变量值不存在")
except (IndexError,SyntaxError,KeyError):
    print("索引值不存在")
else:
    print("无错误")
finally:
    print("finally\r\n\r\n")
    

# 自动抛出异常(raise)和自定义异常类

class MYError(BaseException):
    def __init__(self, msg):
        self.msg = msg
        
        
def fun (m, n):
    if(n == 0):
        # raise ZeroDivisionError("除数不能为0")
        raise MYError("除数不能为0")
    else:
        return m/n
fun(3, 0)
print("程序运行")
def say_hello():
    print("hello")
def say_hi():
    print("hi")

x = 100 
print("hello.py被调用")
print(f"__name__ = {__name__}")

if __name__ == "__main__":
    print("模块在被导入时会从头执行语句")
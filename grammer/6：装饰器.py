import time

def decorator(fun):
    def rec_dec(*arg, **kwargs):
        start = time.time()
        fun(*arg, **kwargs)
        print("函数运行了%.2fs" % ( time.time() - start))
    return rec_dec

## 不使用语法糖
# #计算求和
# def count_sum():
#     sum = 0
#     for i in range(10000000):
#         sum += i
#         # print("%d sum = %d" % (i , sum))
# #计算PI
# def count_pi():
#     PI = 0
#     N = 10000
#     for n in range(int(N)):
#         PI += 1/pow(16,n) * (4/(8*n+1) - 2/(8*n+4) - 1/(8*n+5) - 1/(8*n+6))
#     print(PI)

          
# ss = decorator(count_pi)
# print("装饰器已赋值")
# ss()


@decorator
def count_sum(arg):
    sum = 0
    for i in range(arg):
        sum += i
        # print("%d sum = %d" % (i , sum))
        
@decorator
def count_pi(arg):
    PI = 0
    for n in range(arg):
        PI += 1/pow(16,n) * (4/(8*n+1) - 2/(8*n+4) - 1/(8*n+5) - 1/(8*n+6))
    print(PI)
    
    
count_sum(10000000)
count_pi(1000)
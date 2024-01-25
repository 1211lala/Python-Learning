"""
1. 添加Python & pip的环境变量中
2. pip install flask 
3. 修改host和port app.run(host='0.0.0.0', port= 9000)

4. url与视图
    url == http/https://www.xxxx.com/path
        http默认80端口
        https默认443端口
        path 路径
        参数类型{
            string 
            int 
            float
            path路径可以带/
            UUID 32位的16进制数据
            any 备选值中的任意一个
        }
"""
#从flask的包中导入Flask类
from flask import Flask,request,render_template
#实例化对象
#__name__ 代表当前文件 
app = Flask(__name__)

#创建一个路由和函数\映射下面的函数作为回调
# @app.route('/')
# def hello_world():
#     return "hello "

#创建一个带参数的回调
@app.route("/ex1/<int:file_name>")
def file(file_name):
    return "访问的文件为:%d" % file_name


#处理url中的参数 
@app.route("/ex2/list")
def book():
    page = request.args.get("page",default=50, type=int)
    # return "访问的为book的第%d页" % page
    return f"访问的是{page}页"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 9000,debug=True)
"""
模板渲染 jinja2
    1. 把Debug模式打开,不然会报错
过滤器

"""

#从flask的包中导入Flask类
from flask import Flask,request,render_template
from datetime import datetime 
#实例化对象
#__name__ 代表当前文件 
app = Flask(__name__)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

#返回html文件 参数为类 函数参数
@app.route('/arg/<id>')
def show_blog_id(id):
    return render_template("index.html", blog_id=id, blog_name = "DGS")


#返回html文件 参数为类
#返回html文件 参数为字典
@app.route('/')
def hello_world():
    user = User(username = "DGS", email= "2494210546@qq.com")
    person = {
        "name" : "liuao",
        "age"  : 13,
        "height": "70kg",
        "email" : "2494210546@qq.com"
    }   
    return render_template("index.html", user = user,person = person)




#添加自定义过滤器
def datetime_format(value, format="%Y-%d-%m %H:%M"):
    return value.strftime(format)

app.add_template_filter(datetime_format, "dformat")

#过滤器
@app.route("/filter")
def filter_demo():
    user = User(username = "DGS", email= "2494210546@qq.com")
    mytime = datetime.now()
    return render_template("filter.html", user = user, mytime = mytime)


#控制语句
@app.route("/control")
def control_demo():
    age = 17
    books = [{"name":"book1","author":"author1"}, {"name":"book2","author":"author2"},{"name":"book3","author":"author3"}]
    return render_template("control.html", age = age, books = books)


#继承
@app.route("/chiled1")
def chiled1():
    return render_template("child1.html")

@app.route("/chiled2")
def chiled2():
    return render_template("child2.html")

    
#加载静态文件
@app.route('/static')
def static_demo():
    print("正在访问static")
    return render_template("static.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 9000,debug=True)
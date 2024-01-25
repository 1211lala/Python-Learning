
from flask import Flask,request,render_template,redirect,url_for,make_response,json,jsonify,abort

# __name__ 代表当前文件 
app = Flask(__name__)

# 请求方法
@app.route('/',methods = ["GET", "POST"])
def route_path():
    return "hello world!!!"


#变量规则
# @app.route('/user/<int:id>',methods = ["GET", "POST"])
# @app.route('/user/<str:id>',methods = ["GET", "POST"])
# @app.route('/user/<float:id>',methods = ["GET", "POST"])
@app.route('/user/<id>',methods = ["GET", "POST"])
def user_path(id):
    if int(id) == 1:
        return "this is 1"
    if int(id) == 0:
        return "this is 0"
    return "not found"




# #from表单(前端)
# @app.route('/form',methods = ["GET", "POST"])
# def form_demo():
    
#     name = request.form.get("name1")
#     password = request.form.get("password1")
    
#     print("输入的账号名称为%s" % name)
#     print("输入的账号密码为%s" % password)
    
#     return render_template("index.html")


#from表单(后端)
from wtforms import StringField, PasswordField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,EqualTo

class Register(FlaskForm):
    user_name = StringField(label="用户名", validators = [DataRequired("用户名不能为空")])
    user_password = PasswordField(label="密码", validators=[DataRequired("密码不能为空")])
    user_password2 = PasswordField(label="确认密码", validators=[DataRequired("密码不能为空"), EqualTo('user_password')])
    submit = SubmitField(label= "提交")

app.config["SECRET_KEY"] = "Aaaaa"

@app.route('/form',methods = ['GET', 'POST'])
def form_demo():
    form = Register()
    print(request.method)
    if request.method == 'GET':
        return render_template("reg.html", form = form)
    if request.method == 'POST':
        print("账号名称:%s" % form.user_name.data)
        print("账号密码:%s" % form.user_password.data)
        print("确认密码:%s" % form.user_password2.data)
        return render_template("reg.html", form = form) 



# 重定向 302
# 点击按钮前往新的网页
@app.route("/redirect")
def redirect_path():
    ## 返回外部网页
    # return redirect("http://www.baidu.com")
    ##返回内部函数
    return redirect(url_for("route_path"))

# Json
@app.route("/json")
def json_path():
    data = {
        "name":"刘奥",
        "age":24
    }
    # response = make_response(json.dumps(data, ensure_ascii= False))
    # response.mimetype = 'application/json'
    # return response
    return jsonify(data)

# abort
# 抛出异常
@app.route('/abort',methods = ["GET", "POST"])
def abort_demo():
    
    if request.method == "GET":
        return render_template("index.html")
    
    if request.method == "POST":
        
        name = request.form.get("name1")
        password = request.form.get("password1")
        
        if name == "liuao" and password == "123":
            return make_response("log in success !")
        else:
            print("404")
            abort(404)
            
            return None

@app.errorhandler(404)
def handle_404_error(err):
    return render_template("404.html")



# flask数据库
# pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy

class Config:
    SQLALCHEMY_DATABASE_URL = 'mysql://root:liuao@127.0.0.1:3306/flaskdb'
    
app.config.from_object(Config)
db = SQLAlchemy(app)

class Role(db.Model):
    __tablename__ = "role"
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(32), unique = True)

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(30), unique = True)
    password = db.Column(db.String(120))
    role_id = db.Column(db.Integer, db.ForeignKey("role.id"))


if __name__ == '__main__':
    
    db.drop_all()
    db.create_all()
    
    # app.run(host='0.0.0.0', port= 9000,debug=True)
    role1 = Role(name = "admin1")
    
    db.session.add(role1)
    
    db.session.commit()
    
    role2 = Role(name = "admin2")
    
    db.session.add(role2)
    
    db.session.commit()
    
    
    use1 = User(name = "zhangsan", password = "1222", role_id = role1.id)
    use2 = User(name = "lisi", password = "3334", role_id = role1.id)
    use3 = User(name = "wangzi", password = "4445", role_id = role2.id)
    
    db.session.commit()
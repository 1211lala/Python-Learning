from flask import Flask, request,render_template

app = Flask(__name__)



@app.route('/',methods = ["GET", "POST"])
def route_path():
    return render_template("index.html")


@app.route('/key',methods = ["GET", "POST"])
def key_path():
    print("账号为:%s" % request.form.get("my_name"))
    print("密码为:%s" % request.form.get("my_password"))
    print("时间为:%s" % request.form.get("my_datetime-local"))
    print("性别为:%s" % request.form.get("my_radio"))
    print("颜色为:%s" % request.form.get("my_color"))
    # 获取文件上传的文件对象
    my_file = request.files['my_file']
    
    # 处理上传的文件，这里简单地打印文件名和内容
    if my_file:
        filename = my_file.filename
        content = my_file.read()
        print(f'Uploaded file: {filename}, Content: {content.decode("utf-8")}')
        
        
    if request.form.get("my_checkbox") == "yes is adult":
        print("checkbox = ON")
    elif request.form.get("my_checkbox") == None:
        print("checkbox = OFF")
        
    
    return "数据提交完成"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port= 9000,debug=True)
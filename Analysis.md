# python中文资料网站
    http://www.pythondoc.com/pythontutorial3/datastructures.html#tut-dictionaries
    https://www.runoob.com/python3/python3-errors-execptions.html

## 字节串和字符串

    在 Python 中，以 b 开头的字面量表示字节串(bytes)这是 Python 3 引入的语法，用于明确表示一个字节串而不是字符串。
```py
    # 字符串
    print(type("hello"))
    <class 'str'>

    # 字节串
    print(type(b"hello"))
    <class 'bytes'>
```
    在 Python 中，encode 和 decode 是字符串的两个方法，用于在不同的字符编码之间进行转换。

    
    字符串 --> 字节串
    encode(encoding='utf-8', errors='strict'):

    参数 encoding 指定了目标字符编码，默认为 UTF-8。
    参数 errors 指定了错误处理方式，常见的有 'strict'（默认，遇到非法字符时抛出异常）、'ignore'（忽略非法字符）等。


    字节串 --> 字符串
    decode(encoding='utf-8', errors='strict')：

    该方法用于将字节串解码为指定的字符编码的字符串。
    参数 encoding 指定了字节串的字符编码，默认为 UTF-8。
    参数 errors 指定了错误处理方式，同样可以是 'strict'、'ignore' 等。


## Json
```py
    # 从文件中读取json文件并转换成python的数据类型
    json.load(fp) 
    
    # 读取json字符串并转换成python的数据类型
    json.loads(str) 
    
    # 将python格式的数据类型转换成json格式,保存到文件中
    json.dump(obj, fp) 
    
    # 将python的数据类型转换成json格式中,并返回字符串
    json.dumps(obj) 
    
```



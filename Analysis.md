# 字节串和字符串

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


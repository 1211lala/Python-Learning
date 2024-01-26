import os
import urllib.request


# url = "http://www.pyqt5.cn/static/images/logo.jpg"
# file_name = "picture.jpg"

# url = "http://192.168.8.70"
# file_name = "home.html"

url ="https://vod.v.jstv.com/2024/01/25/JSTV_JSGGNEW_1706182874473_NBn3baX_1928.mp4"
file_name = "sp.mp4"


# url = "https://www.bilibili.com/video/BV1se411Y7FU/?spm_id_from=333.1007.tianma.2-1-3.click"
# file_name = "bili.mp4"

# 获取当前脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建文件夹的相对路径
folder_path = os.path.join(script_dir, "files")

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

file_path = os.path.join(folder_path, file_name)

print(file_path)
urllib.request.urlretrieve(url, filename=file_path)
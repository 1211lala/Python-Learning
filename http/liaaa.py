"""
json.load(fp) 从文件中读取json文件并转换成python的数据类型
json.loads(str) 读取json字符串并转换成python的数据类型

json.dump(obj, fp) 将python格式的数据类型转换成json格式,保存到文件中
json.dumps(obj) 将python的数据类型转换成json格式中,并返回字符串


    server.serveStatic("/", LittleFS, "/").setDefaultFile("home_min.html");

    server.on("/get_software_version", HTTP_GET, get_software_version_callback);

    server.on("/get_wifi_config", HTTP_GET, get_wifi_config_callback);
    server.on("/set_wifi_config", HTTP_POST, set_wifi_config_callback);

    server.on("/get_firedoor_config", HTTP_GET, get_firedoor_config_callback);
    server.on("/set_firedoor_config", HTTP_POST, set_firedoor_config_callback);

    server.on("/get_firedoor_data", HTTP_GET, get_firedoor_data_callback);
    server.on("/set_firedoor_data", HTTP_POST, set_firedoor_data_callback);

    server.on("/set_wifi_scan", HTTP_GET, set_wifi_scan_callback);
    server.on("/get_wifi_list", HTTP_GET, get_wifi_list_callback);

    server.on("/get_board_info", HTTP_GET, get_board_info_callback);
    server.on("/set_soft_reboot", HTTP_POST, set_soft_reboot_callback);
    
    
"""
import urllib.request
import json
import time

print("[ %.2f ]开始访问url" % time.time())
response = urllib.request.urlopen("http://192.168.8.89/get_firedoor_data")
print("[ %.2f ]开始读取url" % time.time())
data_json = response.read().decode("utf-8")
print("[ %.2f ]开始转换url"% time.time())
data_dict = json.loads(data_json)
print(data_dict["code"])
print(data_dict["msg"])
print(data_dict["data"]["state"])
print(data_dict["data"]["angle"])

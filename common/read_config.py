# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 15:15
# @Author  : Rock
# @File    : read_config.py
# @describe: 读取配置文件

# import os
# import codecs
# import configparser
#
# proDir = os.path.split(os.path.realpath(__file__))[0]
# configPath = os.path.join(proDir, "config.ini")
#
#
# class ReadConfig:
#     def __init__(self):
#         fd = open(configPath)
#         data = fd.read()
#
#         #  remove BOM
#         if data[:3] == codecs.BOM_UTF8:
#             data = data[3:]
#             file = codecs.open(configPath, "w")
#             file.write(data)
#             file.close()
#         fd.close()
#
#         self.cf = configparser.ConfigParser()
#         self.cf.read(configPath)
#
#     def get_email(self, name):
#         value = self.cf.get("EMAIL", name)
#         return value
#
#     def get_http(self, name):
#         value = self.cf.get("HTTP", name)
#         return value
#
#     def get_login(self, name):
#         value = self.cf.get("LOGIN", name)
#         return value
#
#
# if __name__ == '__main__':
#     demo = ReadConfig()
#     print(demo.get_email("mail_pass"))
#     print(demo.get_http("base_url"))
#     print(demo.get_login("userName"))


import configparser


class ReadIni(object):
    # 构造函数
    def __init__(self, file_name=None, node=None):
        if file_name is None:
            file_name = './config/config.ini'

        if node is None:
            self.node = 'HTTP'
        else:
            self.node = node

        self.conf = self.load_ini(file_name)

    # 加载文件
    @staticmethod
    def load_ini(file_name):
        conf = configparser.ConfigParser()
        conf.read(file_name)
        return conf

    # 获取Value值
    def get_value(self, key):
        data = self.conf.get(self.node, key)
        return data


if __name__ == '__main__':
    # read = ReadIni()
    read = ReadIni('./config.ini', 'HTTP')
    print(read.get_value('baseurl'))

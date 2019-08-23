# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 15:15
# @Author  : Rock
# @File    : read_config.py
# @describe: 读取配置文件

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
    read = ReadIni('../config/config.ini', 'HTTP')
    print(read.get_value('base_url'))

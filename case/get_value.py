# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:53
# @Author  : DannyDong
# @File    : base_test.py
# @describe: 测试用例基类

from config.read_config import ReadConfig
from common.utils import create_name, create_phone


class GetValue(object):
    # 读取配置文件
    base_url = ReadConfig().get_http("base_url")
    username = ReadConfig().get_login("userName")
    password = ReadConfig().get_login("password")

    mail_pass = ReadConfig().get_email("mail_pass")

    # 执行工具方法
    name = create_name()
    phone = create_phone()

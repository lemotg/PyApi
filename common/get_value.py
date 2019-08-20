# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:53
# @Author  : DannyDong
# @File    : base_test.py
# @describe: 测试用例基类

from common.read_config import ReadIni
from common.utils import create_name, create_phone


class GetValue(object):
    # 读取配置文件
    base_url = ReadIni(node='HTTP').get_value("base_url")

    username = ReadIni(node='LOGIN').get_value("userName")
    password = ReadIni(node='LOGIN').get_value("password")

    # 获取邮箱密码
    mail_pass = ReadIni(node='EMAIL').get_value("mail_pass")

    # 获取debug开关的状态
    is_debug = ReadIni(node='MODEL').get_value("debug")

    # 执行工具方法
    name = create_name()
    phone = create_phone()
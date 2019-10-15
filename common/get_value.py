# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 16:53
# @Author  : DannyDong
# @File    : get_value.py
# @describe: 配置文件读取

from common.read_config import ReadIni


class GetValue(object):
    # 读取配置文件
    base_url = ReadIni(node='HTTP').get_value("base_url")
    username = ReadIni(node='LOGIN').get_value("userName")
    password = ReadIni(node='LOGIN').get_value("password")
    campusId = ReadIni(node='LOGIN').get_value("campusId")

    # 获取邮箱密码
    mail_pass = ReadIni(node='EMAIL').get_value("mail_pass")

    # 获取debug开关的状态
    is_debug = ReadIni(node='MODEL').get_value("debug")

    # 获取WebHook地址
    web_hook_url = ReadIni(node='WEBHOOK').get_value('web_hook_url')
    web_hook_phone = ReadIni(node='WEBHOOK').get_value('web_hook_phone')

    # 定义参数传递方式
    header = {'Content-Type': 'application/json'}

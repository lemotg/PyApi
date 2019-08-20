# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 11:53
# @Author  : Rock
# @File    : get_cookie.py
# @describe: 登录接口

import requests
from config.read_config import ReadConfig

# 读取配置文件
base_url = ReadConfig().get_http("base_url")
userName = ReadConfig().get_login("userName")
password = ReadConfig().get_login("password")


class LoginApi(object):
    def __init__(self):
        self.url = base_url + "manager/signin"

    def get_cookie(self):
        r = requests.post(self.url, data={"userName": userName, "password": password})
        login_cookie = r.cookies
        # print(login_cookie)
        return login_cookie


if __name__ == '__main__':
    Login = LoginApi()
    print(Login.get_cookie())

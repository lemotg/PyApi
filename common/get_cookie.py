# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 11:53
# @Author  : Rock
# @File    : get_cookie.py
# @describe: 登录接口

import requests
from common.get_value import GetValue


class LoginApi(GetValue):
    def __init__(self):
        self.url = self.base_url + "manager/signin"

    def get_cookie(self):
        r = requests.post(self.url, data={"userName": self.username, "password": self.password})
        login_cookie = r.cookies
        # print(login_cookie)
        return login_cookie


if __name__ == '__main__':
    Login = LoginApi()
    print(Login.get_cookie())

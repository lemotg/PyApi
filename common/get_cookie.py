# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 11:53
# @Author  : Rock
# @File    : get_cookie.py
# @describe: 登录接口

import requests
from common.get_value import GetValue
from common.get_log import TestLogs


class LoginApi(GetValue):
    def __init__(self):
        self.url = self.base_url + "manager/signin"
        self.url2 = self.base_url + "manager/switch_campus"
        self.log = TestLogs().get_log()

    def get_cookie(self):
        r = requests.post(self.url, data={"userName": self.username, "password": self.password})
        login_cookie = r.cookies
        # 调用校区切换接口，保证在测试校区运行测试，避免测试数据污染
        requests.post(self.url2, data={"campusId": "N89r0ljVIIw0"}, cookies=login_cookie)
        return login_cookie


if __name__ == '__main__':
    Login = LoginApi()
    print(Login.get_cookie())

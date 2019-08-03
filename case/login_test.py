# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 16:17
# @Author  : Rock
# @File    : login_test.py.py
# @describe: 登录退出接口

import unittest
import requests


class LoginApiTest(unittest.TestCase):
    """登录接口测试"""

    def setUp(self):
        self.url = "https://10.0.22.17:21878/manager/signin"
        self.userName = "bsxz"
        self.password = "33a1cd102fe76c63411cd97bc6be59ab"

    def test_1账号密码正确(self):
        r = requests.post(self.url,data={"password":self.password,"userName":self.userName})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code,200)
        self.assertEqual(result['data']['name'],'boss校长')

    def test_2账号错误(self):
        r = requests.post(self.url,data={"password":self.password,"userName":'1'})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code,200)
        self.assertEqual(result['status']['code'],3134)
        self.assertEqual(result['status']['message'],'账号错误')

    def test_3密码错误(self):
        r = requests.post(self.url,data={"password":"111","userName":self.userName})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code,200)
        self.assertEqual(result['status']['code'],3135)
        self.assertEqual(result['status']['message'],'密码错误')

    def test_4账号密码为空(self):
        r = requests.post(self.url,data={"password":"","userName":""})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code,200)
        self.assertEqual(result['status']['code'],2017)
        self.assertEqual(result['status']['message'],'参数错误')


if __name__ == '__main__':
    unittest.main()



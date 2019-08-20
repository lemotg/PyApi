# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 16:17
# @Author  : Rock
# @File    : login_test.py.py
# @describe: 登录退出接口

import unittest
import requests

from common.get_value import GetValue


class LoginApiTest(unittest.TestCase, GetValue):
    """登录接口"""

    def setUp(self):
        self.url = self.base_url+"manager/signin"

    def test_1(self):
        """账号密码正确"""
        r = requests.post(self.url, data={"password": self.password, "userName": self.username})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['data']['name'], 'boss校长')

    def test_2(self):
        """账号错误"""
        r = requests.post(self.url, data={"password": self.password, "userName": '1'})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['status']['code'], 3134)
        self.assertEqual(result['status']['message'], '账号错误')

    def test_3(self):
        """密码错误"""
        r = requests.post(self.url, data={"password": "111", "userName": self.username})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['status']['code'], 3135)
        self.assertEqual(result['status']['message'], '密码错误')

    def test_4(self):
        """账号密码为空"""
        r = requests.post(self.url, data={"password": "", "userName": ""})
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['status']['code'], 2017)
        self.assertEqual(result['status']['message'], '参数错误')


if __name__ == '__main__':
    unittest.main()

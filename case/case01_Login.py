# -*- coding: utf-8 -*-
# @Time    : 2019/8/2 16:17
# @Author  : Rock
# @File    : case01_Login.py.py
# @describe: 登录退出接口

import unittest
import requests

from common.get_value import GetValue
from common.get_log import LogInfo


class ApiTest(unittest.TestCase, GetValue, LogInfo):
    """登录接口"""
    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('LoginApi测试用例开始执行')
        cls.url = cls.base_url+"manager/signin"  # 登录
        cls.log.info('URL获取成功, URL:'+cls.url)

    @LogInfo.get_error
    def setUp(self):
        pass

    @LogInfo.get_error
    def test_1(self):
        """账号密码正确"""
        r = requests.post(self.url, data={"password": self.password, "userName": self.username})
        result = r.json()
        self.log.debug(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['data']['name'], 'boss校长')

    @LogInfo.get_error
    def test_2(self):
        """账号错误"""
        r = requests.post(self.url, data={"password": self.password, "userName": '1'})
        result = r.json()
        self.log.debug(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['status']['code'], 3134)
        self.assertEqual(result['status']['message'], '账号错误')

    @LogInfo.get_error
    def test_3(self):
        """密码错误"""
        r = requests.post(self.url, data={"password": "111", "userName": self.username})
        result = r.json()
        self.log.debug(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['status']['code'], 3135)
        self.assertEqual(result['status']['message'], '密码错误')

    @LogInfo.get_error
    def test_4(self):
        """账号密码为空"""
        r = requests.post(self.url, data={"password": "", "userName": ""})
        result = r.json()
        self.log.debug(result)
        code = r.status_code
        self.assertEqual(code, 200)
        self.assertEqual(result['status']['code'], 2017)
        self.assertEqual(result['status']['message'], '参数错误')


if __name__ == '__main__':
    unittest.main()

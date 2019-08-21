# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 15:49
# @Author  : Rock
# @File    : student_test.py
# @describe: 学员相关接口

import unittest
import requests

from common.get_cookie import LoginApi
from common.get_value import GetValue
from common.get_log import TestLogs


class StudentApiTest(unittest.TestCase, GetValue):
    """学员相关接口"""
    @classmethod
    def setUpClass(cls) -> None:
        cls.log = TestLogs().get_log()

    def setUp(self):
        # 将获取cookie放入初始化函数中，否则cookie会丢失
        self.cookie = LoginApi().get_cookie()
        self.log.info('Cookie获取成功')
        self.url = self.base_url+"student/potential/new"
        self.log.info('URL获取成功, URL:'+self.url)

    def test1(self):
        """新增学员"""
        r = requests.post(self.url, data={"name": self.name, "phone": self.phone}, cookies=self.cookie)
        result = r.json()
        self.log.info(result)
        self.assertEqual(result['data']['phone'], self.phone)
        self.assertEqual(result['data']['name'], self.name)


if __name__ == '__main__':
    unittest.main()

# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 15:49
# @Author  : Rock
# @File    : student_test.py
# @describe: 学员相关接口

import unittest
import requests

from common.get_cookie import LoginApi
from common.get_value import GetValue, ReadIni


class StudentApiTest(unittest.TestCase, GetValue):
    """学员相关接口"""

    def setUp(self):
        # 将获取cookie放入初始化函数中，否则cookie会丢失
        self.cookie = LoginApi().get_cookie()
        self.url = self.base_url+"student/potential/new"

    def test1(self):
        """新增学员"""
        r = requests.post(self.url, data={"name": self.name, "phone": self.phone}, cookies=self.cookie)
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()

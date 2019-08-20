# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 15:49
# @Author  : Rock
# @File    : student_test.py
# @describe: 学员相关接口

import unittest
import requests
from common.get_cookie import LoginApi
from common.utils import create_name, create_phone
from config.read_config import ReadConfig

name = create_name()
phone = create_phone()
cookie = LoginApi().get_cookie()
base_url = ReadConfig().get_http("base_url")


class StudentApiTest(unittest.TestCase):
    """学员相关接口"""

    def setUp(self):
        self.url = base_url+"student/potential/new"

    def test1(self):
        """新增学员"""
        r = requests.post(self.url, data={"name": name, "phone": phone}, cookies=cookie)
        result = r.json()
        print(result)
        code = r.status_code
        self.assertEqual(code, 200)


if __name__ == '__main__':
    unittest.main()


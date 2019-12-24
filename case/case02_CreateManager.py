# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 14:59
# @Author  : Rock
# @File    : case02_CreateManager.py
# @describe: 新建员工账号
import unittest
import requests

from common.utils import CreateData
from common.get_cookie import LoginApi
from common.get_value import GetValue
from common.get_log import LogInfo


class ApiTest(unittest.TestCase, GetValue, LogInfo):

    """新建员工接口"""
    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('StudentApi测试用例开始执行')
        # 将获取cookie放入初始化函数中，否则cookie会丢失
        cls.cookie = LoginApi().get_cookie()
        cls.log.info('Cookie获取成功')
        cls.url0 = cls.base_url+"manager/create"   # 新增员工

    @LogInfo.get_error
    def setUp(self):
        self.name = CreateData.create_name()
        self.phone = CreateData.create_phone()

    @LogInfo.get_error
    def test_1(self):
        """新增教师账号"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        r = requests.post(
            self.url0,
            cookies=self.cookie,
            headers=self.header,
            json={"name": "教师",
                  "accountName": self.name,
                  "phone": self.phone,
                  "password": self.password,
                  "groupIds": ["SYSTEM_TEACHER"],
                  "campusIds": [self.campusId],
                  "level": 1},
        )
        result = r.json()
        self.log.debug(result)
        self.assertEqual(result['data']['phone'], self.phone)
        self.assertEqual(result['data']['userName'], self.name)
        global managerId
        managerId = result['data']['managerId']
        self.log.debug(managerId)

    def test_2(self):
        """新增助教账号"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        r = requests.post(
            self.url0,
            cookies=self.cookie,
            headers=self.header,
            json={"name": "助教",
                  "accountName": self.name,
                  "phone": self.phone,
                  "password": self.password,
                  "groupIds": ["SYSTEM_ASSISTANT"],
                  "campusIds": [self.campusId],
                  "level": 1},
        )
        result = r.json()
        self.log.debug(result)
        self.assertEqual(result['data']['phone'], self.phone)
        self.assertEqual(result['data']['userName'], self.name)


if __name__ == '__main__':
    unittest.main()

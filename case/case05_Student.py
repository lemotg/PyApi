# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 15:49
# @Author  : Rock
# @File    : case05_Student.py
# @describe: 学员相关接口

import unittest
import requests

from common.utils import CreateData
from common.get_cookie import LoginApi
from common.get_value import GetValue
from common.get_log import LogInfo


class ApiTest(unittest.TestCase, GetValue, LogInfo):

    """学员相关接口"""
    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('StudentApi测试用例开始执行')
        # 将获取cookie放入初始化函数中，否则cookie会丢失
        cls.cookie = LoginApi().get_cookie()
        cls.log.info('Cookie获取成功')
        cls.url0 = cls.base_url+"student/potential/new"   # 新增学员
        cls.url1 = cls.base_url+"student/potential/add_track_record"  # 添加跟进记录

    @LogInfo.get_error
    def setUp(self):
        self.name = CreateData.create_name()
        self.phone = CreateData.create_phone()
        self.millis = CreateData.get_millis()

    @LogInfo.get_error
    def test_1(self):
        """正常新增学员"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        r = requests.post(
            self.url0,
            cookies=self.cookie,
            headers=self.header,
            json={
                "name": self.name,
                "phone": self.phone
            },
        )
        result = r.json()
        self.log.debug(result)
        self.assertEqual(result['data']['phone'], self.phone)
        self.assertEqual(result['data']['name'], self.name)
        global studentid
        studentid = result['data']['studentId']

    @LogInfo.get_error
    def test_2(self):
        """新增学员，手机号输入错误"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        r = requests.post(
            self.url0,
            cookies=self.cookie,
            headers=self.header,
            json={
                "name": self.name,
                "phone": " "
            }
        )
        result = r.json()
        self.log.debug(result)
        self.assertEqual(result['status']['message'], '参数错误')

    @LogInfo.get_error
    def test_3(self):
        """增加意向学员跟进记录"""
        self.log.debug('URL获取成功, URL:' + self.url1)
        r = requests.post(
            self.url1,
            cookies=self.cookie,
            headers=self.header,
            json={
                "studentId": studentid,
                "trackBody": {
                    "communicateDate": self.millis,
                    "communicateType": 1,
                    "communicator": 1,
                    "content": "自动化测试跟进",
                },
                "studentType": "1"
            }
        )
        result = r.json()
        self.log.debug(result)
        self.assertIn('followRecordId', result['data'])


if __name__ == '__main__':
    unittest.main()

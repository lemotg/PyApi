# -*- coding: utf-8 -*-
# @Time    : 2019/10/11 14:54
# @Author  : Rock
# @File    : case03_CreateCourse.py
# @describe: 新建课程接口

import unittest
import requests

from common.utils import CreateData
from common.get_cookie import LoginApi
from common.get_value import GetValue
from common.get_log import LogInfo


class ApiTest(unittest.TestCase, GetValue, LogInfo):

    """新建课程接口"""
    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('CreateCourseApi测试用例开始执行')
        # 将获取cookie放入初始化函数中，否则cookie会丢失
        cls.cookie = LoginApi().get_cookie()
        cls.log.info('Cookie获取成功')
        cls.url0 = cls.base_url+"course/new"   # 新增课程

    @LogInfo.get_error
    def setUp(self):
        self.course_name = CreateData.create_coursename()

    @LogInfo.get_error
    def test_1(self):
        """正常新增班组课程"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        r = requests.post(
            self.url0,
            headers=self.header,
            cookies=self.cookie,
            json={
                "courseType": 1,
                "name": self.course_name,
                "chargeType": 2,
                "duration": 600000,
                "periodsPerTimes": 10,
                "unitPrice": 1000,
                "remark": "班组课",
                "packages": [
                    {
                        "packageUnit": 1,
                        "containNum": 10,
                        "totalPrice": 1000
                    }
                ],
                "isEnabled": True
            },
        )

        result = r.json()
        self.log.debug(result)
        self.assertIn('courseId', result['data'])

    @LogInfo.get_error
    def test_2(self):
        """正常新增1对1课程"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        r = requests.post(
            self.url0,
            headers=self.header,
            cookies=self.cookie,
            json={
                "courseType": 2,
                "name": self.course_name,
                "chargeType": 2,
                "duration": 600000,
                "periodsPerTimes": 10,
                "unitPrice": 1000,
                "remark": "1对1",
                "packages": [
                    {
                        "packageUnit": 1,
                        "containNum": 10,
                        "totalPrice": 1000
                    }
                ],
                "isEnabled": True
            },
        )

        result = r.json()
        self.log.debug(result)
        self.assertIn('courseId', result['data'])


if __name__ == '__main__':
    unittest.main()

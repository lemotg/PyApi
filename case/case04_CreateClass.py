# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 11:03
# @Author  : Rock
# @File    : case04_CreateClass.py
# @describe: 新建班级接口

import unittest
import requests

from common.utils import CreateData
from common.get_cookie import LoginApi
from common.get_value import GetValue
from common.get_log import LogInfo
from common.base_data import BaseData


class ApiTest(unittest.TestCase, GetValue, LogInfo):

    """新建班级接口"""
    @classmethod
    @LogInfo.get_error
    def setUpClass(cls) -> None:
        cls.log.info('CreateClassApi测试用例开始执行')
        # 将获取cookie放入初始化函数中，否则cookie会丢失
        cls.cookie = LoginApi().get_cookie()
        cls.log.info('Cookie获取成功')
        cls.url0 = cls.base_url + "edu_class/new"  # 新增班级
        cls.url1 = cls.base_url + "course/list"  # 查询课程信息

    @LogInfo.get_error
    def setUp(self):
        self.millis = CreateData.get_millis()
        self.name = CreateData.create_name()
        payload = {'index': 0, 'limit': 1, 'course_type': 1, 'charge_type': 2}
        r = requests.get(self.url1, params=payload, cookies=self.cookie)
        result = r.json()
        self.log.debug('查询最新的课程信息')
        global courseId, courseName
        courseId = result['data']['courses'][0]['courseId']
        courseName = result['data']['courses'][0]['name']

    @LogInfo.get_error
    def test_1(self):
        """正常新增班级"""
        self.log.debug('URL获取成功, URL:' + self.url0)
        teacher_data = BaseData().get_teacher(self.cookie)
        accountId = teacher_data['data']['accountId']
        managerId = teacher_data['data']['managerId']
        teacher_name = teacher_data['data']['name']

        self.log.info(self.cookie)
        r = requests.post(
            self.url0,
            headers=self.header,
            cookies=self.cookie,
            json={"name": self.name+"班",
                  "course": {
                      "name": courseName,
                      "courseId": courseId,
                      "chargeType": 2,
                      "times": -10000,
                      "courseType": 1,
                      "teacher":
                          {"name": teacher_name,
                           "accountId": accountId,
                           "managerId": managerId}
                  },
                  "startDate": self.millis,
                  "expectedEnrollment": 3,
                  "isContainer": False
                  }
        )
        result = r.json()
        self.log.debug(result)


if __name__ == '__main__':
    unittest.main()

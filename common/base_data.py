# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 15:54
# @Author  : Rock
# @File    : base_data.py
# @describe: 前置接口

import requests
from common.get_value import GetValue
from common.get_log import LogInfo
from common.get_cookie import LoginApi
from common.utils import CreateData


class BaseData(LogInfo):
    @LogInfo.get_error
    def __init__(self):
        self.url = GetValue.base_url + "manager/create"

    def get_teacher(self, cookie):
        self.log.debug('URL获取成功, URL:' + self.url)
        r = requests.post(
            self.url,
            cookies=cookie,
            headers=GetValue.header,
            json={"name": "教师",
                  "accountName": CreateData.create_name(),
                  "phone": CreateData.create_phone(),
                  "password": GetValue.password,
                  "groupIds": ["SYSTEM_TEACHER"],
                  "campusIds": [GetValue.campusId],
                  "level": 1},
        )
        result = r.json()
        return result


if __name__ == '__main__':
    result = BaseData().get_teacher()
    print(result)

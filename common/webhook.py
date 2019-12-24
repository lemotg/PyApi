# -*- coding: utf-8 -*-
# @Time    : 2019/9/7 15:45
# @Author  : DannyDong
# @File    : webhook.py
# @describe: 接通钉钉机器人通知

import json
import requests

from common.get_value import GetValue


class WebHook(GetValue):
    def __init__(self):
        pass

    def web_hook(self, text, mobile):
        url = self.web_hook_url
        program = {
            "msgtype": "text",
            "text": {"content": text},
            "at": {
                "atMobiles": mobile,
                # "isAtAll": False
                "isAtAll": True
            }
        }
        headers = {'Content-Type': 'application/json'}
        requests.post(url, data=json.dumps(program), headers=headers)

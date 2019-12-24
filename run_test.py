# coding=utf-8
# @Time    : 2019/8/2 23:04
# @Author  : Rock
# @File    : run_test.py
# @describe: 运行入口

import time
import unittest

from common.HTMLTestRunner_cn import HTMLTestRunner

from common.send_email import SendEmail
from common.get_value import GetValue
from common.webhook import WebHook

if __name__ == '__main__':
    if GetValue.is_debug == 'False':
        WebHook().web_hook('铁憨憨开始执行接口自动化测试任务啦', GetValue.web_hook_phone)
    # 定义测试用例的目录为当前目录
    test_dir = './case'
    test_report = './report'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='case*.py')

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H.%M")

    # 定义报告存放路径和文件名
    filename = test_report + "\\" + now + 'result.html'

    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试报告',
                            description='用例执行情况：')

    runner.run(discover)  # 运行测试用例
    fp.close()  # 关闭报告文件

    # 发送邮件开关is_debug,debug模式下，不发送邮件
    if GetValue.is_debug == 'False':
        # 实例化对象
        demo = SendEmail(test_report)
        # 获取最新报告
        new_report = demo.new_report()
        # 发送测试报告
        demo.send_mail(new_report)
        # WebHook
        WebHook().web_hook('接口自动化测试任务结束啦，快去邮箱查看测试报告吧', GetValue.web_hook_phone)
    else:
        pass

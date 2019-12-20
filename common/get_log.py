# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 23:18
# @Author  : DannyDong
# @File    : get_log.py
# @describe: 生成日志信息

import os
import logging
import datetime
import functools
import traceback

from common.get_value import GetValue


class TestLogs(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '\033[0;32m[%(asctime)s]-[%(levelname)s] %(filename)s--> %(funcName)s ----->%(message)s\033[0m'
        )

        # 设置控制台日志信息
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        # 设置级别日志级别,Logging中有NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL这几种级别，日志会记录设置级别以上的日志
        console.setLevel(logging.DEBUG)
        self.logger.addHandler(console)

        # 生成日志文件的开关，为debug模式，不生成文件
        if GetValue.is_debug == 'False':
            # 生成文件路径
            file_name = datetime.datetime.now().strftime("%Y-%m-%d")+".log"

            # 获取当前目录的绝对路径
            cur_path = os.path.abspath(__file__)
            # 获取logs文件夹的绝对路径
            logs_path = os.path.join(os.path.abspath(os.path.dirname(cur_path) + os.path.sep + '../logs/'), '')

            # 设置文件日志信息
            file_handle = logging.FileHandler(logs_path + file_name, mode='a', encoding='utf-8')
            file_handle.setFormatter(formatter)
            file_handle.setLevel(logging.DEBUG)
            self.logger.addHandler(file_handle)

    def get_log(self):
        return self.logger

    def close_link(self):
        pass


class LogInfo(object):
    log = TestLogs().get_log()

    @classmethod
    def get_error(cls, func):
        """
        get_error装饰器，用于获取错误信息并且写入日志
        :param func: 入参函数
        :return:
        """
        @functools.wraps(func)
        def wrapper_func(self):
            try:
                func(self)
            except (RuntimeError, SyntaxError, AttributeError, ValueError, KeyError):
                self.log.error(traceback.format_exc())
                raise Exception('系统出现异常，请及时处理！')
        return wrapper_func


if __name__ == '__main__':
    logger = LogInfo()
    logger.log.debug('this is a debug log')
    logger.log.info('this is a info log')
    logger.log.error('this is a error log')
    logger.log.warning('this is a warning log')

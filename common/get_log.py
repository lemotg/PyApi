# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 23:18
# @Author  : DannyDong
# @File    : get_log.py
# @describe: 生成日志信息

import logging
import datetime


class TestLogs(object):
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            '[%(asctime)s]-[%(levelname)s] %(filename)s--> %(funcName)s ----->%(message)s'
        )

        # 设置控制台日志信息
        console = logging.StreamHandler()
        console.setFormatter(formatter)
        console.setLevel(logging.INFO)

        # 生成文件路径
        file_name = datetime.datetime.now().strftime("%Y-%m-%d")+".log"

        # 设置文件日志信息
        file_handle = logging.FileHandler('./logs/'+file_name, mode='a', encoding='utf-8')
        file_handle.setFormatter(formatter)
        file_handle.setLevel(logging.DEBUG)

        self.logger.addHandler(console)
        self.logger.addHandler(file_handle)

    def get_log(self):
        return self.logger

    def close_link(self):
        pass


if __name__ == '__main__':
    logger = TestLogs().get_log()
    logger.debug('this is a debug log')
    logger.info('this is a info log')
    logger.error('this is a error log')
    logger.warning('this is a warning log')

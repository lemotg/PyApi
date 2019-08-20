# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 11:17
# @Author  : Rock
# @File    : utils.py
# @describe:

import random
import time


def create_phone():
    last = random.randint(999999999, 10000000000)
    phone = "9{}".format(last)
    return phone


def create_name():
    last = random.randint(99, 1000)
    name = "AutoTest{}".format(last)
    return name


def get_millis():
    millis = int(round(time.time() * 1000))
    return millis

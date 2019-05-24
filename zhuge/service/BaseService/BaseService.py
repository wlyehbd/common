#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/5/17 下午3:26
# @Author  : janguo@zhugefang.com
# @Site    :
# @File    : BaseService.py
# @Software: PyCharm


from zhuge.controller.BaseController import Executor
class BaseService(object):
    _executor = Executor()
    executor = Executor()

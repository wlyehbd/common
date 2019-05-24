#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午10:47
# @Author  : jianguo@zhugefang.com
# @Desc    :
from zhuge.controller.BaseController import Executor
class Base(object):

    _executor = Executor()
    executor = Executor()

    table = ""

    def __init__(self, *args, **kwargs):
        self.model = kwargs.get('model')
        self.table = self.model.__tablename__
        self.field = self.model.fields


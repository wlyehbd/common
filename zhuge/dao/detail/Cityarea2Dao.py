#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午6:39
# @Author  : jianguo@zhugefang.com
# @Desc    : 商圈数据层
from zhuge.dao.BaseDao.BaseMongo import BaseMongo
from zhuge.model.Cityarea2 import Cityarea2


class Cityarea2Dao(BaseMongo):
    def __init__(self, *args, **kwargs):
        super().__init__(model=kwargs.get("model", Cityarea2), conf_name=kwargs.get("conf_name", "borough"))

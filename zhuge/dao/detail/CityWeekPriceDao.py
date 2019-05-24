#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午6:39
# @Author  : jianguo@zhugefang.com
# @Desc    : 城区周均价数据层
from zhuge.dao.BaseDao.BaseMongo import BaseMongo
from zhuge.model.City_week_price import City_week_price


class CityWeekPriceDao(BaseMongo):
    def __init__(self, *args, **kwargs):
        super().__init__(model=kwargs.get("model", City_week_price), conf_name=kwargs.get("conf_name", "borough"))

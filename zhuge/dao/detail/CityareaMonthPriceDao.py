#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午6:39
# @Author  : jianguo@zhugefang.com
# @Desc    : 城区价格数据层
from zhuge.dao.BaseDao.BaseMongo import BaseMongo
from zhuge.model.Cityarea_month_price import Cityarea_month_price


class CityareaMonthPriceDao(BaseMongo):
    def __init__(self, *args, **kwargs):
        super().__init__(model=kwargs.get("model", Cityarea_month_price), conf_name=kwargs.get("conf_name", "borough"))

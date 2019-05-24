#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 下午5:20
# @Author  : Sunbowen
# @Email   : sunbowen@zhugefang.com
# @File    : CityMonthListPrice.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base


class CityMonthListPrice(Base):
    __tablename__ = 'city_month_list_price'
    fields = {
        "id": 0,
        "name": 0,
    }
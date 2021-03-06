#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 下午4:44
# @Author  : Sunbowen
# @Email   : sunbowen@zhugefang.com
# @File    : CityDayPrice.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base


class BoroughMonthPrice(Base):
    __tablename__ = 'borough_month_price'
    fields = {
        "id": 0,
        "name": 0,
    }

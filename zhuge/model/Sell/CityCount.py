#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/2 下午4:44
# @Author  : lutaixiang
# @Email   : lutaixiang@zhugefang.com
# @File    : CityCount.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base


class CityCount(Base):
    __tablename__ = 'city_count'
    fields = {
        "id": 0,
        "name": 0,
    }

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 下午2:53
# @Author  : Sunbowen
# @Email   : sunbowen@zhugefang.com
# @File    : HouseSellHistoryPrice.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base


class HouseSellHistoryPriceMongo(Base):
    __tablename__ = 'house_sell_history_price'

    fields = {
        "id": 0,
        "name": 0,
    }
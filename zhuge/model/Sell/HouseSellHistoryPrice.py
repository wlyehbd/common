#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/4 下午2:53
# @Author  : Sunbowen
# @Email   : sunbowen@zhugefang.com
# @File    : HouseSellHistoryPrice.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base
class HouseSellHistoryPrice(Base):
    __tablename__ = 'house_sell_history_price'

    fields = {
        'gov_id': 0,
        'source': 0,
        'company_id': 0,
        'now_created': 0,
        'pre_created': 0,
        'source_url': '',
        'pre_house_price': 0.0,
        'now_house_price': 0.0,
        'house_area': '',
        'house_room': 0,
        'house_floor': '',
        'borough_id': 0,
        'borough_name': '',
        'cityarea_id': 0,
        'change_type': 0,
        'change_range': 0.0,
        'change_value': 0.0,
        'type': 0,
        'cityarea2_id': 0,
        'broker_id': 0,
        'broker_phone': '',
        'source_type': 0,
    }
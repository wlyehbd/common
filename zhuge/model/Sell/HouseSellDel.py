#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 下午4:16
# @Author  : Sunbowen
# @Email   : sunbowen@zhugefang.com
# @File    : HouseSellDel.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base


class HouseSellDel(Base):
    __tablename__ = 'house_sell_del'
    fields = {
        'id': 0,
        'broker_id': 0,
        'house_price': 0.0,
        'house_desc': '',
        'house_title': '',
        'cityarea_id': 0,
        'cityarea2_id': 0,
        'house_floor': '',
        'house_topfloor': 0,
        'house_toward': 0,
        'house_room': 0,
        'house_hall': 0,
        'house_toilet': 0,
        'house_kitchen': 0,
        'house_fitment': 0,
        'house_feature': '',
        'house_built_year': '',
        'use_area': 0.0,
        'owner_name': '',
        'owner_phone': '',
        'house_support': '  ',
        'created': 0,
        'updated': 0,
        'status': 0,
        'source': 0,
        'company_id': 0,
        'source_url': '',
        'is_checked': 0,
        'click_num': 0,
        'refresh': 0,
        'house_type': 0,
        'house_totalarea': '',
        'borough_id': 0,
        'borough_name': '',
        'house_pic_unit': '',
        'house_pic_layout': '',
        'house_number': '',
        'is_fill': '',
        'is_contrast': 0,
        'deviation': 0,
        'gov_id': 0,
        'off_type': 0,
        'correlation_off_parent_id': 0,
        'vr_url': '',
        'video_url': '',
        'tag': '',
    }

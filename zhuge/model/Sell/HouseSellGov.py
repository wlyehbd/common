#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/6 下午12:09
# @Author  : Sunbowen
# @Email   : sunbowen@zhugefang.com
# @File    : HouseSellGov.py
# @Software: PyCharm
from zhuge.model.BaseModel.Base import Base


class HouseSellGov(Base):
    __tablename__ = 'house_sell_gov'

    fields = {
        'broker_id': 0,
        'house_price': 0.0,
        'house_desc': '',
        'house_title': '',
        'cityarea_id': '',
        'cityarea2_id': '',
        'house_floor': '',
        'house_topfloor': 0,
        'house_toward': '',
        'house_room': 0,
        'house_hall': 0,
        'house_toilet': 0,
        'house_kitchen': '',
        'house_fitment': '',
        'house_feature': '',
        'house_built_year': '',
        'use_area': 0.0,
        'owner_name': '',
        'owner_phone': '',
        'service_phone': '',
        'house_support': '',
        'created': 0,
        'updated': 0,
        'entry_time': 0,
        'status': 0,
        'source': 0,
        'company_id': 0,
        'source_owner': 0,
        'source_name': '',
        'app_url': '',
        'wap_url': '',
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
        'public_time': 0,
        'tag': '',
        'broker_num': 0,
        'vr_url': '',
        'video_url': '',
        'unique_key': '',
        'refresh_time': 0,
        'ctime': 0,
        'borough_address': '',
        'property_right_years': '',
        'housing_years': '',
        'visit_total_num': 0,
        'visit_num': 0,
        'company_name': '',
        'source_type': 0,
        'verify_time': 0,
        'user_id': 0,
        'verify_status': 1,
        'dial_time': 0,
        'verify_reason': '',
        'community_id': 0.0
        # 'building_type': '',
        # 'reserved1': '',
        # 'reserved2': '',
        # 'reserved3': 0,
        # 'reserved4': 0,
    }

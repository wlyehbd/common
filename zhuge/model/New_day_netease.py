# -*- coding: utf-8 -*-
"""
@author xiaofei
@email zhengxiaofei@zhuge.com
@desc 
"""
from zhuge.model.BaseModel.Base import Base

class New_day_netease(Base):
    __tablename__ = 'new_day_netease'
    fields = {
        'cityarea_id': 0,
        'complex_id': 0,
        'datetime': 0,
        'location': "",
        'borough_name': "",
        'complex_total': 0,
        'complex_price': 0.0,
        'complex_money': 0.0,
        'complex_area': 0.0,
        'complex_deg': "",
        'created': 0,
        'updated': 0
    }
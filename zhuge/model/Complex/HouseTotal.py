# -*- coding:  utf-8 -*-
"""
@desc 房源数据总量统计表
@class_name house_total
"""
from zhuge.model.BaseModel.Base import Base

class HouseTotal(Base): 
    __tablename__ = 'house_total'
    fields = {
        'id':   0,
        'city_id':  0,
        'city_spy': '',
        'city_fpy': '',
        'city_name': '',
        'year': 0,
        'month': 0,
        'type': '',
        'gov_total': 0,
        'sell_total': 0,
        'gov_totals': 0,
        'merge_totals': 0,
        'merge_total': 0,
        'added_totals': 0,
        'month_added_total': 0,
        'reslove1': 0,
        'reslove2': '',
        'ctime': 0,
        'utime': 0,
        # 'gov_info_total': 0,
        # 'gov_info_totals': 0,
        # 'merge_weight_totals': 0,
        # 'merge_weight_total': 0,
        # 'added_zhuge_totals': 0
    }

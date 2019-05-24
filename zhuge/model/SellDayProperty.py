# -*- coding: utf-8 -*-
from zhuge.model.BaseModel.Base import Base


class SellDayProperty(Base):
    # 二手房业务类型
    __tablename__ = 'sell_day_property'
    fields = {
        'created': 0,
        'updated': 0,
        'datetime': 0,
        'cityarea': '',
        'cityarea_id': 0,
        'property_type': '',
        'uni_property_type': 0,
        'volume_total': 0,
        'volume_totalarea': 0.0,
        'volume_totalprice': 0,
        'volume_price': 0,
    }

# -*- coding: utf-8 -*-
from zhuge.model.BaseModel.Base import Base


# ok
class SellDayCityarea(Base):
    __tablename__ = 'sell_day_cityarea'
    fields = {
        'created': 0,
        'updated': 0,
        'datetime': 0,
        'cityarea': '',
        'cityarea_id': 0,
        'volume_total': 0,
        'volume_totalarea': 0.0,
        'volume_totalprice': 0,
        'volume_price': 0,
        'other_total': 0,
        'other_totalarea': 0.0,
        'res_total': 0,
        'res_totalarea': 0.0,
        'res_totalprice': 0
    }

# -*- coding: utf-8 -*-
from zhuge.model.BaseModel.Base import Base


class ComplexInfo(Base):
    __tablename__ = 'new_complex_net'
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
        'updated': 0,
    }

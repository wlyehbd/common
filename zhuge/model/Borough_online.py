#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-24 下午6:39
# @Author  : jianguo@zhugefang.com
# @Desc    : 商圈数据层
from zhuge.model.BaseModel.Base import Base
class Borough_online(Base):
    __tablename__ = 'borough_online'
    # __tablename__ = 'borough_online_0415'
    fields = {
        "id": 0,
        "name": 0,
    }


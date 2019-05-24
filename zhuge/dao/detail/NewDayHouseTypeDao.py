# -*- coding: utf-8 -*-
"""
@author xiaofei
@email zhengxiaofei@zhuge.com
@desc 
"""
from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.NewDayHouseType import NewDayHouseType


class NewDayHouseTypeDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = NewDayHouseType()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

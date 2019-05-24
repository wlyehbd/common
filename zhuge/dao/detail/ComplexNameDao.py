# -*- coding: utf-8 -*-
from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.ComplexName import ComplexName


class ComplexNameDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = ComplexName()
        super().__init__(conf_name=kwargs.get("conf_name", "appraisal"),
                         model=kwargs.get("model", self.model))

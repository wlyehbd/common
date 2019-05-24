# -*- coding: utf-8 -*-
from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.Complex import Complex


class ComplexDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = Complex()
        super().__init__(conf_name=kwargs.get("conf_name", "complex"),
                         model=kwargs.get("model", self.model))

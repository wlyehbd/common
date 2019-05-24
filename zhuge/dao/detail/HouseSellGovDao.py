from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.HouseSellGov import HouseSellGov


class HouseSellGovDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = HouseSellGov()
        super().__init__(conf_name=kwargs.get("conf_name", "sell"), model=kwargs.get("model", self.model))

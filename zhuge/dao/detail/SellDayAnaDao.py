from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.SellDayAna import SellDayAna


class SellDayAnaDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = SellDayAna()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

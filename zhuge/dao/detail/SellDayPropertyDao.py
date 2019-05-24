from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.SellDayProperty import SellDayProperty


class SellDayPropertyDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = SellDayProperty()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.SellDayCityarea import SellDayCityarea


class SellDayCityareaDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = SellDayCityarea()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

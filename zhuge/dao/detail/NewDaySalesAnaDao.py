from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.NewDaySalesAna import NewDaySalesAna


class NewDaySalesAnaDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = NewDaySalesAna()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

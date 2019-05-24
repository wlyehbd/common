from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.New_day_netease import New_day_netease


class New_day_neteaseDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = New_day_netease()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", New_day_netease))

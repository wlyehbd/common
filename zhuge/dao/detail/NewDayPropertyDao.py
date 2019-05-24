from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.NewDayProperty import NewDayProperty


class NewDayPropertyDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = NewDayProperty()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.NewDayCityarea import NewDayCityarea


class NewDayCityareaDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = NewDayCityarea()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

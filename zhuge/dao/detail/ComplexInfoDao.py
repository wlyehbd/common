from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.ComplexInfo import ComplexInfo


class ComplexInfoDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = ComplexInfo()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

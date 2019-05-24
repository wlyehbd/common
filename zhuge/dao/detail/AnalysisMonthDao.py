from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.AnalysisMonth import AnalysisMonth


class AnalysisMonthDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = AnalysisMonth()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.AnalysisWeek import AnalysisWeek


class AnalysisWeekDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = AnalysisWeek()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

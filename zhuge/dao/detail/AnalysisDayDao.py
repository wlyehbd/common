from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.AnalysisDay import AnalysisDay


class AnalysisDayDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = AnalysisDay()
        super().__init__(conf_name=kwargs.get("conf_name", "analysis"), model=kwargs.get("model", self.model))

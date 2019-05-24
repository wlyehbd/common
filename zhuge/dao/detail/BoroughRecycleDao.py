from zhuge.dao.BaseDao.BaseMongo import BaseMongo
from zhuge.model.Borough_recycle import Borough_recycle


class BoroughRecycleDao(BaseMongo):
    def __init__(self, *args, **kwargs):
        super().__init__(model=kwargs.get("model", Borough_recycle), conf_name=kwargs.get("conf_name", "borough"))

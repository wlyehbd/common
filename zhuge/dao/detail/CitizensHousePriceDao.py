from zhuge.dao.BaseDao.BaseMysql import BaseMysql
from zhuge.model.CitizensHousePrice import CitizensHousePrice


class CitizensHousePriceDao(BaseMysql):
    def __init__(self, *args, **kwargs):
        self.model = CitizensHousePrice()
        super().__init__(conf_name=kwargs.get("conf_name", "sell_analysis"), model=kwargs.get("model", self.model))

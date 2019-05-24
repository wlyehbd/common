from zhuge.model.BaseModel.Base import Base


class DailyHouseSellAvgprice(Base):
    __tablename__ = 'daily_house_sell_avgprice'

    fields = {
        'id': 0,
        'type': 0,
        'date': 0,
        'price': 0,
        'cityarea_id': 0,
        'cityarea2_id': 0,
        'count_add': 0,
        'count_rise': 0,
        'count_reduce': 0,
        'count_sell': 0,
        'count_gov': 0,
        'ctime': 0,
    }

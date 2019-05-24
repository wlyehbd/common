from zhuge.model.BaseModel.Base import Base


class DailyHouseSellBoroughAvgprice(Base):
    __tablename__ = 'daily_house_sell_borough_avgprice'

    fields = {
        'id': 0,
        'type': 0,
        'date': 0,
        'price': 0,
        'cityarea_id': 0,
        'cityarea2_id': 0,
        'borough_id': 0,
        'borough_name': "",
        'count_add': 0,
        'count_rise': 0,
        'count_reduce': 0,
        'count_sell': 0,
        'count_gov': 0,
        'ctime': 0,
        'count_rent_gov': 0,
    }

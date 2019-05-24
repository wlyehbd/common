from zhuge.model.BaseModel.Base import Base


class Cityarea2MonthPrice(Base):
    __tablename__ = 'cityarea2_month_price'

    fields = {
        "id": 0,
        "cityarea2_id": 0,
        "year": 0,
        "yymm": 0,
        "month": 0,
        "date": 0,
        "time": 0,
        "cms_id": 0,
        "reserve2": "",
        "avg_price": 0
    }

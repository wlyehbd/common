from zhuge.model.BaseModel.Base import Base


# ok
class SellDayAna(Base):
    __tablename__ = 'sell_day_ana'
    fields = {
        "id": 0,
        "created": 0,
        "updated": 0,
        "datetime": 0,
        "listing_total": 0,
        "listing_totalarea": 0.0,
        "listing_house_total": 0,
        "listing_house_totalarea": 0.0,
        "unsold_total": 0,
        "unsold_totalarea": 0.0,
        "unsold_house_total": 0,
        "unsold_house_totalarea": 0.0,
        "volume_total": 0,
        "volume_totalarea": 0.0,
        "volume_totalprice": 0,
        "volume_price": 0,
        "bus_total": 0,
        "bus_totalarea": 0.0,
        "bus_totalprice": 0,
        "bus_price": 0,
        "work_total": 0,
        "work_totalarea": 0.0,
        "work_totalprice": 0,
        "work_price": 0,
        "park_total": 0,
        "park_totalarea": 0.0,
        "park_totalprice": 0,
        "park_price": 0,
        "res_total": 0,
        "res_totalarea": 0.0,
        "res_totalprice": 0,
        "res_price": 0,
        'other_total': 0,
        'other_totalarea': 0.0,
        'other_totalprice': 0,
    }

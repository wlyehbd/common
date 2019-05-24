from zhuge.model.BaseModel.Base import Base


# ok
class NewDayCityarea(Base):
    __tablename__ = 'new_day_cityarea'
    fields = {
        'created': 0,
        'updated': 0,
        'datetime': 0,
        'cityarea': '',
        'cityarea_id': 0,
        'volume_total': 0,
        'volume_totalarea': 0.0,
        'volume_totalprice': 0,
        'volume_price': 0,
        'res_total': 0,
        'res_totalarea': 0.0,
        'sold_total': 0,
        'sold_totalarea': 0.0,
        'other_total': 0,
        'other_totalarea': 0.0,
        'res_sold_total': 0,
        'presale_total': 0,
        'presale_totalarea': 0.0,
    }

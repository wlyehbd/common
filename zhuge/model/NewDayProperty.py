from zhuge.model.BaseModel.Base import Base


# ok
class NewDayProperty(Base):
    # 按照物业类型 
    __tablename__ = 'new_day_property'
    fields = {
        'datetime': 0,
        'cityarea_id': 0,
        'cityarea': '',
        'property_type': '',
        'uni_property_type': 0,
        'volume_total': 0,
        'volume_totalarea': 0.0,
        'volume_totalprice': 0,
        'volume_price': 0,
        'sold_total': 0,
        'sold_totalarea': 0.0,
        'presale_total': 0,
        'presale_totalarea': 0.0,
        'created': 0,
        'updated': 0,
    }

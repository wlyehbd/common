from zhuge.model.BaseModel.Base import Base


class ComplexHistoryPrice(Base):
    __tablename__ = 'complex_history_price'
    fields = {
        "id": 0,
        "complex_id": 0,
        "cms_id": 0,
        "avg_price": 0,
        "max_price": '',
        "min_price": '',
        "price_desc": '',
        "set_price": 0,
        "periphery_price": '',
        "property_type": 0,
        "sp_type": 0,
        "ap_type": 0,
        "type": 0,
        "trend": 0,
        "add_time": 0,
        "title": '',

    }

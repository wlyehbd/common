from zhuge.model.BaseModel.Base import Base


class NewMonthAnalysis(Base):
    __tablename__ = 'new_month_analysis'
    fields = {
        'created': 0,
        'updated': 0,
        'datetime': 0,
        'total': 0,
        'price': 0,
        'unit_price': 0,
        'totalprice': 0,
        'totalarea': 0.0,
        'cityarea': '',
        'property': '',
        'loop_line': '',
        'service_text': '',
        'service_type': 0,
        'house_type_text': '',
        'cityarea_id': 0,
        'pricetype': 0,
        'house_type': 0,
        'uni_loop_line': 0,
        'pricesum_type': 0,
        'totalareatype': 0,
        'property_type': 0,
        'special_type': 0
    }

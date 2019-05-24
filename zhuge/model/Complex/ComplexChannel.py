"""
@desc 新房ComplexChannel表实体类
@class_name ComplexChannel
"""
from zhuge.model.BaseModel.Base import Base


class ComplexChannel(Base):
    __tablename__ = 'dm_complex_channel'

    fields = {
        'id': 0,
        'city_id': 0,
        'city_fpy': '',
        'city_spy': '',
        'city_name': '',
        'is_b': 0,
        'sort': 0,
        'city_status': 0,
        'source_id': 0,
        'source_name': '',
        'source_pinyin': '',
        'source_url': '',
        'priority': 0,
        'spider_status': 0,
        'abbr': '',
        'service_fee': '',
        'service_fee_desc': '',
        'new_agency_fee': 0,
        'is_show': 0,
        'is_proxy': 0,
        'logo_url': '',
        'old_logo_url': '',
        'old_small_logo_url': '',
        'small_logo_url': '',
        'pid': 0,
        'is_hot': 0,
        'is_open': 0,
        'is_pay_type': 0,
        'newhouse_db': 0,
        'ctime': 0,
        'utime': 0,
    }

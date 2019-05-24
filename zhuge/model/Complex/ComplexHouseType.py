from zhuge.model.BaseModel.Base import Base


class ComplexHouseType(Base):
    __tablename__ = 'complex_housetype'
    fields = {
        'id': 0,
        'complex_id': 0,
        'source_id': 0,
        'house_pic_id': 0,
        'source_url': '',
        'housetype_tag': '',
        'house_room': 0,
        'house_hall': 0,
        'house_toilet': 0,
        'house_kitchen': 0,
        'housetype_toward': '',
        'house_totalarea': 0.00,
        'house_topfloor': '',
        'housetype_saletype': '',
        'house_layout': '',
        'reference_totalprice': 0.00,
        'reference_price': 0,
        'reference_down_payment': '',
        'housetype_desc': '',
        'upload_status': 0,
        'uv_count': 0,
        'reference_month_payment': '',
        'ctime': 0,
        'utime': 0,
        'sortweight': 0,
        'unique_key': '',
        'pic_source_url': '',
        'housetype_kindname': '',
        'cms_id': 0,
        'layout_source_id': 0,
        'is_delete': 0
    }

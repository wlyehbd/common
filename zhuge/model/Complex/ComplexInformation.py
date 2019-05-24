from zhuge.model.BaseModel.Base import Base


class ComplexInformation(Base):
    __tablename__ = 'complex_information'
    fields = {
        'id': 0,
        'complex_id': 0,
        'source_id': 0,
        'building_title': '',
        'building_content': '',
        'pic_source_url': '',
        'pic_url': '',
        'source_url': '',
        'building_time': '',
        'ctime': 0,
        'utime': 0,
        'upload_status': 0,
        'unique_key': '',
        'new_unique_key': '',
        'cms_id': 0,
        'source': '',
        'is_delete':0
    }

from zhuge.model.BaseModel.Base import Base


class ComplexLicense(Base):
    __tablename__ = 'complex_license'
    fields = {
        'id': 0,
        'complex_id': 0,
        'source_id': 0,
        'pubtime': '',
        'building_info': '',
        'license': '',
        'unique_key': '',
        'source_url': '',
        'cms_id': 0,
        'is_delete': 0
    }

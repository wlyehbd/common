from zhuge.model.BaseModel.Base import Base


class CmsIds(Base):
    __tablename__ = 'cms_ids'
    fields = {
        "cms_id": 0,
        "city": "",
        "complex_id": 0,
        "ctime": 0
    }

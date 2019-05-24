from zhuge.model.BaseModel.Base import Base


class DMComplexSource(Base):
    __tablename__ = 'dm_complex_channel'

    fields = {
        "id": 0,
        "city_id": 0,
        "source_id": 0,
        "priority": 0,
        "source_name": ""
    }

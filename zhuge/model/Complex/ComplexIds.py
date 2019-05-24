from zhuge.model.BaseModel.Base import Base


class ComplexIds(Base):
    __tablename__ = 'complex_ids'
    fields = {
        "id": 0,
        "complex_id": "",
        "status": 0,
        "utime": 0,
        "ctime": 0
    }

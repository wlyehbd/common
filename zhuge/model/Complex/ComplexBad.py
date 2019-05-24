from zhuge.model.BaseModel.Base import Base


class ComplexBad(Base):
    __tablename__ = 'complex_bad'

    fields = {
        "id": 0,
        "source_id": 0,
        "city_id": 0,
        "source_url": "",
        "cityarea_id": "",
        "cityarea2_id": "",
        "complex_name": "",
        "bad_type": 0,
        "utime": 0,
        "ctime": 0,
        "url_bad": 0,
        "complex_pic": 0,
        "complex_housetype": 0,
        "complex_information": 0,
        "complex_comment": 0,
        "complex_license": 0,
    }

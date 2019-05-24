from zhuge.model.BaseModel.Base import Base

class ComplexDeliver(Base):
    __tablename__ = "complex_deliver"

    fields = {
        "id": 0,
        "complex_id": 0,
        "cms_id": 0,
        "first_delivertime": 0,
        "deliver_details": "",
        "deliver_history": "",
        "first_sale": 0,
        "sale_details": "",
        "sale_history": "",
        "ctime": 0,
        "utime": 0,
    }

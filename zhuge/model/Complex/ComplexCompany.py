from zhuge.model.BaseModel.Base import Base


class ComplexCompany(Base):
    __tablename__ = "company"

    fields = {
        "id": 0,
        "name": "",  # 机构名称
        "address": "",  # 机构地址
        "type": 0,  # 机构类别   1:开发商，2:物业公司，3学校
        "desc": 0,  # 机构简介
        "phone": "",  # 机构电话
        "lng_lat": "",  # 机构位置
        "web_url": "",  # 网站地址
        "email": "",  # 邮箱
        "fax": "",  # 传真
    }

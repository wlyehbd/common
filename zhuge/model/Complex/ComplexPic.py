from zhuge.model.BaseModel.Base import Base


class ComplexPic(Base):
    __tablename__ = 'complex_pic'

    fields = {
        'id': 0,
        'complex_id': 0,
        'housetype_id': '',
        'source_id': 0,
        'source_url': "",
        'upload_status': 0,
        'pic_type': "",
        'pic_source_url': "",
        'nofinger_pic_url': 0,
        'pic_url': "",
        'unique_key': "",
        'ctime': 0,
        'utime': 0,
        'addfinger_pic_url': '',
        'vr_video_url': '',
        'vr_video_pic': '',
        'cms_id': 0,
        'vr_source_url': '',
        'vr_source_pic': '',
        'is_delete': 0
    }
from zhuge.model.BaseModel.Base import Base


class ComplexComment(Base):
    __tablename__ = 'complex_comment'

    fields = {
        'id': 0,
        'complex_id': 0,
        'source_id': 0,
        'comment_source': '',
        'comment_showtime': '',
        'comment_time': 0,
        'comment_url': '',
        'comment_content': '',
        'upload_status': 0,
        'pic_url': '',
        'pic_source_url': '',
        'comment_user': '',
        'ctime': 0,
        'utime': 0,
        'unique_key': '',
        'city_id': 0,
        'title': '',
        'vote': 0,
        'user_agent': 0,
        'overall': 0,
        'environment': 0,
        'charms': 0,
        'traffic': 0,
        'position': 0,
        'price': 0,
        'cms_id': 0,
        'is_delete': 0
    }

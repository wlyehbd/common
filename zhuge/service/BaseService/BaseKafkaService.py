from zhuge.service.BaseService.BaseService import BaseService

from zhuge.dao.BaseDao.BaseKafka import BaseKafka


class BaseKafkaService(BaseService):
    def __init__(self):
        pass

    def producer(self, *args, **kwargs):
        return BaseKafka(conf_name=kwargs.get("conf_name")).kafka_producer(*args, **kwargs)

    def consumer(self, *args, **kwargs):
        return BaseKafka(conf_name=kwargs.get("conf_name")).kafka_consumer(*args, **kwargs)

if __name__ == '__main__':
    body={"data": "test"}
    BaseKafkaService().producer(conf_name="sell", topic="sell-house-data", params=body)
# -*- coding: utf-8 -*-
"""
@author xiaofei
@email zhengxiaofei@zhuge.com
@auth
@desc kafka连接池
"""
try:
    from kafka import KafkaProducer
    from kafka import KafkaConsumer
except Exception as e:
    print('没有安装pykafka')
from zhuge.apps.config.ConfigService import ConfigService
import logging
import contextlib



class KafkaDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        hosts_conf = ConfigService.get_kafka_conf()
        self.kafka_config = hosts_conf.get(self.conf_name)

    @contextlib.contextmanager
    def getProducerConn(self, *args, **kwargs):
        if self.kafka_config:
            conn = KafkaProducer(bootstrap_servers=self.kafka_config, compression_type='gzip')
        else:
            print('kafka配置找不到')
            return
        try:
            yield conn
        except Exception as e:
            logging.error("连接kafka生产者失败:", e)
        finally:
            conn.close()
        return conn

    @contextlib.contextmanager
    def getConsumerConn(self, *args, **kwargs):
        if self.kafka_config:
            conn = KafkaConsumer(bootstrap_servers=self.kafka_config)
        else:
            print('kafka配置找不到')
            return
        try:
            yield conn
        except Exception as e:
            logging.error("连接kafka消费者失败:", e)
        finally:
            conn.close()
        return conn

    # @staticmethod
    # def getKafkaConn(**kwargs):
    #     conf_name = kwargs.get("conf_name")
    #     server = KafkaDB.pool.get(conf_name, None)
    #     if not server:
    #         hosts_conf = ConfigService.get_kafka_conf()
    #         hosts = hosts_conf.get(conf_name, "")
    #         if hosts:
    #             client = KafkaClient(hosts=hosts)
    #         else:
    #             print('kafka配置找不到')
    #             return
    #         KafkaDB.pool.setdefault(conf_name, client)
    #         return client
    #     return server




        # topics_key = bytes(name, encoding='utf8')
        # topic = client.topics[topics_key]
        # consumer = topic.get_simple_consumer(
        #     auto_commit_enable=True,
        #     auto_commit_interval_ms=1,
        #     consumer_id=topics_key)



if __name__ == '__main__':
    server = KafkaDB.getKafkaConn(conf_name = 'thor')
    key = bytes('test', encoding='utf8')
    print(key)
    topic = server.topics[key]
    consumer = topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print("consumer message:", message.offset)
            print(message.value)
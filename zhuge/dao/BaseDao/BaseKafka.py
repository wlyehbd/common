#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : tanghan@zhugefang.com
# @Desc    :
from zhuge.databases.dbfactory.dbfactory import dbfactory
from zhuge.dao.Base import Base
from kafka import TopicPartition
import json


class BaseKafka(Base):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        self.conn = dbfactory.create_db(conf_name=self.conf_name, db_type="db_kafka")

    # 生产者
    def kafka_producer(self, *args, **kwargs):
        try:
            with self.conn.getProducerConn() as producer:
                topic = kwargs.get("topic")
                params = kwargs.get("params")
                if topic and params:
                    if not isinstance(params, str):
                        params = json.dumps(params)
                    producer.send(topic, bytes(params, encoding='utf8'))
                    # producer.flush()
                else:
                    print("topic为空 or params为空！")
                    return
                return True

        except Exception as e:
            print("kafka_producer", e)
            return False

    # 消费者
    def kafka_consumer(self, *args, **kwargs):
        try:
            with self.conn.getConsumerConn() as consumer:
                topic = kwargs.get("topic")
                consumer.assign([TopicPartition(topic, 3)])
                data = []
                for message in consumer:
                    if message:
                        data.append(json.loads(message.value))
                return data

        except Exception as e:
            print("kafka_consumer", e)
            return False
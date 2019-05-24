#!/usr/bin/env python
# coding:utf-8
# Author:   --<lucas>
# Purpose: MongoDB的使用
# Created: 2017/06/22
from pymongo import MongoClient
from zhuge.apps.config.ConfigService import ConfigService

from zhuge.apps.config.CitySouceMapping import get_db
import logging
import contextlib


class MongoDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        mongo_conf = ConfigService.get_mongo_conf()
        self.conf = mongo_conf.get(self.conf_name)
    __pool = {}

    @contextlib.contextmanager
    def getMongoConn(self, *args, **kwargs):
        link_type = kwargs.get("link_type", 'default')
        conf = self.conf.get(link_type)
        connect_name = link_type + self.conf_name
        conn = MongoDB.__pool.get(connect_name)

        city = kwargs.get("city")
        db_name = kwargs.get("db_name")
        db_name = db_name if db_name else get_db(type=self.conf_name, city=city)
        if not conn:
            uri = conf.get("url")
            host = conf.get("host")
            port = conf.get("port")
            user = conf.get("username", "")
            passwd = conf.get("password", "")
            maxPoolSize = conf.get("maxPoolSize", 50)
            maxIdleTimeMS = conf.get("maxIdleTimeMS", 10)
            if not uri:
                if user and passwd:
                    uri = f"mongodb://{user}:{passwd}@{host}:{port}"
                else:
                    uri = f"mongodb://{host}:{port}"
            conn = MongoClient(uri,maxPoolSize=maxPoolSize,maxIdleTimeMS=maxIdleTimeMS)
            MongoDB.__pool.setdefault(connect_name, conn)
        try:
            client = conn.get_database(db_name)
            yield client
        except Exception as e:
            logging.error('ERROR', e)
        finally:
            # conn.close()
            # conn.close_cursor()
            pass

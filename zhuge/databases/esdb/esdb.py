#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-20 上午10:56
# @Author  : jianguo@zhugefang.com
# @Desc    :
from zhuge.apps.config.ConfigService import ConfigService
from zhuge.apps.config.CitySouceMapping import getEsConfigName
from elasticsearch import Elasticsearch
import contextlib


class EsDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")
        # es_config = ConfigService.get_es_config()
        # db_config = es_config.get(self.conf_name)
        #
        # self.host = db_config.get("host")
        # self.port = db_config.get("port")
        # self.user = db_config.get("username", "")
        # self.passwd = db_config.get("password", "")
        # self.maxsize = db_config.get('maxsize', 10)

    __pool = {}

    @contextlib.contextmanager
    def get_conn(self, **kwargs):
        city = kwargs.get("city","")
        # 通过城市和业务获取配置
        if city == "": # 没有城市用默认配置
            conf_name = self.conf_name
        else:
            conf_name = getEsConfigName(city=city,service_type=self.conf_name)
        es = EsDB.__pool.get(conf_name)
        if es and not es.ping():
            es = None
        if not es:
            es_config = ConfigService.get_es_config()
            db_config = es_config.get(conf_name)
            host = db_config.get("host")
            maxsize = db_config.get('maxsize', 10)
            es = Elasticsearch(hosts=host, maxsize=maxsize)
            es.ping()
            EsDB.__pool.setdefault(self.conf_name, es)
        yield es

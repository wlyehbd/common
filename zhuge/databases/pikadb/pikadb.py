# -*- coding: utf-8 -*-s
import redis
from zhuge.apps.config.ConfigService import ConfigService



class PikaDB(object):
    def __init__(self, *args, **kwargs):
        pass

    pool = {}

    @staticmethod
    def getPikaConn(**kwargs):
        conf_name = kwargs.get("conf_name")
        link_type = kwargs.get("link_type", 'default')
        pool = PikaDB.pool.get(conf_name + link_type, None)
        # if pool and not pool.ping():
        #     pool = None
        if not pool:
            pika_conf = ConfigService.get_pika_conf()
            conf = pika_conf.get(conf_name, {}).get(link_type, None)
            if not conf:
                print("pika配置未找到")
                return
            db_url = conf.get("db_url", "")
            host = conf.get("host", "127.0.0.1")
            port = conf.get("port", 6379)
            db = conf.get("db", 0)
            max_connections = conf.get("max_connections", 50)
            if db_url:
                pool = redis.StrictRedis.from_url(url=db_url)
            else:
                pool = redis.ConnectionPool(host=host, port=port, db=db, max_connections=max_connections)
            PikaDB.pool.setdefault(conf_name + link_type, pool)
        server = redis.StrictRedis(connection_pool=pool)
        return server

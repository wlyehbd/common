# -*- coding: UTF-8 -*-
import pymysql
from zhuge.apps.config.CitySouceMapping import get_db, getConfigName
from zhuge.apps.config.ConfigService import ConfigService
import contextlib
import logging
from DBUtils.PooledDB import PooledDB

class MysqlDB(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")

    __pool = {}

    @contextlib.contextmanager
    def get_conn(self, *args, **kwargs):
        city = kwargs.get("city")
        link_type = kwargs.get("link_type", 'default')
        conf_name = getConfigName(city=city, type=self.conf_name)
        connect_name = link_type + conf_name
        conn_pool = MysqlDB.__pool.get(connect_name)
        db_name = get_db(type=conf_name, city=city)
        if conn_pool:
            pass
        else:
            # 获取主从连接
            mysql_conf = ConfigService.get_mysql_conf()
            conf1 = mysql_conf.get(conf_name)
            conf = conf1.get(link_type)
            host = conf.get("host")
            port = conf.get("port")
            user = conf.get("user")
            passwd = conf.get("passwd")
            mincached = conf.get("mincached",1)
            maxcached = conf.get("maxcached",1)
            maxconnections = conf.get("maxconnections",1)
            conn_pool = PooledDB(creator=pymysql,blocking=True, host=host, port=port, user=user,mincached=mincached, maxcached=maxcached, maxconnections=maxconnections, password=passwd, charset="utf8")
            MysqlDB.__pool.setdefault(connect_name, conn_pool)
        conn = conn_pool.connection()
        conn._con._con.select_db(db_name)
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        try:
            yield cursor
            conn.commit()
        except Exception as e:
            conn.rollback()
            logging.error(e)
        finally:
            cursor.close()
            conn.close()

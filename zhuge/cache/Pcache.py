#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午11:28
# @Author  : jianguo@zhugefang.com
# @Desc    : dao 缓存装饰器

from zhuge.databases.dbfactory.dbfactory import dbfactory
from zhuge.apps.config.ConfigService import ConfigService
import json
import time
import logging,os,sys
logger = logging.getLogger("lowercache")
logger_content = logging.getLogger("cache_content")

class Pcache(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")  # 缓存地址
        self.key = kwargs.get("key")  # 缓存key
        self.time = kwargs.get("time", 86400)  # 缓存失效时间
        self.update = kwargs.get("update", [])  # 更新数据清空缓存
        self.pre = "newcache_"

    def __call__(self, func):
        """
        :param func:
        :return:
        """

        def wrapper(*args, **kwargs):
            city = kwargs.get("city", "default")
            class_name = list(args).pop().__class__.__name__
            func_name = func.__name__
            # hashkey：【城市】【类名【函数名称】
            pika_conf = ConfigService.get_pika_conf()
            prefix = pika_conf.get(self.conf_name).get('pre')
            name = self.pre + prefix + city + "." + class_name + "." + func_name
            cache_key = kwargs.get(self.key)
            cache_type = 0
            st = time.time()
            if self.update:  # 更新清理缓存
                cache_type = 2
                for key in self.update:
                    self.del_cache(name=self.pre + prefix + city + "." + class_name + "." + key, keys=cache_key)
                result = func(*args, **kwargs)
            else:
                result = self.pull_cache(name=name, key=cache_key)
                if not result:
                    # 未查询到缓存
                    result = func(*args, **kwargs)  # 查询数据
                    if result:
                        cache_type = 1
                        # 添加缓存
                        self.push_cache(name=name, key=cache_key, value=result)
            # logging.debug("cache", extra={"fun_name": func_name, "cache_type": cache_type, "fun_time": time.time()-st, "project": self.pre})
            return result
        return wrapper

    def push_cache(self, name, key, value):
        """
        :param name:
        :param key:
        :param value:
        :desc 添加缓存
        :return:
        """
        try:
            redis_search = dbfactory.create_db(conf_name=self.conf_name, db_type="db_pika", link_type="default")
            data = {"data": value, "time": time.time()}
            result = redis_search.hset(name=name, key=key, value=json.dumps(data))
            if self.time: # 默认有失效时间就给大key设置失效时间
                redis_search.expire(name=name, time=self.time)
            return result

        except Exception as e:
            return None

    def pull_cache(self, name, key):
        """
        :param name:
        :param key:
        :desc #获取缓存
        :return:
        """
        times = int(time.time())
        timeArray = time.localtime(times)
        otherStyleTime = time.strftime("%Y-%m-%d %H:%M", timeArray)
        day = otherStyleTime.split(" ")[0]
        hm =  otherStyleTime.split(" ")[1]
        logkey = "cache_log_y_"+day
        nologkey = "cache_log_n_"+day
        try:
            redis_search = dbfactory.create_db(conf_name=self.conf_name, db_type="db_pika", link_type="slave1")
            try:
                rate = float(redis_search.get("cache_rate") or 1)
            except Exception as e1:
                print("pull_cache",e1)
            data = redis_search.hget(name=name, key=key)
            if data:
                data = json.loads(data)
                cache_time = data.get("time", 0)
                if self.time == 0 or cache_time+self.time*rate>times: # 未失效直接返回
                    # redis_search.hincrby(logkey,hm)
                    return data.get("data", None)
            #  失效直接返回None
            # redis_search.hincrby(nologkey, hm)
            return None
            # return redis_search.hget(name=name, key=key)
        except Exception as e:
            print(name,e)
            return None


    def del_cache(self, name, keys):
        """
        :param name:
        :param keys:
        :param 删除缓存
        :return:
        """
        try:
            redis_search = dbfactory.create_db(conf_name=self.conf_name, db_type="db_pika", link_type="default")
            return redis_search.hdel(name, keys)
        except Exception as e:
            return None


class Delcache(object):
    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")  # 缓存地址
        self.update = kwargs.get("update", [])  # 更新数据清空缓存
        self.pre = "newcache_"

    def __call__(self, func):
        """
        :param func:
        :return:
        """

        def wrapper(*args, **kwargs):
            city = kwargs.get("city", "default")
            class_name = list(args).pop().__class__.__name__
            func_name = func.__name__
            # hashkey：【城市】【类名【函数名称】
            pika_conf = ConfigService.get_pika_conf()
            prefix = pika_conf.get(self.conf_name).get('pre')
            st = time.time()
            for key in self.update:
                self.del_cache(name=self.pre + prefix + city + "." + class_name + "." + key)
            result = func(*args, **kwargs)
            logging.debug("cache", extra={"fun_name": func_name, "cache_type": "del", "fun_time": time.time()-st, "project": self.pre})
            return result
        return wrapper

    def del_cache(self, name):
        try:
            redis_search = dbfactory.create_db(conf_name=self.conf_name, db_type="db_pika", link_type="default")
            return redis_search.delete(name)
        except Exception as e:
            return None


class LowerPcache(Pcache):

    def __init__(self, *args, **kwargs):
        self.conf_name = kwargs.get("conf_name")  # 配置名称
        self.key = kwargs.get("key")  # 缓存field在参数中变量名
        self.time = kwargs.get("time", 0) # 缓存失效时间
        self.pre = "lowercache_" # 前缀

    def __call__(self, func):
        """
        :param func:
        :return: wrapper
        """

        def wrapper(*args, **kwargs):
            st = time.time() # 开始时间戳
            # 开始拼接缓存key和field
            city = kwargs.get("city", "default") # 城市
            class_name = list(args).pop().__class__.__name__ # 类名
            func_name = func.__name__ # 函数名
            prefix = ConfigService.get_pika_conf().get(self.conf_name).get('pre') # 获取pika配置中二级前缀
            # hashkey：【城市】【类名【函数名称】
            name = self.pre + prefix + city + "." + class_name + "." + func_name

            cache_key = kwargs.get(self.key) # 通过变量名获取缓存field的值

            # 从pika降级缓存开关值。
            pika_search = dbfactory.create_db(conf_name=self.conf_name, db_type="db_pika", link_type="slave1")
            cache_type = int(pika_search.get("lower_pcache") or 0) # 0超时再走缓存，1直接走缓存

            # 开始请求数据 正常情况下插入缓存并返回结果
            if cache_type == 0: # 降级模式
                result = {}
                try:
                    result = func(*args, **kwargs)  # 查询数据
                    if result:
                        self.push_cache(name=name, key=cache_key, value=json.dumps(result))
                    # 降级模式 正常状态
                    logger.info("lowcache", extra={"fun_name": func_name, "cache_type": 0,
                                              "fun_time": time.time() - st, "project": prefix})

                    logger_content.debug({"name": name, "cache_key": cache_key, "result": result})
                    return result
                except Exception as e:
                    print("func执行异常", e)
                    # cache_type == 1

             # 查询到缓存就返回数据
            result = self.pull_cache(name=name, key=cache_key)
            if result:
                result = json.loads(result)
                logger.info("lowcache", extra={"fun_name": func_name, "cache_type":2 ,
                                                 "fun_time": time.time() - st, "project": prefix})

                logger_content.debug({"name": name, "cache_key": cache_key, "result": result})
                return result

            # 查询缓存模式 并且没有数据 需要执行func 获取数据
            if cache_type == 1:
                try:
                    result = func(*args, **kwargs)  # 执行函数
                    if result:
                        self.push_cache(name=name, key=cache_key, value=json.dumps(result))
                    logger.info("lowcache", extra={"fun_name": func_name, "cache_type": 1,
                                                  "fun_time": time.time() - st, "project": prefix})
                    logger_content.debug({"name": name, "cache_key": cache_key, "result": result})
                    return result
                except Exception as e:
                    print("缓存模式下func执行异常", e)
                    logger.info("lowcache", extra={"fun_name": func_name, "cache_type": 4,
                                                "fun_time": time.time() - st, "project": prefix})
            logger_content.debug({"name": name, "cache_key": cache_key, "result": result})
            return result or {}

        return wrapper


# -*- coding: utf-8 -*-
import requests
import json
from zhuge.cache.Pcache import Pcache


def City(city, type):
    jsons = dict()
    if isinstance(city, str):
        jsons.setdefault("city", city)
    if isinstance(type, str):
        jsons.setdefault("type", type)
    data = requests.post(url="http://config.dapi.zhugefang.com/config/getCity", json=jsons)
    result = json.loads(data.content)["data"]
    return result


def CityInfo(where):
    jsons = dict()
    page = {
        "index": 1,
        "size": 500
    }
    jsons.setdefault("page", page)
    filter = {}
    if where and isinstance(where, dict):
        for i, k in where.items():
            filter.setdefault(i, k)
    jsons.setdefault("filter", filter)
    data = requests.post(url="http://config.dapi.zhugefang.com/config/getcityinfo", json=jsons)
    result = json.loads(data.content)["data"]
    return result


def CityInterval(city="bj", city_last="sansha"):
    jsons = dict()
    jsons.setdefault("city", city)
    jsons.setdefault("city_last", city_last)
    data = requests.post(url="http://config.dapi.zhugefang.com/config/getCityConfig", json=jsons)
    result = json.loads(data.content)["data"]
    return result


class CityConfigService(object):
    @Pcache(conf_name='borough_api', key="where")
    def get_cityinfo(self, **kwargs):
        """
        城市详细信息服务
        :param kwargs:
        @where string 筛选条件 (缓存key)
            name: 模糊查询
            id: []
            sell_db: 1(旧), 2(新)
            rent_db: 1(旧), 2(新)
            city_level: 1,2,3,4,5,6
            is_b: True
            is_sell: True
            is_apartment: True
            is_newhouse: True
            is_rent: True
        :return:

        """
        where = kwargs.get("where", "{}")
        where = json.loads(where)
        return CityInfo(where=where)

    @Pcache(conf_name='borough_api', key="cache_key")
    def get_city(self, **kwargs):
        """
        城市基础信息服务
        :param kwargs:
        :return:
        """
        city = kwargs.get("city", "")
        type = kwargs.get("type", "")
        return City(city=city, type=type)


if __name__ == '__main__':
    # a = CityConfigService().get_cityinfo(city="bj", where='{"is_b": 1}')
    a = CityConfigService().get_city(city="sh", cache_key="sh_")
    print(a)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-10-10 下午8:25
# @Author  : jianguo@zhugefang.com
# @Desc    : 公共查询es语句
import json, random
from zhuge.service.BaseService.BaseService import BaseService


class BaseSearchDSL(BaseService):
    nested = {}
    # 等值查询字段列表
    equal = ()
    # text分词搜索字段
    match = ()
    # keyword不分词搜索字段
    wildcard = ()
    # 范围查询字段列表
    region = ()
    # 区域范围
    geos = ()
    # 等值多选
    checkbox = ()
    # 坐标查询
    point = ()

    def params_mapping(self, pms):
        """
        # @Time    : 17-10-14 下午17:29
        # @Author  : jianguo@zhugefang.com
        # @Desc    : 参数映射(不同的业务实现不同的参数映射)
        :param pms:
        :return:
        """
        return pms

    def _produce_aggs(self, aggsdict):
        # full type:
        # {
        #     "groupby": "color",
        #     "name": "aggs_color",
        #     "path": "nested path",
        #     "size": 10
        #     "ops": {
        #         "field": "price",
        #         "op": "avg",
        #         "name": "avg_price"
        #     }
        # }
        # short type: "color"

        if isinstance(aggsdict, dict):
            group_by = aggsdict.get("groupby", "")
            group_name = aggsdict.get("name", "aggs_{}".format(group_by))
            _size = aggsdict.get("size", 10)
            ops = aggsdict.get("ops", None)
            path = self.nested.get(group_by, None) if "path" not in aggsdict else aggsdict["path"]

            res = {
                group_name: {
                    "terms": {
                        "field": group_by,
                        "size": _size
                    }
                }
            }

            if not ops is None:
                op_field = ops["field"]
                op = ops["op"]
                op_name = ops.get("name", "{}_{}".format(op, op_field))
                op_res = {
                    op_name: {
                        op: {
                            "field": op_field
                        }
                    }
                }
                if (op_field in self.nested) or ops.get("path", None):
                    op_path = self.nested[op_field] if "path" not in ops else ops["path"]
                    if (path and op_path != path):
                        raise ValueError("Error file: {} class: {} function: ".format(__file__,
                                                                                      self.__calss__.__name__,
                                                                                      "_produce_aggs"))
                    op_nested_name = "nested_{}".format(op_field)
                    op_res[op_name][op]["field"] = "{}.{}".format(op_path, op_field)
                    res[group_name]["aggs"] = {
                        op_nested_name: {
                            "nested": {
                                "path": op_path
                            },
                            "aggs": op_res
                        }
                    }

                else:
                    res[group_name]["aggs"] = op_res

            # if (group_by in self.nested) or aggsdict.get("path", None):
            if path:
                path = self.nested[group_by] if "path" not in aggsdict else aggsdict["path"]
                nested_name = "nested_{}".format(group_by)
                res[group_name]["terms"]["field"] = "{}.{}".format(path, group_by)
                return {
                    nested_name: {
                        "nested": {
                            "path": path
                        },
                        "aggs": res
                    }
                }
            return res

        elif isinstance(aggsdict, str):
            group_by = aggsdict
            group_name = "aggs_{}".format(group_by)
            res = {
                group_name: {
                    "terms": {
                        "field": group_by
                    }
                }
            }

            if group_by in self.nested:
                path = self.nested[group_by]
                nested_name = "nested_{}".format(group_by)
                res[group_name]["terms"]["field"] = "{}.{}".format(path, group_by)
                return {
                    nested_name: {
                        "nested": {
                            "path": path
                        },
                        "aggs": res
                    }
                }
            return res

    def produce_aggs(self, aggs_params):
        if isinstance(aggs_params, dict):
            return self._produce_aggs(aggs_params)

        elif isinstance(aggs_params, str):
            return self._produce_aggs(aggs_params)

        elif isinstance(aggs_params, list):
            if len(aggs_params) == 1:
                return self._produce_aggs(aggs_params[0])

            def add_path(mdict, path):
                for k, v in mdict.items():
                    if k == "field":
                        mdict[k] = "{}.{}".format(path, v)
                    if isinstance(v, dict):
                        add_path(v, path)

            aggslist = [self._produce_aggs(agg) for agg in aggs_params]
            N = len(aggslist)

            for i in range(N - 2, -1, -1):
                # zhi you yige key aggs_name or nested_name
                assert len(aggslist[i]) == 1, "Error file: {} class: {} function: ".format(__file__,
                                                                                           self.__calss__.__name__,
                                                                                           "produce_aggs")
                key0 = list(aggslist[i])[0]
                if "terms" in aggslist[i][key0]:  # aggs_  key0 zi ding yi aggs_name
                    aggslist[i][key0].setdefault("aggs", {}).update(aggslist[i + 1])
                elif "nested" in aggslist[i][key0]:  # nested_   zi ding yi nested_name
                    path = aggslist[i][key0]["nested"]["path"]
                    key1 = list(aggslist[i][key0]["aggs"])[0]
                    temp = aggslist[i + 1]
                    tkey = list(temp)[0]
                    path_2 = temp[tkey].get("nested", {}).get("path", None)
                    if path_2 and (path_2 != path):  # 嵌套aggs，若外层field为nested，那么内层field和 ops field都需要为nested，且path相同
                        raise ValueError("path[{}] != path[{}]".format(path, path_2))
                    if path_2:
                        temp = temp["aggs"]  # 在外层已经标记进入nested，在内层和ops不需要再标记，只需在field前面加上path前缀
                    add_path(temp, path)  # 只需在field前面加上path前缀
                    aggslist[i][key0]["aggs"][key1].setdefault("aggs", {}).update(temp)
            return aggslist[0]

    def get_search_dsl(self, *args, **kwargs):
        pms = kwargs.get("pms", {})
        pms = self.params_mapping(pms=pms)
        filter = pms.get("filter", {})
        aggs = pms.get("aggs", {})
        aggs_params = pms.get("aggs_params", {})

        if aggs_params:
            aggs = self.produce_aggs(aggs_params)

        bool_must = self.get_bool_should(filter=filter)

        # 拼装区域范围
        if "distance" in filter:
            pos = str(pms.get("pos", {}).get("latitude", "")) + "," + str(
                pms.get("pos", {}).get("longitude", ""))
            if not pos.startswith(",") and not pos.endswith(","):
                bool_must += [
                    {"bool": {"filter": [{"geo_distance": {"distance": str(filter["distance"]) + "m", "pos": pos}}]}}]

        # ==============排序方式================
        sort = pms.get("sort", [])
        sorts = []
        for s in sort[:]:
            if s.get("field") in self.nested:
                path = self.nested[s.get("field")]
                sorts += [{path + '.' + s.get("field"): {"order": s.get("type"), "nested_path": path}}]
                sort.remove(s)
        sorts += [{s.get("field"): {"order": s.get("type")}} for s in sort]

        # ==============排序方式================

        # ===============限制分页=============
        if pms.get("from", 0) > 3000:
            pms["from"] = random.randint(0, 300)
        if pms.get("size", 30) > 30:
            pms["size"] = 30

        query = {"query": {"bool": {"must": bool_must}}, "from": pms.get("from", 0),
                 "size": pms.get("size", 30)}
        # 排序
        if sorts:
            query["sort"] = sorts
        if aggs:
            query["aggs"] = aggs
        # 控制返回字段，默认所有
        if pms.get("_source", []):
            query["_source"] = pms["_source"]
        return json.dumps(query)

    def gt_equal_dsl(self, key, value, bool):
        if len(value) == 1:
            # 单选等值查询
            condition = [{"bool": {bool: [{"term": {key: v}} for v in value]}}]
        else:
            # 多选等值查询
            condition = [{"bool": {bool: [{"terms": {key: [v for v in value]}}]}}]
        return condition

    def gt_checkbox_dsl(self, key, value, bool):
        # 多选等值查询
        condition = [{"bool": {bool: [{"term": {key: v}} for v in value]}}]
        return condition

    def gt_match_dsl(self, key, value, bool):
        condition = [{"bool": {bool: [{"match_phrase": {key: {"query": v, "slop": 10}}} for v in value]}}]
        return condition

    def gt_wildcard_dsl(self, key, value, bool):
        condition = [{"bool": {bool: [{"wildcard": {key: "*" + v + "*"}} for v in value]}}]
        return condition

    def gt_region_dsl(self, key, value, bool):
        def gt_condition(v):
            v = v.replace("+", "-")
            if "-" not in v:
                return {"term": {key: v}}
            if not v.split("-")[1]:
                c = {"range": {key: {"gte": v.split("-")[0]}}}
            elif not v.split("-")[0]:
                c = {"range": {key: {"lte": v.split("-")[1]}}}
            else:
                c = {"range": {key: {"gte": v.split("-")[0], "lte": v.split("-")[1]}}}
            return c

        if bool == "must":
            bool = "should"
        condition = [{"bool": {bool: [gt_condition(v) for v in value]}}]
        return condition

    def gt_point_dsl(self, key, value, bool):
        condition = [{"bool": {bool: [{"geo_bounding_box": {key: v}} for v in value]}}]
        return condition

    def get_bool_must(self, pms):
        filters = pms.get("filter", {})
        bool_must = []
        nesteds = []
        flag = False
        if "status" in filters:
            flag = True
        elif ("not_status" in filters) and filters["not_status"] == "0":
            flag = True
        change_price_flag = []
        change_price = [{"nested": {"path": "house_info", "query": {"bool": {"must": change_price_flag}}}}]
        for key, value in filters.items():
            key = key.strip()
            if not value:
                continue
            value = str(value).strip(" ").strip(",").split(",") if not isinstance(value, list) else value
            if key == "price_change":
                change_price_flag += self.gt_equal_dsl(key="house_info.price_change", value=value, bool="must")
                continue
            if key == "price_updated":
                change_price_flag += self.gt_region_dsl(key="house_info.price_updated", value=value, bool="must")
                continue

            if key == "tag" or key == "not_tag":
                tmp_bool = "must"
                if key == "not_tag":
                    tmp_bool = "must_not"
                if flag:
                    if key == "not_tag":
                        nesteds += [{"nested": {"path": "house_info", "query": {
                            "bool": {
                                "must_not": {"match_phrase": {"house_info.tag": v}},
                                "must": {"term": {"house_info.status": 1}}}}}}
                                    for v in value]
                    else:
                        nesteds += [{"nested": {"path": "house_info", "query": {
                            "bool": {
                                "must": [{"match_phrase": {"house_info.tag": v}},
                                         {"term": {"house_info.status": 1}}]}}}}
                                    for v in value]
                else:
                    nesteds += [{"nested": {"path": "house_info",
                                            "query": {"bool": {tmp_bool: {"match_phrase": {"house_info.tag": v}}}}}}
                                for v in value]
                continue
            # 嵌套
            if (key in self.nested) or ((key[4:] in self.nested) and key.startswith("not_")):
                condition = {}
                if not key.startswith("not_"):
                    nsk = self.nested[key]
                    new_key = nsk + '.' + key
                    bool = "must"
                else:
                    nsk = self.nested[key[4:]]
                    new_key = nsk + '.' + key[4:]
                    bool = "must_not"
                # 拼数等值查询
                if (key in self.equal) or (key[4:] in self.equal):
                    condition = self.gt_equal_dsl(key=new_key, value=value, bool=bool)

                # 拼数多值查询
                if (key in self.checkbox) or (key[4:] in self.checkbox):
                    condition = self.gt_checkbox_dsl(key=new_key, value=value, bool=bool)

                # 拼数模糊查询
                if (key in self.match) or (key[4:] in self.match):
                    condition = self.gt_match_dsl(key=new_key, value=value, bool=bool)

                # keyword不分词搜索
                if (key in self.wildcard) or (key[4:] in self.wildcard):
                    condition = self.gt_wildcard_dsl(key=new_key, value=value, bool=bool)

                # 拼数值范围
                if (key in self.region) or (key[4:] in self.region):
                    condition = self.gt_region_dsl(key=new_key, value=value, bool=bool)

                # 拼坐标点范围
                if (key in self.point) or (key[4:] in self.point):
                    condition = self.gt_point_dsl(key=new_key, value=value, bool=bool)

                if flag and nsk == "house_info":
                    condition += [{"term": {"house_info.status": 1}}]
                nesteds.append({"nested": {"path": nsk, "query": {"bool": {"must": condition}}}})
                # for mest in nesteds:
                #     if nsk == mest.get("nested").get("path"):
                #         if condition:
                #             mest["nested"]["query"]["bool"]["must"] += condition
                #         break
                # else:
                #     nesteds.append({"nested": {"path": nsk, "query": {"bool": {"must": condition}}}})
            else:
                if not key.startswith("not_"):
                    bool = "must"
                else:
                    key = key[4:]
                    bool = "must_not"
                # 拼数等值查询
                if (key in self.equal) or (key[4:] in self.equal):
                    bool_must += self.gt_equal_dsl(key=key, value=value, bool=bool)

                # 拼数多值查询
                if (key in self.checkbox) or (key[4:] in self.checkbox):
                    bool_must += self.gt_checkbox_dsl(key=key, value=value, bool=bool)

                if (key in self.match) or (key[4:] in self.match):
                    bool_must += self.gt_match_dsl(key=key, value=value, bool=bool)

                if (key in self.wildcard) or (key[4:] in self.wildcard):
                    bool_must += self.gt_wildcard_dsl(key=key, value=value, bool=bool)

                # 拼数值范围
                if (key in self.region) or (key[4:] in self.region):
                    bool_must += self.gt_region_dsl(key=key, value=value, bool=bool)

                # 拼坐标点范围
                if (key in self.point) or (key[4:] in self.point):
                    bool_must += self.gt_point_dsl(key=key, value=value, bool=bool)

        if change_price_flag:
            if flag:
                change_price_flag += [{"term": {"house_info.status": 1}}]
            bool_must += change_price
        bool_must += nesteds
        return bool_must

    def get_bool_should(self, filter):

        should_tmp = []
        # 非should dict
        notsdict = {}
        # 循环外层字典
        for key, value in filter.items():
            if key.startswith("should"):
                # 循环数组
                tmp = []
                for i in value:
                    tmp += self.get_bool_should(filter=i)
                should_tmp += [{'bool': {'should': tmp}}]
            else:
                notsdict.setdefault(key, value)
        if notsdict:
            tmp = self.get_bool_must(pms={"filter": notsdict})
            must_tmp = tmp
            if should_tmp:
                should_tmp = must_tmp + should_tmp
            else:
                should_tmp = must_tmp
        return should_tmp

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 上午11:28
# @Author  : jianguo@zhugefang.com
# @Desc    :

# import tornado.ioloop
import time
import tornado
from tornado.web import HTTPError
import json
from concurrent.futures import ThreadPoolExecutor
from zhuge.utils.BaseUtils import BaseUtils
from zhuge.apps.config.ConfigService import ConfigService


class Executor(ThreadPoolExecutor):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=ConfigService.get_thread_num())  # 设置线程数
        return cls._instance


def catch_exception(origin_func):

    def wrapper(*args, **kwargs):
        try:
            st = time.time()
            u = origin_func(*args, **kwargs)
            et = time.time() - st
            return u
        except Exception as e:
            print(e)
            raise e
    return wrapper


def catch(*dargs, **dkwargs):
    """
    # @Time    : 18-2-13 上午11:28
    # @Author  : jianguo@zhugefang.com
    # @Desc    : 异常处理装饰器
    """
    def wrapper(func):
        def _wrapper(*args, **kargs):
            request = args[0]
            try:
                st = time.time()
                result = {"message": "success", "code": 200}
                fun = func(*args, **kargs)
                et = time.time() - st
                result["time"] = et
                result["page"] = fun.get("page", {})
                result["data"] = fun.get("data", [])
                result["code"] = fun.get("code", 200)
                request.write(json.dumps(result))
            except Exception as e:
                print(e)
                result = {"message": "error", "code": 500}
                request.write(json.dumps(result))
        return _wrapper
    return wrapper


def catch_yield(*dargs, **dkwargs):
    def wrapper(func):
        @tornado.gen.coroutine
        def _wrapper(*args, **kargs):
            request = args[0]
            try:
                st = time.time()
                result = {"message": "success", "code": 200}
                fun = yield func(*args, **kargs)
                et = time.time() - st
                try:
                    if et>0.3:
                        print("超过0.3s的请求")
                        print("URI：",request.request.uri)
                        print("城市：",kargs.get('city'))
                        print("参数：",request.request.body)
                        print("时间：",et,"s")
                        print("超过0.3s的参数结束请求")
                except Exception as e:
                    print ("超时打印失败",e)
                result["time"] = et
                result["page"] = fun.get("page", {})
                result["data"] = fun.get("data", [])
                result["code"] = fun.get("code", 200)
                if fun.get("total") or 0:
                    result["total"] = fun.get("total", 0)
                if fun.get("message"):
                    result["message"] = fun.get("message")
                request.write(json.dumps(result))
            except Exception as e:
                result = {"message": str(e), "code": 500}
                request.write(json.dumps(result))
        return _wrapper
    return wrapper


class BaseController(tornado.web.RequestHandler):
    executor = Executor()

    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Content-Type,Authorization,X-Requested-With")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')

    @catch_yield()
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        data = yield self.gethandle(*args, **kwargs)
        return data

    @catch_yield()
    @tornado.gen.coroutine
    def post(self, *args, **kwargs):
        data = yield self.posthandle(*args, **kwargs)
        return data

    @catch_yield()
    @tornado.gen.coroutine
    def head(self, *args, **kwargs):
        data = yield self.headhandle(*args, **kwargs)
        return data

    @catch_yield()
    @tornado.gen.coroutine
    def options(self, *args, **kwargs):
        data = yield self.optionshandle(*args, **kwargs)
        return data

    @catch_yield()
    @tornado.gen.coroutine
    def delete(self, *args, **kwargs):
        data = yield self.deletehandle(*args, **kwargs)
        return data

    @catch_yield()
    @tornado.gen.coroutine
    def patch(self, *args, **kwargs):
        data = yield self.patchhandle(*args, **kwargs)
        return data

    @catch_yield()
    @tornado.gen.coroutine
    def put(self, *args, **kwargs):
        data = yield self.puthandle(*args, **kwargs)
        return data

    def headhandle(self, *args, **kwargs):
        raise HTTPError(405)

    def gethandle(self, *args, **kwargs):
        raise HTTPError(405)

    def posthandle(self, *args, **kwargs):
        raise HTTPError(405)

    def deletehandle(self, *args, **kwargs):
        raise HTTPError(405)

    def patchhandle(self, *args, **kwargs):
        raise HTTPError(405)

    def puthandle(self, *args, **kwargs):
        raise HTTPError(405)

    def optionshandle(self, *args, **kwargs):
        raise HTTPError(405)

# @route('/hello2')
# class hello2(BaseController):
#     executor = Executor()
#     # @Time    : 18-4-14 下午2:30
#     # @Author  : jianguo@zhugefang.com
#     # @Desc    : 查询经纪公司列表
#     @catch1()  # 异常装饰器
#     @tornado.gen.coroutine
#     def get(self, *args, **kwargs):
#         try:
#             result =  yield self.getData()
#         except Exception as e:
#             print (e)
#         if result:
#             return {"data": result.decode()}
#
#     @tornado.concurrent.run_on_executor
#     def getData(self):
#         dbfactory.db_pika(conf_name="borough_api").hset("apitest", "hello1", "欢迎使用诸葛找房数据分析api服务!!!")
#         result = dbfactory.db_pika(conf_name="borough_api").hget("apitest", "hello1")
#         return result

def encrypt(*dargs, **dkwargs):
    """
    加密装饰器
    :param dargs:
    :param dkwargs:
    :return:
    """
    def wrapper(func):
        def _wrapper(*args, **kargs):
            signatures = {"JD": 'acb34c2b9da033dd38e946d313449068'}
            request = args[0]
            user = request.get_argument("user")
            signature = request.get_argument("signature")
            key = signatures.get(user)
            pms = dkwargs.get('pms', [])
            pm = [f"{key}={request.get_argument(key)}" for key in pms]
            pm = "&".join(pm) + key
            my_signature = BaseUtils.getMd5(pm)
            print(my_signature)
            if my_signature == signature:
                fun = func(*args, **kargs)
                return fun
            else:
                result = {
                    "message": "您的Token无效,请联系诸葛找房,多次尝试会被记录黑名单,谢谢配合！！！",
                    "code": 200,
                    "data": []}
                request.write(json.dumps(result))
        return _wrapper
    return wrapper

# def login_permit(f):
#     """
#     # @Time    : 18-4-16 上午17:00
#     # @Author  : zhuyikun@zhugefang.com
#     # @Desc    : 获取权限装饰器
#
#     """
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         try:
#             request = args[0]
#             token = request.get_argument('token')
#             print(token)
#             result = user_service.get_one(filter={'user_id': int(user_id)})
#             print('permit...', result)
#             del result[0]['_id']
#             del result[0]['password']
#             kwargs['user_info'] = result[0]
#             return f(*args, **kwargs)
#         except Exception as e:
#             print(e)
#             return {'data': {"message": "Not Login", "code": 401}}
#     return decorated_function

class Route(object):
    """ 把每个URL与Handler的关系保存到一个元组中，然后追加到列表内，列表内包含了所有的Handler """

    def __init__(self):
        self.urls = list()  # 路由列表

    def __call__(self, url, *args, **kwargs):
        def register(cls):
            self.urls.append((url, cls))  # 把路由的对应关系表添加到路由列表中
            return cls

        return register

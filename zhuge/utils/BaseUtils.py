#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import time
import json
import requests
import pinyin
import re
import datetime


class BaseUtils(object):
    @staticmethod
    def getMd5(value):
        m = hashlib.md5()
        m.update(value.encode("utf8"))
        return m.hexdigest()

    @staticmethod
    def getIntTime():
        return int(time.time())

    @staticmethod
    def getPiyin(value):
        py = pinyin.get(value, format="strip")
        return BaseUtils.extract_str(py)

    @staticmethod
    def extract_str(string):
        string = string.lower()
        regEx = "\W+"
        pattern = re.compile(regEx)
        mt = re.sub(pattern, '', string=string)
        return mt

    @staticmethod
    def extract(*args, **kwargs):
        data_list = re.findall(kwargs.get("regex"), str(kwargs.get("data")))
        return len(data_list) > 0 and data_list.pop()

    @staticmethod
    def replace(*args, **kwargs):
        return re.sub(kwargs.get("regex"), kwargs.get("value"), kwargs.get("data"))

    @staticmethod
    def getFpy(value, delimiter=""):
        py = pinyin.get(value, format="strip", delimiter=delimiter)
        return py

    @staticmethod
    def getSpy(value, delimiter=""):
        py = pinyin.get_initial(value, delimiter=delimiter)
        return py

    @staticmethod
    def getSignature(data):
        key = ''

        return key

    @staticmethod
    def list_to_dict(data, key, value):
        result = dict()
        for i in data:
            result.setdefault(i[key], i[value])
        return result

    @staticmethod
    def get_city():
        pms = {"city": "jiamusi", "city_last": "tl"}
        result = requests.post(url="http://config.dapi.zhugefang.com/config/getCityConfig", json=pms)
        result = json.loads(result.content)['data']
        # result = BaseUtils.list_to_dict(result, key, value)
        return result

    @staticmethod
    def get_city_s(city, city_last):
        pms = {"city": "%s" % city, "city_last": "%s" % city_last}
        result = requests.post(url="http://config.dapi.zhugefang.com/config/getCityConfig", json=pms)
        result = json.loads(result.content)['data']
        # result = BaseUtils.list_to_dict(result, key, value)
        return result

    @staticmethod
    def get_new_channel(key='channel_name', value='source_id'):
        result = requests.get("http://newhouse.dapi.zhugefang.test/config/getNewHouseChannel")
        result = json.loads(result.content)['data']
        result = BaseUtils.list_to_dict(result, key, value)
        return result

    @staticmethod
    def get_pre_month(num=6):
        today = datetime.date.today()
        result = []
        for i in range(num):
            first_day = today.replace(day=1)
            pre_date = first_day - datetime.timedelta(days=1)
            pre_month = datetime.datetime.strftime(pre_date, '%Y%m')
            result.append(int(pre_month))
            today = pre_date
        result.sort()
        return result

    @staticmethod
    def get_pre_week(num=52, today=""):
        now = datetime.datetime.now()
        if today:
            now = datetime.datetime.strptime(today, '%Y%m%d')
        pre_week_start = now - datetime.timedelta(days=now.weekday())
        result = []
        for i in range(num):
            pre_week = pre_week_start.strftime('%Y%m%d')
            result.append(int(pre_week))
            pre_week_start = pre_week_start - datetime.timedelta(weeks=1)
        result.sort()
        return result

    @staticmethod
    def get_pre_day(num=14, today=""):
        pre_day_start = datetime.datetime.now()
        if today:
            pre_day_start = datetime.datetime.strptime(today, '%Y%m%d')

        result = []
        for i in range(num):
            pre_day = pre_day_start.strftime('%Y%m%d')
            result.append(int(pre_day))
            pre_day_start = pre_day_start - datetime.timedelta(days=1)
        result.sort()
        return result

    @staticmethod
    def stamp_to_time(timestamp, fromdata="%Y-%m-%d %H:%M:%S"):
        if timestamp and re.search('^\d{9,}$', str(timestamp)):
            time_local = time.localtime(int(timestamp))
            dt = time.strftime(fromdata, time_local)
            return dt
        else:
            return timestamp

    @staticmethod
    def mkdir(path):
        # 引入模块
        import os

        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)

            print(path + ' 创建成功')
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            print(path + ' 目录已存在')
            return False


class Prpcrypt():

    def __init__(self, key, texts):
        self.AES = None
        if not self.AES:
            from zhuge.Crypto.Cipher import AES
            from zhuge.binascii import b2a_hex, a2b_hex
            self.AES = AES
            self.b2a_hex = b2a_hex
            self.a2b_hex = a2b_hex
        self.key = key
        self.mode = self.AES.MODE_CBC
        self.texts = texts

        # 加密函数，如果text不是16的倍数【加密文本text必须为16的倍数！】，那就补足为16的倍数

    def encrypt(self, text):
        cryptor = self.AES.new(self.key, self.mode, self.key)
        # 这里密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.目前AES-128足够用
        length = 32
        count = len(text)
        if (count % length != 0):
            add = length - (count % length)
        else:
            add = 0
        text = text + ('\0' * add)
        self.ciphertext = cryptor.encrypt(text)
        # 因为AES加密时候得到的字符串不一定是ascii字符集的，输出到终端或者保存时候可能存在问题
        # 所以这里统一把加密后的字符串转化为16进制字符串
        print('encrypt', self.ciphertext)
        return self.b2a_hex(self.ciphertext)

        # 解密后，去掉补足的空格用strip() 去掉

    def decrypt(self, text):
        cryptor = self.AES.new(self.key, self.mode, self.key)
        plain_text = cryptor.decrypt(self.a2b_hex(text)).decode()
        return plain_text.rstrip('\0')

    def get_encrypt(self):
        aes_text = self.encrypt(self.texts)
        return str(aes_text).replace("b'", '').replace("'", '')

    def get_decrypt(self):
        return self.decrypt(self.texts)


if __name__ == '__main__':
    BaseUtils.get_pre_week(today="20180701")

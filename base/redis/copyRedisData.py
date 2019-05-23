"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/2/26
@Desc    :

"""
from databases.dbfactory.dbfactory import dbfactory
import json, time


class RedisHandle(object):
    def __init__(self):
        self.redis_conn = dbfactory.db_redis(conf_name="complex_test")
        self.complex = dbfactory.db_redis(conf_name="complex")

    def copyData(self, old_key, new_key, size=10):
        start = 0
        end = size - 1
        while True:
            result = self.redis_conn.lrange(old_key, start, end)
            if not result:
                break
            print(len(result))
            self.redis_conn.lpush(new_key, *result)
            start += size
            end += size
            # result = json.loads(str(result[0], encoding="utf-8")) # 查看数据格式


if __name__ == '__main__':
    a = RedisHandle()
    old_key = "aba-anjuke-complex_details_bak"
    new_key = "aba-anjuke-complex_details"
    a.copyData(old_key, new_key)

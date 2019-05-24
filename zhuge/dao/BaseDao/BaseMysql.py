
# @Time    : 18-1-13 上午10:49
# @Author  : jianguo@zhugefang.com
# @Desc    :
from zhuge.dao.Base import Base
from zhuge.databases.dbfactory.dbfactory import dbfactory
import logging


class BaseMysql(Base):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.get("model")
        self.conn = dbfactory.create_db(conf_name=kwargs.get("conf_name"), db_type=kwargs.get("db_type") or "db_mysql")
        super().__init__(model=self.model)

    def exe_s_sql(self, *args, **kwargs):
        """
            @Author  : jianguo@zhugefang.com
            @Time    : 18-3-14 上午10:49
            @Desc    : 执行原生语句SELECT语句 返回单条数据
            :param  city: 城市缩写
            :param  sql:  语句
            :param  link_type: 指定连接实例（默认default配置）
            :return: 字典类型

        """
        city = kwargs.get("city")
        link_type = kwargs.get('link_type', 'default')
        sql = kwargs.get("sql").get("sql")
        pms = kwargs.get("sql").get("pms")
        with self.conn.get_conn(link_type=link_type, city=city) as cursor:
            cursor.execute(sql, pms)
            res = cursor.fetchone() or {}
            return res

    def exe_s_sqls(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行原生语句SELECT语句 返回多条数据
           :param  city: 城市缩写
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型

        """
        city = kwargs.get("city")
        link_type = kwargs.get('link_type', 'default')
        sql = kwargs.get("sql").get("sql")
        pms = kwargs.get("sql").get("pms", ())
        with self.conn.get_conn(city=city, link_type=link_type) as cursor:
            cursor.execute(sql, pms)
            res = cursor.fetchall()
            return res

    def exe_i_sql(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行原生语句INSERT语句 返回单条数据ID
           :param  city: 城市缩写
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型

        """
        city = kwargs.get("city")
        sql = kwargs.get("sql").get("sql")
        link_type = kwargs.get("link_type", "default")
        pms = kwargs.get("sql").get("pms", ())
        with self.conn.get_conn(city=city, link_type=link_type) as cursor:
            cursor.execute(sql, pms)
            res = cursor.lastrowid
            return res

    def exe_i_sqls(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行原生语句SELECT语句 返回单条数据
           :param  city: 城市缩写
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型

        """
        city = kwargs.get("city")
        sql = kwargs.get("sql").get("sql")
        link_type = kwargs.get("link_type", "default")
        pms = kwargs.get("sql").get("pms", ())
        with self.conn.get_conn(city=city, link_type=link_type) as cursor:
            res = cursor.executemany(sql, pms)
            return res

    def exe_t_i_sqls(self, *args, **kwargs):
        """
        执行事务语句
        :param args:   [{'sql':sql,'pms':pms}，{'sql':sql,'pms':pms}]
        :param kwargs:
        :return:
        """
        city = kwargs.get("city")
        datas = kwargs.get("datas")
        with self.conn.get_conn(city=city) as cursor:
            for data in datas:
                sql = data.get("sql")
                pms = data.get("pms", ())
                res = cursor.execute(sql, pms)
            return True

    def exe_u_sql(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行原生语句SELECT语句 返回单条数据
           :param  city: 城市缩写
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型

        """
        city = kwargs.get("city")
        sql = kwargs.get("sql").get("sql")
        pms = kwargs.get("sql").get("pms", ())
        with self.conn.get_conn(city=city) as cursor:
            res = cursor.execute(sql, pms)
            return res

    def exe_d_sql(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行原生语句SELECT语句 返回单条数据
           :param  city: 城市缩写
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型

        """
        city = kwargs.get("city")
        link_type = kwargs.get('link_type', 'default')
        filter = kwargs.get('filter')
        if not filter:
            logging.error('delete is not filter')
            return False
        sql = f"DELETE from {self.table} WHERE {filter}"
        try:
            with self.conn.get_conn(city=city, link_type=link_type) as cursor:
                cursor.execute(sql)
                return True
        except Exception as e:
            logging.error(e)
            return False

    def count_model(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行查询总数语句
           :param  city: 城市缩写
           :param  filter: where条件 ‘1=1’
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型
        """
        city = kwargs.get("city")
        link_type = kwargs.get('link_type', 'default')
        filter = kwargs.get('filter')
        field = kwargs.get('field', 'COUNT(1) AS total')
        sql_count = f"SELECT {field} from {self.table}"
        sql = f"{sql_count} WHERE {filter}" if filter else f"{sql_count}"
        return self.exe_s_sql(link_type=link_type, city=city, sql={'sql': sql})

    def count_models(self, *args, **kwargs):
        """
           @Author  : jianguo@zhugefang.com
           @Time    : 18-3-14 上午10:49
           @Desc    : 执行查询总数语句
           :param  city: 城市缩写
           :param  filter: where条件 ‘1=1’
           :param  link_type: 指定连接实例（默认default配置）
           :return: 字典类型
        """
        city = kwargs.get("city")
        link_type = kwargs.get('link_type', 'default')
        filter = kwargs.get('filter')
        field = kwargs.get('field', 'COUNT(1) AS total')
        sql_count = f"SELECT {field} from {self.table}"
        sql = f"{sql_count} WHERE {filter}" if filter else f"{sql_count}"
        return self.exe_s_sqls(link_type=link_type, city=city, sql={'sql': sql})

    def select_model(self, *args, **kwargs):
        link_type = kwargs.get('link_type', 'default')
        city = kwargs.get("city")
        filter = kwargs.get('filter')
        field = kwargs.get('field')
        index = kwargs.get('index')
        size = kwargs.get('size')
        sql = self.model.get_select_sql(field=field, index=index, size=size, filter=filter)
        data = self.exe_s_sqls(link_type=link_type, sql=sql, city=city)
        return data

    def select_one(self, *args, **kwargs):
        link_type = kwargs.get('link_type', 'default')
        city = kwargs.get("city")
        filter = kwargs.get('filter')
        field = kwargs.get('field')
        index = kwargs.get('index')
        size = kwargs.get('size')
        sql = self.model.get_select_sql(field=field, index=index, size=size, filter=filter)
        data = self.exe_s_sql(link_type=link_type, sql=sql, city=city)
        return data

    def update_model(self, *args, **kwargs):
        link_type = kwargs.get('link_type', "default")
        city = kwargs.get("city")
        filter = kwargs.get('filter')
        data = kwargs.get("data")
        sql = self.model.get_update_sql(city=city, filter=filter, data=data)
        result = self.exe_u_sql(link_type=link_type, city=city, sql=sql)
        return result

    def insert_model(self, *args, **kwargs):
        link_type = kwargs.get('link_type', "default")
        city = kwargs.get("city")
        data = kwargs.get("data")
        sql = self.model.get_insert_sql(city=city, data=data)
        result = self.exe_i_sql(link_type=link_type, city=city, sql=sql)
        return result

    def inserts_model(self, *args, **kwargs):
        link_type = kwargs.get('link_type', "default")
        city = kwargs.get("city")
        data = kwargs.get("data")
        sql = self.model.get_insert_sqls(city=city, data=data)
        result = self.exe_i_sqls(city=city, sql=sql)
        return result

    def insert_update_model(self, *args, **kwargs):
        link_type = kwargs.get('link_type', "default")
        city = kwargs.get("city")
        data = kwargs.get("data")
        yes_up = kwargs.get("yes_up", [])
        adjust = kwargs.get("adjust", {})
        sql = self.model.get_insert_update_sqls(data=[data], yes_up=yes_up, adjust=adjust)
        result = self.exe_i_sqls(link_type=link_type, city=city, sql=sql)
        return result

    def delete_model(self, *args, **kwargs):
        link_type = kwargs.get('link_type')
        city = kwargs.get("city")
        filter = kwargs.get("filter")
        sql = self.model.get_delete_sql(city=city, filter=filter)
        result = self.exe_d_sql(link_type=link_type, city=city, sql=sql)
        return result

    def get_ids(self, *args, **kwargs):
        complex_id = kwargs.get('complex_id')
        sql = f"SELECT id from {self.table} WHERE complex_id='{complex_id}'"
        result = self.exe_s_sql(city=kwargs.get("city"), sql={'sql': sql})
        if result and len(result) > 0:
            return result.get("id")
        else:
            i_sql = f"INSERT INTO {self.table} (`complex_id`) VALUES ('{complex_id}')"
            i_data = self.exe_i_sql(
                city=kwargs.get("city"), sql={
                    'sql': i_sql})
            if i_data:
                return i_data

    def select_newmodel(self, *args, **kwargs):
        link_type = kwargs.get('link_type', 'default')
        city = kwargs.get("city")
        sql = self.model.get_newselect_sql(*args, **kwargs)
        data = self.exe_s_sqls(link_type=link_type, sql=sql, city=city)
        data = self.tf_decimal(datas=data)
        return data

    def tf_decimal(self, datas):
        decimal = ['created_time', 'updated', 'sort_weight']
        if isinstance(datas, list):
            for data in datas:
                for k, v in data.items():
                    if k in decimal:
                        data[k] = int(data[k])
            return datas
        elif isinstance(datas, dict):
            for k, v in datas.items():
                if k in decimal:
                    datas[k] = int(datas[k])
            return datas

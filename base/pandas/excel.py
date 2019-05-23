"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/4/22
@Desc    :

"""
import time
import xlrd
import pandas as pd
from multiprocessing import Pool
from apps.zhuge_newhouse.dao.ComplexInformationDao import ComplexInformationDao


class Excel(object):
    def __init__(self):
        self.information = ComplexInformationDao()

    def run(self):
        try:
            df = pd.read_excel("删除的点评.xlsx", usecols="C:D")
            # sql = """DELETE FROM complex_icons WHERE developer_price = 0 AND developer_price_unit = '' AND
            # ( sale_status IS NULL OR sale_status = '' OR sale_status = 0 )
            # AND first_delivertime = '' AND first_saletime = 0"""
            # info = self.complex.exe_s_sqls(city=city, sql={'sql': sql})
            data = df.values
            head = df.head()
            for i in head:
                print(i)
            print(1)
        except Exception as e:
            print(e)

    def xlrd(self):
        workbook = xlrd.open_workbook(r'删除的点评.xlsx')
        table = workbook.sheets()[0]
        citys = table.col_values(2, start_rowx=0, end_rowx=None)
        ids = table.col_values(3, start_rowx=0, end_rowx=None)
        result = {}
        for i in range(1, len(ids)):
            result.setdefault(citys[i], [])
            result[citys[i]].append(int(ids[i]))

        for city, v in result.items():
            where = [str(id) for id in v]
            where = ",".join(where)
            sql = f"""delete from complex_comment where source_id=81 and id in ({where})"""
            info = self.information.exe_s_sqls(city=city, sql={"sql": sql})
            print(city, info)

    def all_city(self):
        sql = f"""show databases"""
        info = self.information.exe_s_sqls(city="sh", sql={'sql': sql})
        result = []
        for i in info:
            if "newhouse_" in i['Database']:
                result.append(i['Database'].split("_")[1])
        return result


if __name__ == '__main__':
    t = time.time()
    a = Excel()
    a.xlrd()
    # p = Pool(10)
    # citys = [
    #     "aba",
    #     "bj"
    #     # "baoshan",
    #     # "dali",
    #     # "fz",
    #     # "jh",
    #     # "nanchong",
    #     # "mas",
    #     # "wlmq",
    #     # "wuhu",
    #     # "xiangyang",
    #     # "yinchuan",
    #     # "yz",
    # ]
    # for i in a.all_city():
        # for i in citys:
    #     p.apply_async(a.run, args=(i,))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')
    # print(f"耗时:{time.time() - t}s")

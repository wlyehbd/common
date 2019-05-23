"""
@Author  : hanbingde@zhugefang.com
@Time    : 2019/3/1
@Desc    :  未审核楼盘新房gov表楼盘名称md5值不对应数据监控
"""
import sys
import time

sys.path.append("../../../")
sys.path.append("../../")
from zhuge.service.BaseService.BaseMysqlService import BaseMysqlService
from zhuge.apps.zhuge_newhouse.dao.ComplexDao import ComplexDao
from apps.zhuge_newhouse.dao.ComplexInformationDao import ComplexInformationDao
from multiprocessing import Pool
from zhuge.utils.BaseUtils import BaseUtils


class MysqlMultiProcess(BaseMysqlService):
    def __init__(self):
        self.complex = ComplexDao()
        self.information = ComplexInformationDao()

    def run(self, city):
        try:
            # sql = """update complex_information set building_content=REPLACE(building_content, SUBSTR(building_content,locate("我已阅读并同意", building_content), 999),"")  where building_content REGEXP ".*我已阅读并同意.*" """
            # sql = """update complex_information set building_content=REPLACE(building_content, "请咨询售楼处","")  where building_content REGEXP "请咨询售楼处" """
            # sql = """select count(1) from  complex_information where building_content REGEXP "400.{6,20}转[0-9]{3,}" """
            sql = """ALTER TABLE `complex_information` 
ADD COLUMN `content_md5` varchar(255) NULL DEFAULT NULL AFTER `is_delete`;"""
            info = self.complex.exe_s_sqls(city=city, sql={'sql': sql})
            # if not info:
            print(city, info)
        except Exception as e:
            print(city, e)

    def special_handle(self, city):
        try:
            total = self.information.count_model(city=city, filter="building_content REGEXP '400.{6,20}转[0-9]{3,}' ")
            num = 0
            while total and total.get("total") != 0 and num <= 13:
                num += 1
                sql = """select * from  complex_information where building_content REGEXP "400.{6,20}转[0-9]{3,}" limit 1000 """
                infos = self.information.exe_s_sqls(city=city, sql={'sql': sql})
                for i in infos:
                    i["building_content"] = BaseUtils.replace(data=i["building_content"],
                                                              regex="[^,.，。]*400[\d\-—,\s]{6,}转\d{3,}。?",
                                                              value="")
                    # print(BaseUtils.extract(data=i["building_content"],
                    #                         regex="[^,.，。]*400[\d\-—,\s]{7,}转\d{3,}。?")
                    #       )
                success = self.information.insert_update_models(city=city, data=infos, yes_up=["building_content"])
                print(f"{city}一共{total}条, 成功处理{success / 2}条", )
                total = self.information.count_model(city=city, filter="building_content REGEXP '转[0-9]{3,}' ")

            # if info:
            # print(city, infos)
        except Exception as e:
            print(city, e)

    def all_city(self):
        sql = f"""show databases"""
        info = self.complex.exe_s_sqls(city="sh", sql={'sql': sql})
        result = []
        for i in info:
            if "newhouse_" in i['Database']:
                result.append(i['Database'].split("_")[1])
        return result


if __name__ == '__main__':
    t = time.time()
    a = MysqlMultiProcess()
    p = Pool(10)
    citys = [
        "aba",
        "bj"
        # "baoshan",
        # "dali",
        # "fz",
        # "jh",
        # "nanchong",
        # "mas",
        # "wlmq",
        # "wuhu",
        # "xiangyang",
        # "yinchuan",
        # "yz",
    ]
    for i in a.all_city():
        # for i in citys:
        p.apply_async(a.run, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    print(f"耗时:{time.time() - t}s")

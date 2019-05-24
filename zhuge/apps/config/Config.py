#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-1-13 下午2:40
# @Author  : jianguo@zhugefang.com
# @Desc    :

log_config = {
    "path": "/home/zhuge/project/zhuge-etl2/logs/",
    "level": "DEBUG"  # INFO ERROR DEBUG
}
mongo_conf = {
    "borough": {
        "default": {
            # 主库
            'host': 'dds-2ze2f6d07e237dd41500-pub.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'zhuge',
            'password': '7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck',
        },
        "slave_1": {
            'host': 'dds-2ze2f6d07e237dd42.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'zhuge',
            'password': '7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck',
        },
    },
    "hidden_etl": {
        "default": {
            # 主库/
            'host': 'dds-2ze2b1d1c958b0f41.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'root',
            'password': 'HDP4xQvlUPDprhMjkw6SWErgkWCAZCDb',
        },
        "slave_1": {
            'host': 'mongo.zhugefang.com',
            'port': 9603,
            'username': 'zhuge',
            'password': '7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck',
        },
    },
    "hidden_off": {
        "default": {
            # 主库
            'host': 'dds-2ze2b1d1c958b0f41.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'root',
            'password': 'HDP4xQvlUPDprhMjkw6SWErgkWCAZCDb',
        },
        "slave_1": {
            'host': 'mongo.zhugefang.com',
            'port': 9603,
            'username': 'zhuge',
            'password': '7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck',
        },
    },
    "brokerbd": {
        "default": {
            'host': 'dds-2ze2b1d1c958b0f41.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'root',
            'password': 'HDP4xQvlUPDprhMjkw6SWErgkWCAZCDb',
        },
    },
    "ccmag": {
        "default": {
            'host': 'dds-2ze2b1d1c958b0f41.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'root',
            'password': 'HDP4xQvlUPDprhMjkw6SWErgkWCAZCDb',
        },
    },
    "building": {
        "default": {
            # 主库
            'host': 'mongo.zhugefang.com',
            'port': 9601,
            'username': 'zhuge',
            'password': '7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck',
        },
    },
    "newhouse_dock": {
        "default": {
            'host': 'dds-2ze2b1d1c958b0f41.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'root',
            'password': 'HDP4xQvlUPDprhMjkw6SWErgkWCAZCDb',
        },
    },
    "avgprice": {
        "default": {
            # 主库
            'host': 'dds-2ze2f6d07e237dd41500-pub.mongodb.rds.aliyuncs.com',
            'port': 3717,
            'username': 'zhuge',
            'password': '7UgfAWbUtTKeMVGrSLwsHjB9xGjumnck',
        },
    },

}

redis_conf = {
    "brokers_api": {
        # "db_url": "redis://root:p3dBUsVi4Fw4Vw4YMEDUomPbWM1hjd@r-2ze7af23552a3164.redis.rds.aliyuncs.com:6379/5"
        "db_url": "redis://127.0.0.1:6379/5"
    },
    "dm_api": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/0",
    },
    "borough_api": {
        "db_url": "redis://127.0.0.1:6379/1"
    },
    "complex_api": {
        "db_url": "redis://127.0.0.1:6379/3",
    },
    "sell": {
        "db_url": "redis://root:zhugeZHAOFANG1116@redis.zhugefang.com:9431",
    },
    "sell_api": {
        "db_url": "redis://127.0.0.1:6379/1"
    },
    "sell_personal": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379",
    },
    "complex": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/2",
    },
    "complex_cityarea": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/4",
    },
    "hidden": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/1"
    },
    "complex_cache": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/7",
    },
    "ccmag_api": {
        "db_url": "redis://127.0.0.1:6379/7",
    },
    "plathouse": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/7",
    },
    "consultation": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379",
    },
    "sell_monitor": {
        "db_url": "redis://root:zhugeZHAOFANG1116@r-2zefc71473d249c4.redis.rds.aliyuncs.com:6379/14",
    },
}

kafka_conf = {
    "thor": "10.45.142.19:9092,10.25.114.207:9092,10.25.115.91:9092"
}


tidb_conf = {
    "sell_api": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_rw",
            "passwd": "BXckJSdboJXYzjiC6c2jOH7hRPYL2H",
            "port": 4000,
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_rw",
            "passwd": "BXckJSdboJXYzjiC6c2jOH7hRPYL2H",
            "port": 4000,
            "charset": "utf8"
        },
    },

}

rabbitmq_conf = {
    "sell": {
        "default": {
            #          "host": "101.201.119.110",
            "host": "10.45.146.41",
            "user": "zhuge",
            "passwd": "data",
            "port": "5672"
        },
        "slave_1": {
            "host": "101.201.103.13",
            "user": "admin",
            "passwd": "admin",
            "port": "5672"
        }
    },
    "rent": {
        "default": {
            #          "host": "101.201.119.110",
            "host": "10.45.146.41",
            "user": "zhuge",
            "passwd": "data",
            "port": "5672"
        },
        "slave_1": {
            "host": "101.201.103.13",
            "user": "admin",
            "passwd": "admin",
            "port": "5672"
        }
    }
}

sell_db_name = {
    "bj": "spider"
}
mysql_conf = {
    "sell": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "mysql.zhugefang.com",
            "user": "data_r",
            "port": 9524,
            "passwd": "BQ6Qr1*dIh%##bK3zg5p0M6x@Mkqs&hg",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },
    "plathouse": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },
    "rent": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },
    "rent_t": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            'host': 'tidb.zhuge.com',
            'port': 4000,
            'user': 'data_rw',
            'passwd': 'BXckJSdboJXYzjiC6c2jOH7hRPYL2H',
        },
    },
    "hidden": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },

    "new_sell": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "mysql.zhugefang.com",
            "user": "data_r",
            "port": 9512,
            "passwd": "BQ6Qr1*dIh%##bK3zg5p0M6x@Mkqs&hg",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },
    "new_plathouse": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },

    "zhuge_dm": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "rm-2zed5a6vhd5qk06z5.mysql.rds.aliyuncs.com",
            "user": "dm_rw",
            "passwd": "CszwRk3breCsM5BCH0yDfHLorJM5QB5T",
            "port": 3306,
            "charset": "utf8"
        },
        "dev": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "rm-2zed5a6vhd5qk06z5.mysql.rds.aliyuncs.com",
            "user": "dm_rw",
            "passwd": "CszwRk3breCsM5BCH0yDfHLorJM5QB5T",
            "port": 3306,
            "charset": "utf8"
        }
    },

    "brokerhouse": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        }
    },
    "brokers": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        }
    },
    "complex": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "mysql.zhugefang.com",
            "user": "data_r",
            "port": 9543,
            "passwd": "ugtQiLyMAgBUf81tyOoMcRgzIzYOszjL",
            "charset": "utf8",
        },
        "slave_1": {

        }
    },
    "plathouse": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8",
        },
        "slave_1": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "10.25.156.118",
            "user": "afe-rw",
            "port": 3306,
            "passwd": "HMugq0Fjz3bK67tHdSFottW2ORwSKpcJ",
            "charset": "utf8"
        }
    },
    "analysis": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_r",
            "port": 9902,
            "passwd": "BQ6Qr1*dIh%##bK3zg5p0M6x@Mkqs&hg",
            "charset": "utf8",
        },
    },
    "sell_analysis": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_r",
            "port": 9902,
            "passwd": "BQ6Qr1*dIh%##bK3zg5p0M6x@Mkqs&hg",
            "charset": "utf8",
        },
        "write": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_rw",
            "passwd": "BXckJSdboJXYzjiC6c2jOH7hRPYL2H",
            "port": 9902,
            "charset": "utf8",
        },
    },
    "appraisal": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_r",
            "port": 9902,
            "passwd": "BQ6Qr1*dIh%##bK3zg5p0M6x@Mkqs&hg",
            "charset": "utf8",
        },
        "write": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "tidb.zhuge.com",
            "user": "data_rw",
            "passwd": "BXckJSdboJXYzjiC6c2jOH7hRPYL2H",
            "port": 9902,
            "charset": "utf8",
        },
    },
    "localhost": {
        "default": {
            "max_connections": 20,
            "wait_connection_timeout": 3,
            "host": "localhost",
            "user": "root",
            "port": 3306,
            "passwd": "admin123",
            "charset": "utf8",
        },
    },
}
pika_conf = {
    "sell_api": {
        "default": {
            # "host": "10.80.83.119",
            "host": "127.0.0.1",
            "port": 6379,
        },
        "slave1": {
            # "host": "10.80.83.119",
            "host": "127.0.0.1",
            "port": 6379,
        },
        "pre": "D-sell-",
    },
    "plat_api": {
        "host": "10.80.83.119",
        # "host": "127.0.0.1",
        "port": 9221,
        "pre": "D-plat-",
    },
    "borough_api": {
        "default": {
            # "host": "10.80.83.119",
            "host": "127.0.0.1",
            "port": 6379,
        },
        "slave1": {
            # "host": "10.80.83.119",
            "host": "127.0.0.1",
            "port": 6379,
        },
        "pre": "D-borough-",
    }
}
es_config = {
    "index_name_pre": "offline_",
    "sell": {
        "host": [
            # "101.201.119.240:9200"
            "101.201.119.240:9200"
        ],
        "maxsize": 25
    },

    "brokerhouse": {
        "host": [
            "10.25.156.118:9200"
        ],
        "maxsize": 25
    },

    "plathouse": {
        "host": [
            "10.25.156.118:9200"
        ],
        "maxsize": 25
    },
    "house_new_online": {
        "host": [
            '10.26.121.90:8800',
            '10.26.121.93:8800',
            '10.25.131.143:8800'
        ],
        "maxsize": 25
    },
    "index_name_rent": "offline_",
    "rent": {
        "host": [
            "10.25.156.118:9200"
        ],
        "maxsize": 25
    }
}
token_maping = {
    'user': 'jd',
    'passwd': 'jd-1234566'

}

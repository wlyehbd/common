import logging
from zhuge.apps.config.ConfigService import ConfigService


def logger(**kwargs):
    log_config = ConfigService.get_log_config()
    log_path = kwargs.get("log_path") or log_config.get("log_path")
    level_type = kwargs.get("level_type") or log_config.get("level_type")
    date_format = kwargs.get("date_format") or log_config.get("date_format")
    log_format = kwargs.get("log_format") or log_config.get("log_format")
    suffix = kwargs.get("suffix") or log_config.get("suffix")
    when = kwargs.get("when") or 'MIDNIGHT'
    interval = kwargs.get("interval") or 1
    backupCount = kwargs.get("backupCount") or 30

    # 缓存命中情况 入etl
    hdlr = logging.handlers.TimedRotatingFileHandler(filename=log_path, when=when, interval=interval, backupCount=backupCount)
    hdlr.suffix = suffix
    hdlr.setLevel(level_type)
    formater = logging.Formatter(fmt=log_format,datefmt=date_format)
    hdlr.setFormatter(fmt = formater)
    ch = logging.StreamHandler()
    ch.setLevel(level_type)
    ch.setFormatter(fmt = formater)
    logging.getLogger("lowercache").addHandler(hdlr)
    logging.getLogger("lowercache").addHandler(ch)
    logging.getLogger("lowercache").setLevel(level_type)

    # 打印降级缓存的参数和返回值 输出到控制台
    ch1 = logging.StreamHandler()
    ch1.setLevel(level_type)
    logger_content = logging.getLogger("cache_content")
    logger_content.setLevel(level_type)
    logger_content.addHandler(ch1)


import datetime
import json
import logging
import os

# 使用logging模块记录日志
logger = logging.getLogger("my_logger")
# 获取json配置文件
with open(os.path.join(os.getcwd(), "conf", "init.json"), "r", encoding="utf-8") as f:
    conf = f.read()
conf = json.loads(conf)


def reandom():
    date = datetime.datetime.now()
    hour = f"0{date.hour}" if date.hour < 10 else str(date.hour)
    minute = f"0{date.minute}" if date.minute < 10 else str(date.minute)
    second = f"0{date.second}" if date.second < 10 else str(date.second)
    year = str(date.year)[2:4]

    number = year + hour + minute + second + str(date.microsecond)[:3]
    number = conf["Prefix"] + str(number)
    logger.info(f"生成的随机数为:{str(number)}")
    return number

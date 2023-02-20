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
    if date.hour < 10:
        hour = "0" + str(date.hour)
    else:
        hour = str(date.hour)

    if date.minute < 10:
        minute = "0" + str(date.minute)
    else:
        minute = str(date.minute)

    if date.second < 10:
        second = "0" + str(date.second)
    else:
        second = str(date.second)

    year = str(date.year)[2:4]

    number = year + hour + minute + second + str(date.microsecond)[0:3]
    number = conf["Prefix"] + str(number)
    logger.info("生成的随机数为:{}".format(str(number)))
    return number

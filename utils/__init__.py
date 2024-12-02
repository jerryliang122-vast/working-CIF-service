#获取conf中的信息
from .comfig import port
#发送询价邮件
from .email_api import inquiry_smtp
#生成随机编号
from .random_number import reandom
#获取询价数据库
from .email_api import email_sql

#获取发送指定货清单数据库
from .nomination_list_email_send import email_sql as nomination_list_email_sql

#nomination list 发送邮件
from .nomination_list_email_send import smtp as nomination_list_smtp
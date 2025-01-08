import os
import imbox
from imap_tools import imap_utf7
import json
import logging
from sql import email_list, Session
import datetime

logger = logging.getLogger("my_logger")


# 读取邮箱配置
with open("conf/auto_send_bill_to_shpr/email_config.json", "r", encoding="utf-8") as f:
    email_config = json.load(f)

# 数据库操作方法
session = Session()
Agent = email_list


class email_list:
    def __init__(self):
        # 登录邮箱
        self.mail = imbox.Imbox(
            email_config["host"],
            username=email_config["username"],
            password=email_config["password"],
            ssl=True,
            ssl_context=None,
            starttls=False,
        )

    def get_email_floder(self):
        # 获取邮箱文件夹
        folders = self.mail.folders()
        folders = [imap_utf7.decode(folder["name"]) for folder in folders]
        return folders

    # 检查时间
    def check_date(self):
        # 获取今天的日期
        today = datetime.datetime.now().date()
        # 推算一个月前的今天
        last_month = today - datetime.timedelta(days=30)
        return today, last_month

    def get_email_list(self, folder, date, unread=False):
        email_lists = []
        # 获取邮件列表
        for uid, message in self.mail.messages(
            folder=folder, unread=unread, date__gt=date
        ):
            # 获取邮件主题
            subject = message.subject
            # 获取发件人
            sender = message.sent_from
            # 获取收件人
            receiver = message.sent_to
            # 获取邮件日期
            date = message.date
            email_lists.append(
                {
                    "uid": uid,
                    "subject": subject,
                    "sender": sender,
                    "receiver": receiver,
                    "date": date,
                }
            )
        return email_lists

    def main(self):
        # 检查缓存在数据库中的邮件，以及邮件时间。
        get_email_list = self.get_email_list(
            "INBOX", self.check_date()[1], unread=False
        )
        print(get_email_list)


if __name__ == "__main__":
    email_list = email_list()
    email_list.main()

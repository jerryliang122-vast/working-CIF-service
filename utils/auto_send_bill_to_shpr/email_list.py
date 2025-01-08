import os
import imbox
from imap_tools import imap_utf7
import json

# 读取邮箱配置
with open("conf/auto_send_bill_to_shpr/email_config.json", "r", encoding="utf-8") as f:
    email_config = json.load(f)

# 登录邮箱
mail = imbox.Imbox(
    email_config["host"],
    username=email_config["username"],
    password=email_config["password"],
    ssl=True,
    ssl_context=None,
    starttls=False,
)

from imbox import Imbox
import json
import os

# 读取conf email.conf文件
with open(os.path.join(os.getcwd(), "conf", "email.conf"), "r") as f:
    email_conf = f.read()
email_conf = json.loads(email_conf)


def get_folder():
    # 连接邮箱
    with Imbox(
        email_conf["smtp_server"], email_conf["smtp_user"], email_conf["smtp_password"], port=email_conf["smtp_port"]
    ) as imbox:
        # 获取文件夹
        folders = imbox.folders()
        return folders

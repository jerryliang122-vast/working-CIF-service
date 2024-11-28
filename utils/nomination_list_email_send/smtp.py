import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import os
import json
import logging

logger = logging.getLogger("my_logger")
# 邮件模板修改

def mail_template():
    return """
    <html>
    <head>
    <title>nomination list</title>
    </head>
    <body>
    <p>Dear team,<p>
    <p>Att is a list of all the nomination cargos we currently have on hand.</p>
    <p>Hope it can help you to check the current status of the goods more quickly and conveniently.</p>
    <p>Please update it to your corresponding sales staff.</p>
    <p>Thanks and best regards!</p>
    <p>NVOCC#SMTC-NV00275/FMCBond#026678/WCA#92530</p>
    <img src="cid:image1">
    </body>
    </html>
    """


# 邮件发送
def send_mail(name, subject, data):
    try:
        # 使用split函数将邮件作为列表
        email = name.split(",")
        # 从配置文件中获取邮箱账号和密码
        with open(os.path.join(os.getcwd(), "conf", "email.json"), "r") as f:
            email_conf = json.load(f)
        # 读取签名照片
        with open(os.path.join(os.getcwd(), "conf", "signature.jpg"), "rb") as f:
            img_data = f.read()
        msg = MIMEMultipart()
        msg.attach(MIMEText(data, "html"))
        # 图片部分
        img = MIMEImage(img_data, _subtype="jpg")
        img.add_header("Content-ID", "<image1>")
        msg.attach(img)
        # 邮件发送
        msg["Subject"] = subject
        msg["From"] = f'{email_conf["name"]} <{email_conf["smtp_user"]}>'
        msg["To"] = ",".join(email)
        smtp = smtplib.SMTP_SSL(email_conf["smtp_server"], port=email_conf["smtp_port"])
        smtp.login(email_conf["smtp_user"], email_conf["smtp_password"])
        smtp.sendmail(email_conf["smtp_user"], email, msg.as_string())
        smtp.quit()
        return True
    except Exception as e:
        logger.error(e)
        return False

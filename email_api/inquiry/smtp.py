import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import json
from email_api.agent_email_sql import Session, Agent

# 邮件模板data样式
###data = [  ["Row 1, Column 1", "Row 1, Column 2"],
###  ["Row 2, Column 1", "Row 2, Column 2"],
###  ["Row 3, Column 1", "Row 3, Column 2"],
###]


# 处理放置在conf文件中的签名照片
def get_img():
    with open(os.path.join(os.getcwd(), "conf", "signature"), "rb") as f:
        img_data = f.read()
    return img_data


# 邮件模板修改
def mail_template(clasue, address, data):
    # 读取列表数据并生成
    table_rows = ""
    for row in data:
        table_rows += "<tr><td>{}</td><td>{}</td></tr>".format(row[0], row[1])
    # 读取签名照片并转换为base64编码
    img_data = get_img()
    # 邮件模板
    html_template = """
    <html>
    <head>
    <title>DAP shipment</title>
    </head>
    <body>
    <h1>Dear team,</h1>
    <p>This is a {clasue} shipment</p>
    <p>Address:</p>
    <p>{address}</p>
    <table>
        {table_rows}
    </table>
    <p>Thanks and best regards!</p>
    <p>NVOCC#SMTC-NV00275/FMCBond#026678/WCA#92530</p>
    <img src="data:image/jpeg;base64,{encoded_image}" alt="Company logo">
    </body>
    </html>
    """.format(
        clasue=clasue, address=address, table_rows=table_rows, encoded_image=img_data
    )
    return html_template


# 邮件发送
def send_mail(name, clasue, address, data):
    # 读取代理邮箱
    email = Session().read_email(name)
    # 使用split函数将邮件作为列表
    email = email.split(",")
    # 从配置文件中获取邮箱账号和密码
    with open(os.path.join(os.getcwd(), "conf", "email.conf"), "r") as f:
        email_conf = f.read()
    email_conf = json.loads(email_conf)
    # 邮件模板
    html_template = mail_template(clasue, address, data)
    # 邮件发送
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "DAP shipment"
    msg["From"] = email_conf["name"]
    msg["To"] = ",".join(email)
    msg.attach(MIMEText(html_template, "html"))
    # 发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(email_conf["smtp_server"])
    smtp.login(email_conf["smtp_user"], email_conf["smtp_password"])
    smtp.sendmail(email_conf["smtp_user"], email, msg.as_string())
    smtp.quit()
    return True

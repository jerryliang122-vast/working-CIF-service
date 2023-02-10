import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

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

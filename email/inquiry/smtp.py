import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


# 处理放置在conf文件中的签名照片
def get_img():
    with open(os.path.join(os.getcwd(), "conf", "signature"), "rb") as f:
        img_data = f.read()
    return img_data

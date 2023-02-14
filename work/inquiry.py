import sys
import json
import os
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QListView, QAbstractItemView
from PyQt6.QtWidgets import QMessageBox
from email_api.agent_email_sql import Agent, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, TEXT
import logging
from email_api.inquiry.smtp import mail_template


# 获取港口信息
with open(os.path.join(os.getcwd(), "conf", "port.json"), "r", encoding="utf-8") as f:
    port_conf = f.read()
port_conf = json.loads(port_conf)


# 数据库操作方法
session = Session()


def insert(name, email):
    agent = Agent(name=name, email=email)
    session.add(agent)


# 读取代理名字
def read_name():
    data = session.query(Agent.name).all()
    # 将元组转换成列表
    data = [i[0] for i in data]
    return data


# 读取代理邮箱
def read_email(name):
    data = session.query(Agent.email).filter(Agent.name == name).first()
    return data[0]


# 按照港口读取代理名称列表
def read_port_name(port):
    data = session.query(Agent.name).filter(Agent.port.like("%{}%".format(port))).all()
    data = [i[0] for i in data]
    return data


# 按照港口写入或更新代理email信息和名称
def write_port_name(port, name, email):
    try:
        # 先查询是否有此港口的代理
        data = session.query(Agent.name).filter(Agent.port.like("%{}%".format(port))).all()
        data = [i[0] for i in data]
        if name in data:
            # 更新
            session.query(Agent).filter(Agent.name == name).update({Agent.email: email})
        else:
            # 写入
            agent = Agent(port=port, name=name, email=email)
            session.add(agent)
        # 提交
        session.commit()
        return True
    except Exception as e:
        logging.error(e)
        return False


class work_inquiry:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.hangxian.currentIndexChanged.connect(self.get_country)
        self.main_window.guojia.currentIndexChanged.connect(self.get_port)
        self.main_window.add_agent_email.clicked.connect(self.write_proxy)
        self.main_window.daili_list_update.clicked.connect(self.get_proxy)
        self.main_window.Preview_email.clicked.connect(self.preview)

    # 根据选择的航线，获取json中的国家
    def get_country(self):
        ship_route = self.main_window.hangxian.currentText()
        country = list(port_conf[ship_route].keys())
        # 更新到ComboBox
        self.main_window.guojia.clear()
        self.main_window.guojia.addItems(country)
        return country

    # 根据选择的国家，获取json中的港口
    def get_port(self):
        ship_route = self.main_window.hangxian.currentText()
        country = self.main_window.guojia.currentText()
        if country:
            port = port_conf[ship_route][country]
            # 更新到ComboBox
            self.main_window.gangkou.clear()
            self.main_window.gangkou.addItems(port)
            return port

    # 使用listview显示代理信息
    def get_proxy(self):
        model = QStandardItemModel(self.main_window.daili_list)
        # 从数据库中获取代理信息

        # 读取此港口下的代理列表
        proxy_infos = read_port_name(self.main_window.gangkou.currentText())
        for info in proxy_infos:
            item = QStandardItem(info)
            item.setCheckable(True)
            model.appendRow(item)

        self.main_window.daili_list.setModel(model)

    # 代理信息写入数据库
    def write_proxy(self):
        # 读取选择的航线信息
        ship_route = self.main_window.hangxian.currentText()
        # 读取选择的国家信息
        country = self.main_window.guojia.currentText()
        # 读取选择的港口信息
        port = self.main_window.gangkou.currentText()
        # 读取代理名字
        proxy_name = self.main_window.agent_name.text()
        # 读取代理邮箱
        proxy_email = self.main_window.agent_email_list.toPlainText()
        # 处理代理邮箱数据。将换行符替换成逗号
        proxy_email = proxy_email.replace("\n", ",")
        # 向数据库写入数据
        data = write_port_name(port, proxy_name, proxy_email)
        # 判断是否写入成功
        if data:
            # 弹出界面提示
            QMessageBox.about(self.main_window, "提示", "写入成功")
        else:
            QMessageBox.about(self.main_window, "提示", "写入失败")

    # 预览
    def preview(self):
        # 获取地址
        address = self.main_window.address.toPlainText()
        # 获取件数
        number = self.main_window.PKGS.text()
        # 获取重量
        weight = self.main_window.KGS.text()
        # 获取体积
        volume = self.main_window.CBM.text()
        # 获取货物单件体积
        single_volume = self.main_window.size.text()
        # 获取HS 编码
        hs_code = self.main_window.HS.text()
        # 获取货物描述
        goods_description = self.main_window.cargoname.text()
        # 获取条款
        clause = self.main_window.clause.currentText()
        # 处理货物数据
        ###data = [  ["Row 1, ", "Row 1, Column 2"],
        ###  ["Row 2, Column 1", "Row 2, Column 2"],
        ###  ["Row 3, Column 1", "Row 3, Column 2"],
        ###]
        data = [
            ["quantity", f"{number}"],
            ["weight", f"{weight}"],
            ["volume", f"{volume}"],
            ["single_volume", f"{single_volume}"],
            ["hs_code", f"{hs_code}"],
        ]
        # 渲染模板
        global template  # 设置为全局变量
        template = mail_template(clause, address, data)
        # 显示到textedit界面
        self.main_window.emailtext.setHtml(template)

import sys
import os
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QListView, QAbstractItemView, QMainWindow, QMessageBox, QHeaderView
from utils import email_sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, TEXT
import logging
from utils import inquiry_smtp
from utils import port
logger = logging.getLogger("my_logger")

# 获取港口信息
port_conf = port()


# 数据库操作方法
session = email_sql.Session()
Agent = email_sql.Agent

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
def read_email(name, port):
    data = session.query(Agent.email).filter(Agent.name == name, Agent.port == port).first()
    return data[0]


# 按照港口读取代理名称列表
def read_port_name(port):
    data = session.query(Agent.name).filter(Agent.port.like(f"%{port}%")).all()
    data = [i[0] for i in data]
    return data


# 按照港口写入或更新代理email信息和名称
def write_port_name(port, name, email):
    try:
        # 先查询是否有此港口的代理
        data = session.query(Agent.name).filter(Agent.port.like(f"%{port}%")).all()
        data = [i[0] for i in data]
        if name in data:
            # 更新
            session.query(Agent).filter(Agent.name == name, Agent.port == port).update({Agent.email: email})
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
        self.get_line()
        self.get_country()
        self.get_port()
        self.main_window.hangxian.currentIndexChanged.connect(self.get_country)
        self.main_window.guojia.currentIndexChanged.connect(self.get_port)
        self.main_window.gangkou.currentIndexChanged.connect(self.get_proxy)
        self.main_window.add_agent_email.clicked.connect(self.write_proxy)
        self.main_window.Preview_email.clicked.connect(self.preview)
        self.main_window.send_email.clicked.connect(self.send_email)
        self.main_window.aoto.clicked.connect(self.random_number)
        self.main_window.delete_data.clicked.connect(self.delete_data)

    #自动生成航线菜单栏中的内容
    def get_line(self):
        self.main_window.hangxian.clear()
        #读取航线
        line = list(port_conf.get_line())
        self.main_window.hangxian.addItems(line)

    # 根据选择的航线，获取json中的国家
    def get_country(self):
        ship_route = self.main_window.hangxian.currentText()
        country = list(port_conf.get_country(ship_route))
        # 更新到ComboBox
        self.main_window.guojia.clear()
        self.main_window.guojia.addItems(country)
        return country

    # 根据选择的国家，获取json中的港口
    def get_port(self):
        ship_route = self.main_window.hangxian.currentText()
        if country := self.main_window.guojia.currentText():
            port = list(port_conf.get_port(ship_route,country))
            # 更新到ComboBox
            self.main_window.gangkou.clear()
            self.main_window.gangkou.addItems(port)
            return port

    # 使用listview显示代理信息
    def get_proxy(self):
        # 读取此港口下的代理列表
        proxy_infos = read_port_name(self.main_window.gangkou.currentText())

        model = QStandardItemModel()
        for info in proxy_infos:
            item = QStandardItem(info)
            item.setCheckable(True)
            model.appendRow(item)
        self.main_window.daili_list.setModel(model)
        self.main_window.daili_list.selectionModel().currentRowChanged.connect(self.update_addresslist)

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
        if data := write_port_name(port, proxy_name, proxy_email):
            # 弹出界面提示
            QMessageBox.about(self.main_window, "提示", "写入成功")
        else:
            QMessageBox.about(self.main_window, "提示", "写入失败")

    # 预览
    def preview_data(self):
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
        # 获取港口
        port = self.main_window.port.text()
        # 处理货物数据
        ###data = [  ["Row 1, ", "Row 1, Column 2"],
        ###  ["Row 2, Column 1", "Row 2, Column 2"],
        ###  ["Row 3, Column 1", "Row 3, Column 2"],
        ###]
        if port == "":
            port = "Please recommend a nearest port"
        if single_volume == "":
            single_volume = "N/A"
        if hs_code == "":
            hs_code = "N/A"
        if goods_description == "":
            goods_description = "N/A"
        data = [
            ["quantity", f"{number}"],
            ["weight", f"{weight}"],
            ["volume", f"{volume}"],
            ["cargo_size", f"{single_volume}"],
            ["hs_code", f"{hs_code}"],
            ["cargo_description", f"{goods_description}"],
        ]
        return inquiry_smtp.mail_template(clause, port, address, data)

    # 预览显示到界面
    def preview(self):
        # 获取模板
        template = self.preview_data()
        # 显示到textedit界面
        self.main_window.emailtext.setHtml(template)

    # 发送邮件
    def send_email(self):
        try:
            # 获取条款
            clause = self.main_window.clause.currentText()
            # 获取询价编号
            inquiry_number = self.main_window.inquiry_number.text()
            # 设计邮件主题
            subject = f"Inquiry {clause} price == {inquiry_number}"
            # 从listview中获取选中代理信息
            selected_indexes = self.main_window.daili_list.selectedIndexes()
            # 获取港口
            port = self.main_window.gangkou.currentText()
            # 获取模板
            template = self.preview_data()
            for index in selected_indexes:
                proxy_infos = read_email(index.data(), port)
                # 发送邮件
                report = inquiry_smtp.send_mail(proxy_infos, subject, template)
            # 判断reports列表中是否含有false
            if report == False:
                QMessageBox.about(self.main_window, "提示", "发送失败")
            else:
                QMessageBox.about(self.main_window, "提示", "发送成功")
        except Exception as e:
            QMessageBox.about(self.main_window, "提示", "出现崩溃")
            logger.error(e)

    # 随机生成询价编号
    def random_number(self):
        from utils import reandom

        inquiry_number = reandom()
        self.main_window.random_number.clear()
        self.main_window.random_number.appendPlainText(inquiry_number)

    # 显示代理邮箱
    def update_addresslist(self, current, previous):
        # 获取当前选中项的名称
        selected_item = self.main_window.daili_list.model().itemFromIndex(current)
        selected_name = selected_item.text()
        # 获取港口
        port = self.main_window.gangkou.currentText()
        # 获取代理邮箱
        email = read_email(selected_name, port)
        # email做成列表
        email_list = email.split(",")
        # 创建表格模型并填充数据
        model = QStandardItemModel()
        header_labels = ["邮箱"]
        model.setHorizontalHeaderLabels(header_labels)
        for item in email_list:
            item_email = QStandardItem(item.strip())  # 使用strip()方法去掉元素中的空格
            model.appendRow([item_email])
        self.main_window.addresslist.setModel(model)
        header = self.main_window.addresslist.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # 删除填充的所有数据
    def delete_data(self):
        self.main_window.address.clear()
        self.main_window.PKGS.clear()
        self.main_window.KGS.clear()
        self.main_window.CBM.clear()
        self.main_window.size.clear()
        self.main_window.HS.clear()
        self.main_window.cargoname.clear()
        self.main_window.port.clear()
        self.main_window.emailtext.clear()
        self.main_window.agent_name.clear()
        self.main_window.agent_email_list.clear()
        self.main_window.random_number.clear()
        self.main_window.inquiry_number.clear()
        #弹出提示
        QMessageBox.about(self.main_window, "提示", "清空成功")
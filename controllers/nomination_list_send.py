import sys
import os
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import (
    QListView,
    QAbstractItemView,
    QMainWindow,
    QMessageBox,
    QHeaderView,
)
from utils import nomination_list_email_sql
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, TEXT
import logging
from utils import nomination_list_smtp
from utils import port
from Ui.Ui_untitled import Ui_Form

logger = logging.getLogger("my_logger")


# 获取港口信息
port_conf = port()


# 数据库操作方法
session = nomination_list_email_sql.Session()
Agent = nomination_list_email_sql.Agent


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
    data = (
        session.query(Agent.email)
        .filter(Agent.name == name, Agent.port == port)
        .first()
    )
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
            session.query(Agent).filter(Agent.name == name, Agent.port == port).update(
                {Agent.email: email}
            )
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


def delete_agent_by_port_and_name(port, name):
    try:
        # 查询指定港口和名称的代理
        agent = (
            session.query(Agent)
            .filter(Agent.port.like(f"%{port}%"), Agent.name == name)
            .first()
        )
        if agent:
            # 如果代理存在，则删除
            session.delete(agent)
            session.commit()
            return True
        else:
            # 如果代理不存在，返回 False
            return False
    except Exception as e:
        # 打印错误信息到日志
        logging.error(e)
        return False


class nomination_list_send:
    def __init__(self, main_window):
        self.main_window = main_window
        self.get_line()
        self.get_country()
        self.get_port()
        self.get_proxy()
        self.main_window.nom_line.currentIndexChanged.connect(self.get_country)
        self.main_window.nom_countries.currentIndexChanged.connect(self.get_port)
        self.main_window.nom_port.currentIndexChanged.connect(self.get_proxy)
        self.main_window.nom_agent_add.clicked.connect(self.write_proxy)
        self.main_window.nom_agent_delete.clicked.connect(self.delete_agent)
        self.main_window.nom_file_list_update.clicked.connect(self.nomination_list_file)
        self.main_window.nom_email_send.clicked.connect(self.send_email)
        


    # 自动生成航线菜单栏中的内容
    def get_line(self):
        self.main_window.nom_line.clear()
        # 读取航线
        line = list(port_conf.get_line())
        self.main_window.nom_line.addItems(line)

    # 根据选择的航线，获取json中的国家
    def get_country(self):
        ship_route = self.main_window.nom_line.currentText()
        country = list(port_conf.get_country(ship_route))
        # 更新到ComboBox
        self.main_window.nom_countries.clear()
        self.main_window.nom_countries.addItems(country)
        return country

    # 根据选择的国家，获取json中的港口
    def get_port(self):
        ship_route = self.main_window.nom_line.currentText()
        if country := self.main_window.nom_countries.currentText():
            port = list(port_conf.get_port(ship_route, country))
            # 更新到ComboBox
            self.main_window.nom_port.clear()
            self.main_window.nom_port.addItems(port)
            return port
        
    # 获取文件列表 并显示在nom_file_list
    def nomination_list_file(self):
        # 获取文件列表
        file_list = os.listdir(os.path.join('conf','nomination_list'))
        # 创建表格模型并填充数据
        model = QStandardItemModel()
        for file in file_list:
            item = QStandardItem(file)
            item.setCheckable(False)
            model.appendRow(item)
        self.main_window.nom_file_list.setModel(model)
        header = self.main_window.nom_file_list.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # 使用listview显示代理信息
    def get_proxy(self):
        # 读取此港口下的代理列表
        proxy_infos = read_port_name(self.main_window.nom_port.currentText())

        model = QStandardItemModel()
        for info in proxy_infos:
            item = QStandardItem(info)
            item.setCheckable(False)
            model.appendRow(item)
        self.main_window.nom_port_list.setModel(model)
        self.main_window.nom_port_list.selectionModel().currentRowChanged.connect(
            self.update_addresslist
        )

        # 代理信息写入数据库
    def write_proxy(self):
        # 读取选择的港口信息
        port = self.main_window.nom_port.currentText()
        # 读取代理名字
        proxy_name = self.main_window.nom_agent_name.text()
        # 读取代理邮箱
        proxy_email = self.main_window.nom_agent_email_list.toPlainText()
        # 处理代理邮箱数据。将换行符替换成逗号
        proxy_email = proxy_email.replace("\n", ",")
        if data := write_port_name(port, proxy_name, proxy_email):
            # 弹出界面提示
            QMessageBox.about(self.main_window, "提示", "写入成功")
        else:
            QMessageBox.about(self.main_window, "提示", "写入失败")

    # 显示代理邮箱
    def update_addresslist(self, current, previous):
        # 获取当前选中项的名称
        selected_item = self.main_window.nom_port_list.model().itemFromIndex(current)
        selected_name = selected_item.text()
        # 获取港口
        port = self.main_window.nom_port.currentText()
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
        self.main_window.nom_email_list.setModel(model)
        header = self.main_window.nom_email_list.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    # 删除数据库中存储的代理信息
    def delete_agent(self):
        try:
            # 从daili_list中获取选中代理信息
            selected_indexes = self.main_window.nom_port_list.selectedIndexes()
            # 获取港口
            port = self.main_window.nom_port.currentText()
            # 将选中的代理信息返回到delete_agent_by_port_and_name
            for index in selected_indexes:
                delete_info = delete_agent_by_port_and_name(port, index.data())
                if delete_info:
                    # 弹出提示信息
                    QMessageBox.about(self.main_window, "提示", "删除成功")
                else:
                    # 弹出提示信息
                    QMessageBox.about(self.main_window, "提示", "删除失败")
        except Exception as e:
            # 弹出提示信息
            QMessageBox.about(self.main_window, "提示", "出现崩溃")
            logger.error(e)
    
    # 发送邮件
    def send_email(self):
        try:
            # 获取邮件主题
            subject = self.main_window.nom_email_subject.text()
            # 从listview中获取选中代理信息
            selected_indexes = self.main_window.nom_port_list.selectedIndexes()
            # 获取港口
            port = self.main_window.nom_port.currentText()
            # 获取从nom_file_list 中的文件名称
            file_name = self.main_window.nom_file_list.selectedIndexes()
            #拼接文件路径
            file_path = os.path.join(os.getcwd(), 'conf','nomination_list', file_name[0].data())
            proxy_infos = read_email(selected_indexes[0].data(), port)
            # 发送邮件
            report = nomination_list_smtp.send_mail(proxy_infos, subject, file_path)
            # 判断reports列表中是否含有false
            if report == False:
                QMessageBox.about(self.main_window, "提示", "发送失败")
            else:
                QMessageBox.about(self.main_window, "提示", "发送成功")
        except Exception as e:
            QMessageBox.about(self.main_window, "提示", "出现崩溃")
            logger.error(e)
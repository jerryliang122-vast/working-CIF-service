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
from utils import inquiry_smtp
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


class work_inquiry:
    def __init__(self, main_window):
        self.main_window = main_window
        self.get_line()
        self.get_country()
        self.get_port()


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
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
from utils import email_sql
import logging
import re

class BillCalculate():
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.bill_output.clicked.connect(self.calculate_bill)
        self.main_window.bill_clean.clicked.connect(self.clean)

    #计算方式
    def calculate(self,bill_number,separator,exclude_number):
        #根据英文,分割bill_number
        bill_number_list = bill_number.split(separator)
        new_bill_number_list = []
        for i in bill_number_list:
            #使用正则表达式
            if not re.search(exclude_number, i):
                new_bill_number_list.append(i)
        return new_bill_number_list


    def calculate_bill(self):
        # 获取输入框中的值
        bill_number = self.main_window.bill_number.toPlainText()
        # 获取输入框分隔符
        separator = self.main_window.bill_split.text()
        # 输入需要剔除的编号
        exclude_number = self.main_window.bill_splitout.toPlainText()
        #计算
        bill_number_list = self.calculate(bill_number,separator,exclude_number)
        #显示到qplaintextedit
        self.main_window.bill_out.setPlainText(str(bill_number_list))
        self.main_window.bill_out2.setPlainText(str(len(bill_number_list)))

    def clean(self):
        self.main_window.bill_out.clear()
        self.main_window.bill_out2.clear()
        self.main_window.bill_number.clear()
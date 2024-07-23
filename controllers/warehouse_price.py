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
import yaml



class warehouse_price():
    def __init__(self, main_window):
        self.main_window = main_window
        self.check_config_folder()
        self.main_window.wright_yaml.clicked.connect(self.write_warehouse_stander)
        self.main_window.clean_cfs_charge.clicked.connect(self.clear_field)
        self.main_window.pushButton_4.clicked.connect(self.read_warehouse_stander)

    

    #检查config文件夹中是否有warehouse，没有则创建。
    def check_config_folder(self):
        if not os.path.exists("conf/warehouse"):
            os.mkdir("conf/warehouse")
    
    #当按下写入键后，写入文件到config/warehouse
    def write_warehouse_stander(self):
        stander_name = self.main_window.cfs_name.text()
        BL_charge = self.main_window.cfs_bl_charge.text()
        #外港上下车费
        cfs_yg_pkgs_charge = self.main_window.cfs_yg_pkgs_charge.text()
        cfs_yg_weight_charge = self.main_window.cfs_yg_weight_charge.text()
        cfs_yg_cmb_charge = self.main_window.cfs_yg_cmb_charge.text()
        cfs_yg_mini_charge = self.main_window.cfs_yg_mini_charge.text()
        #洋山收费标准
        cfs_ys_pkgs_charge = self.main_window.cfs_ys_pkgs_charge.text()
        cfs_ys_weight_charge = self.main_window.cfs_ys_weight_charge.text()
        cfs_ys_cbm_charge = self.main_window.cfs_ys_cbm_charge.text()
        cfs_ys_mini_charge = self.main_window.cfs_ys_mini_charge.text()
        #厢式车
        cfs_van_charge = self.main_window.cfs_van_charge.text()
        #超大费
        cfs_ows_charge = self.main_window.cfs_ows_charge.text()
        #保险费
        cfs_Insurance_charge = self.main_window.cfs_Insurance_charge.text()
        #配置成字典
        cfs_stander = {
            "BL_charge": BL_charge,
            "cfs_yg_pkgs_charge": cfs_yg_pkgs_charge,
            "cfs_yg_weight_charge": cfs_yg_weight_charge,
            "cfs_yg_cmb_charge": cfs_yg_cmb_charge,
            "cfs_yg_mini_charge": cfs_yg_mini_charge,
            "cfs_ys_pkgs_charge": cfs_ys_pkgs_charge,
            "cfs_ys_weight_charge": cfs_ys_weight_charge,
            "cfs_ys_cbm_charge": cfs_ys_cbm_charge,
            "cfs_ys_mini_charge": cfs_ys_mini_charge,
            "cfs_van_charge": cfs_van_charge,
            "cfs_ows_charge": cfs_ows_charge,
            "cfs_Insurance_charge": cfs_Insurance_charge,
        }
        #检查warehouse文件夹中是否已经由对应的名称
        if os.path.exists(f"conf/warehouse/{stander_name}.yaml"):
            #弹出框询问是否覆盖
            if QMessageBox.question(
                self.main_window,
                "提示",
                "文件已存在，是否覆盖？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            ) == QMessageBox.StandardButton.Yes:
                with open(f"conf/warehouse/{stander_name}.yaml", "w", encoding="utf-8") as f:
                    yaml.dump(cfs_stander, f, allow_unicode=True, default_flow_style=False)
        else:
            #写入文件
            with open(f"conf/warehouse/{stander_name}.yaml", "w", encoding="utf-8") as f:
                yaml.dump(cfs_stander, f, allow_unicode=True, default_flow_style=False)

    #清除字段
    def clear_field(self):
        self.main_window.cfs_name.clear()
        self.main_window.cfs_bl_charge.clear()
        self.main_window.cfs_yg_pkgs_charge.clear()
        self.main_window.cfs_yg_weight_charge.clear()
        self.main_window.cfs_yg_cmb_charge.clear()
        self.main_window.cfs_yg_mini_charge.clear()
        self.main_window.cfs_ys_pkgs_charge.clear()
        self.main_window.cfs_ys_weight_charge.clear()
        self.main_window.cfs_ys_cbm_charge.clear()
        self.main_window.cfs_ys_mini_charge.clear()
        self.main_window.cfs_van_charge.clear()
        self.main_window.cfs_ows_charge.clear()
        self.main_window.cfs_Insurance_charge.clear()
        #弹框
        QMessageBox.information(self.main_window, "提示", "清除成功")

    
    #读取conf/warehouse 文件并呈现在QlistView中对象名为stander_list
    def read_warehouse_stander(self):
        # 创建表格模型并填充数据
        model = QStandardItemModel()
        header_labels = ["名称"]
        model.setHorizontalHeaderLabels(header_labels)
        for file in os.listdir("conf/warehouse"):
            if file.endswith(".yaml"):
                item = QStandardItem(file.replace(".yaml", ""))
                model.appendRow([item])
        self.main_window.stander_list.setModel(model)
        self.main_window.stander_list.selectionModel().currentRowChanged.connect(self.read_and_show_warehouse_stander)

    #读取conf/warehouse 并写入标准的登记配置
    def read_and_show_warehouse_stander(self, current):
        stander_name  = self.main_window.stander_list.model().itemFromIndex(current)
        stander_name = stander_name.text()
        with open(f"conf/warehouse/{stander_name}.yaml", "r", encoding="utf-8") as f:
            cfs_stander = yaml.load(f, Loader=yaml.FullLoader)
        self.main_window.cfs_name.setText(stander_name)
        self.main_window.cfs_bl_charge.setText(cfs_stander['BL_charge'])
        self.main_window.cfs_yg_pkgs_charge.setText(cfs_stander['cfs_yg_pkgs_charge'])
        self.main_window.cfs_yg_weight_charge.setText(cfs_stander['cfs_yg_weight_charge'])
        self.main_window.cfs_yg_cmb_charge.setText(cfs_stander['cfs_yg_cmb_charge'])
        self.main_window.cfs_yg_mini_charge.setText(cfs_stander['cfs_yg_mini_charge'])
        self.main_window.cfs_ys_pkgs_charge.setText(cfs_stander['cfs_ys_pkgs_charge'])
        self.main_window.cfs_ys_weight_charge.setText(cfs_stander['cfs_ys_weight_charge'])
        self.main_window.cfs_ys_cbm_charge.setText(cfs_stander['cfs_ys_cbm_charge'])
        self.main_window.cfs_ys_mini_charge.setText(cfs_stander['cfs_ys_mini_charge'])
        self.main_window.cfs_van_charge.setText(cfs_stander['cfs_van_charge'])
        self.main_window.cfs_ows_charge.setText(cfs_stander['cfs_ows_charge'])
        self.main_window.cfs_Insurance_charge.setText(cfs_stander['cfs_Insurance_charge'])

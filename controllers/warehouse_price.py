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
        self.main_window.wright_yaml.currentIndexChanged.connect(self.write_warehouse_stander)

    

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
        #写入文件
        with open(f"conf/warehouse/{stander_name}.yaml", "w", encoding="utf-8") as f:
            yaml.dump(cfs_stander, f, allow_unicode=True, default_flow_style=False)

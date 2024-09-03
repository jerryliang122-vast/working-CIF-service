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
        self.main_window.use_cfs_numebr_calculate.clicked.connect(self.calculate_warehouse_price_no)

    

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

    #计算仓库费用, 使用进仓费编号计算
    def calculate_warehouse_price_no(self):
        cargo_data = {
            "warehouse_name":self.main_window.chose_cfs_name.currentText(),
            "warehouse_in_out":self.main_window.cfs_inout_chose.currentText(),
            "cfs_pallets": self.main_window.cfs_pallets.isChecked(),
            "cfs_night_in": self.main_window.cfs_night_in.isChecked(),
            "cfs_van": self.main_window.cfs_van.isChecked(),
            "cfs_pkgs": self.main_window.cfs_pkgs.text(),
            "cfs_tone": self.main_window.cfs_tone.text(),
            "cfs_cbm": self.main_window.cfs_cbm.text(),
            "cargo_dims": self.main_window.cargo_dims.text(),
            "cfs_number": self.main_window.cfs_number.text(),
            "cfs_discount_price": self.main_window.cfs_discount_price.text(),
            "where_cfs_discount": self.main_window.where_cfs_discount.currentText(),
            "cfs_discount": self.main_window.cfs_discount.isChecked(),
        }
        cargo_stander = {
            "cfs_name": self.main_window.cfs_name.text(),
            "cfs_bl_charge" : self.main_window.cfs_bl_charge.text(),
            "cfs_yg_pkgs_charge" : self.main_window.cfs_yg_pkgs_charge.text(),
            "cfs_yg_weight_charge" : self.main_window.cfs_yg_weight_charge.text(),
            "cfs_yg_cmb_charge" : self.main_window.cfs_yg_cmb_charge.text(),
            "cfs_yg_mini_charge" : self.main_window.cfs_yg_mini_charge.text(),
            "cfs_ys_pkgs_charge" : self.main_window.cfs_ys_pkgs_charge.text(),
            "cfs_ys_weight_charge" : self.main_window.cfs_ys_weight_charge.text(),
            "cfs_ys_cbm_charge" : self.main_window.cfs_ys_cbm_charge.text(),
            "cfs_ys_mini_charge": self.main_window.cfs_ys_mini_charge.text(),
            "cfs_van_charge" : self.main_window.cfs_van_charge.text(),
            "cfs_ows_charge" : self.main_window.cfs_ows_charge.text(),
            "cfs_Insurance_charge" : self.main_window.cfs_Insurance_charge.text(),
        }
        #加载网页查询
        import utils.warehouse.web as web 
        import utils.warehouse.cfs_wg as cfs_wg
        if cargo_data['warehouse_name'] == '外港仓库':
            cargo_data_web = web.web_grasp(False,cargo_data["cfs_number"])
            web_data =cargo_data_web.get_data()
        else:
            cargo_data_web = web.web_grasp(True,cargo_data["cfs_number"])
            web_data =cargo_data_web.get_data()
        #网页参数返回如下[{'time': 10, 'car_model': True, 'cargo_id': 'HWMAA2400934N-MF', 'goods': [{'pkgs_type': False, 'pkgs': '20', 'weight': '200.000', 'volume': '0.661', 'dims': '36.0×34.0×27.0'}]}, {'time': 16, 'car_model': True, 'cargo_id': 'HWMAA2400934N-MF', 'goods': [{'pkgs_type': False, 'pkgs': '24', 'weight': '175.000', 'volume': '0.800', 'dims': '35.0×34.0×28.0'}]}]
        if cargo_data_web == None:
            QMessageBox.information(self.main_window, "提示", "没有找到此单号，请检查单号是否正确")
            return
        if all(v is not None and v != '' for v in cargo_stander.values()) == False:
            QMessageBox.information(self.main_window, "提示", "请先设置仓库标准")
            return
        #在web_data中添加一些数据
        discount = {
            'where_cfs_discount': cargo_data["where_cfs_discount"],
            'cfs_discount': cargo_data["cfs_discount"],
            'cfs_discount_price': cargo_data["cfs_discount_price"]
        }

        if cargo_data["warehouse_name"] == "外港仓库":
            cargo_calculate = cfs_wg.calculate_cfs_wg(web_data,cargo_stander,discount)
            cargo_data_calculate = cargo_calculate.main()
        #将数据显示在cfs_price_output 的QTextEdit中
        self.main_window.cfs_price_output.setText(str(cargo_data_calculate))
        return
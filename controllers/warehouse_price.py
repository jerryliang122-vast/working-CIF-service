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
import utils.warehouse.web as web 
import utils.warehouse.cfs_wg as cfs_wg


class WebDataThread(QThread):
    '''
    
    '''
    finished = pyqtSignal(dict)  # 信号，用于在线程完成后发送结果

    def __init__(self, cargo_data, cargo_stander):
        super().__init__()
        self.cargo_data = cargo_data
        self.cargo_stander = cargo_stander

    def run(self):
        # 根据仓库名称选择不同的网页抓取方式
        if self.cargo_data['warehouse_name'] == '外港仓库':
            cargo_data_web = web.web_grasp(False, self.cargo_data["cfs_number"])
            web_data = cargo_data_web.get_data()
        else:
            cargo_data_web = web.web_grasp(True, self.cargo_data["cfs_number"])
            web_data = cargo_data_web.get_data()
        
        # 如果没有找到单号，则弹出提示框
        if cargo_data_web is None:
            QMessageBox.information(self.main_window, "提示", "没有找到此单号，请检查单号是否正确")
            return
        
        # 如果仓库标准没有设置，则弹出提示框
        if all(v is not None and v != '' for v in self.cargo_stander.values()) == False:
            QMessageBox.information(self.main_window, "提示", "请先设置仓库标准")
            return
        
        # 获取折扣信息
        discount = {
            'where_cfs_discount': self.cargo_data["where_cfs_discount"],
            'cfs_discount': self.cargo_data["cfs_discount"],
            'cfs_discount_price': self.cargo_data["cfs_discount_price"]
        }

        # 根据仓库名称选择不同的计算方式
        if self.cargo_data["warehouse_name"] == "外港仓库":
            cargo_calculate = cfs_wg.calculate_cfs_wg(web_data, self.cargo_stander, discount)
            cargo_data_calculate = cargo_calculate.main()
        
        self.finished.emit(cargo_data_calculate)  # 发送结果信号



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
        # 定义一个字典cargo_data，用于存储货物信息
        cargo_data = {
            "warehouse_name":self.main_window.chose_cfs_name.currentText(),  # 仓库名称
            "warehouse_in_out":self.main_window.cfs_inout_chose.currentText(),  # 仓库进出
            "cfs_pallets": self.main_window.cfs_pallets.isChecked(),  # 是否有托盘
            "cfs_night_in": self.main_window.cfs_night_in.isChecked(),  # 是否夜间进仓
            "cfs_van": self.main_window.cfs_van.isChecked(),  # 是否有货车
            "cfs_pkgs": self.main_window.cfs_pkgs.text(),  # 货物件数
            "cfs_tone": self.main_window.cfs_tone.text(),  # 货物吨数
            "cfs_cbm": self.main_window.cfs_cbm.text(),  # 货物体积
            "cargo_dims": self.main_window.cargo_dims.text(),  # 货物尺寸
            "cfs_number": self.main_window.cfs_number.text(),  # 货物编号
            "cfs_discount_price": self.main_window.cfs_discount_price.text(),  # 货物折扣价格
            "where_cfs_discount": self.main_window.where_cfs_discount.currentText(),  # 货物折扣位置
            "cfs_discount": self.main_window.cfs_discount.isChecked(),  # 是否有货物折扣
        }
        # 定义一个字典cargo_stander，用于存储货物标准信息
        cargo_stander = {
            "cfs_name": self.main_window.cfs_name.text(),  # 货物名称
            "cfs_bl_charge" : self.main_window.cfs_bl_charge.text(),  # 货物BL费用
            "cfs_yg_pkgs_charge" : self.main_window.cfs_yg_pkgs_charge.text(),  # 货物运费（件数）
            "cfs_yg_weight_charge" : self.main_window.cfs_yg_weight_charge.text(),  # 货物运费（重量）
            "cfs_yg_cmb_charge" : self.main_window.cfs_yg_cmb_charge.text(),  # 货物运费（体积）
            "cfs_yg_mini_charge" : self.main_window.cfs_yg_mini_charge.text(),  # 货物运费（最小费用）
            "cfs_ys_pkgs_charge" : self.main_window.cfs_ys_pkgs_charge.text(),  # 货物运输费用（件数）
            "cfs_ys_weight_charge" : self.main_window.cfs_ys_weight_charge.text(),  # 货物运输费用（重量）
            "cfs_ys_cbm_charge" : self.main_window.cfs_ys_cbm_charge.text(),  # 货物运输费用（体积）
            "cfs_ys_mini_charge": self.main_window.cfs_ys_mini_charge.text(),  # 货物运输费用（最小费用）
            "cfs_van_charge" : self.main_window.cfs_van_charge.text(),  # 货物货车费用
            "cfs_ows_charge" : self.main_window.cfs_ows_charge.text(),  # 货物其他费用
            "cfs_Insurance_charge" : self.main_window.cfs_Insurance_charge.text(),  # 货物保险费用
        }
        # 创建一个WebDataThread线程，用于处理货物信息
        thread = WebDataThread(cargo_data, cargo_stander)
        # 当线程完成时，调用update_ui_with_result函数
        thread.finished.connect(self.update_ui_with_result)
        # 启动线程
        thread.start()

        return
        # 定义一个函数update_ui_with_result，用于更新UI界面
    def update_ui_with_result(self, result):
        # 将计算结果输出到UI界面的cfs_price_output文本框中
        self.main_window.cfs_price_output.setText(str(result))
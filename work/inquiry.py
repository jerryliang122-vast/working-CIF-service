import sys
import json
import os

# 获取港口信息
with open(os.path.join(os.getcwd(), "conf", "port.json"), "r", encoding="utf-8") as f:
    port_conf = f.read()
port_conf = json.loads(port_conf)


class work_inquiry:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.hangxian.currentIndexChanged.connect(self.get_country)
        self.main_window.guojia.currentIndexChanged.connect(self.get_port)

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

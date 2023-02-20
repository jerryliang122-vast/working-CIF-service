# 初始化
import os
import sys

# 检查工作目录下是否有conf文件夹
if not os.path.exists("conf"):
    # 没有的话直接重命名init_conf文件夹为conf
    os.rename("init_conf", "conf")

from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_untitled import Ui_Form
import sys
from work.inquiry import work_inquiry

# sys导出控制台的输出
sys.stdout = open("log.log", "w", encoding="utf-8")


class wm(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.combo_box_handler = work_inquiry(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = wm()
    mainwindow.show()
    app.exec()

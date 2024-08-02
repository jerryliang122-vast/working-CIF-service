# 初始化
import os
import sys
import config.config

# 检查工作目录下是否有conf文件夹,执行初始化
if not os.path.exists("conf"):
    # 没有的话新建一个conf文件夹，并执行
    os.mkdir("conf")
config.config.main()
from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui.Ui_untitled import Ui_Form
import sys
from controllers import work_inquiry
from controllers import BillCalculate
import logging

logpath = os.path.join(os.getcwd(), "log.log")
logging.basicConfig(
    level=logging.DEBUG,  # 级别：CRITICAL > ERROR > WARNING > INFO > DEBUG，默认级别为 WARNING
    format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename=logpath,
    filemode="a",
)
logger = logging.getLogger("my_logger")

# sys导出控制台的输出
sys.stdout = open("log.log", "w", encoding="utf-8")


class wm(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.combo_box_handler = work_inquiry(self)
        self.combo_box_handler2 = BillCalculate(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = wm()
    mainwindow.show()
    app.exec()

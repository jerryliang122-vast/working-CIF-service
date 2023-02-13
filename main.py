# 初始化
import os

# 检查工作目录下是否有conf文件夹
if not os.path.exists("conf"):
    # 没有的话直接重命名init_conf文件夹为conf
    os.rename("init_conf", "conf")

from PyQt6.QtWidgets import QApplication, QMainWindow
from Ui_untitled import Ui_Form
import sys
from work.inquiry import work_inquiry
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.FileHandler("conf/app.log"), logging.StreamHandler()],
    encoding="utf-8",
)
logger = logging.getLogger()


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

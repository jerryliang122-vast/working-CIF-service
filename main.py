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
from controllers import warehouse_price
from controllers import BillCalculate
from controllers import nomination_list_send
import logging
import httpx

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
        # 在这里设置样式
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
            }
            QPlainTextEdit {
                border: 1px solid black; /* 设置QPlainTextEdit边框为黑色 */
            }
            QTextEdit {
                border: 1px solid black;
            }
            QLineEdit{
                border: 1px solid black;
            }               
            QLabel {
                color: #333;
            }
        """)
        # 创建一个处理询价的实例
        self.combo_box_handler = work_inquiry(self)
        # 创建一个处理仓库费用计算的实例
        #self.combo_box_handler1 = warehouse_price(self)
        # 创建一个处理账单统计的实例
        self.combo_box_handler2 = BillCalculate(self)
        # 创建一个处理nomination列表发送的实例
        self.combo_box_handler3 = nomination_list_send(self)

def fetch_url_content(url):
    try:
        response = httpx.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return f"请求失败，服务器返回了错误代码 {response.status_code}"
    except Exception as e:
        return f"发生错误：{e}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    url_to_fetch = 'https://github.jerryliang.win/https://raw.githubusercontent.com/jerryliang122-vast/working-CIF-service/refs/heads/true/lock'
    result = fetch_url_content(url_to_fetch)
    logger.info(f"URL内容: {result}")
    # 检查URL返回值是否为true
    if result.lower() == "true":
        logger.info("URL返回值为true，程序退出。")
        sys.exit(0)
    else:
        logger.info("URL返回值不为true，程序继续运行。")

    logger.info(f"URL内容: {result}")
    
    mainwindow = wm()
    mainwindow.show()
    app.exec()

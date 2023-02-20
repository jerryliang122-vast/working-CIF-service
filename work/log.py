import logging
import os


class mylog:
    def __init__(self):
        self.logpath = os.path.join(os.getcwd(), "log.log")
        logging.basicConfig(
            level=logging.WARNING,  # 级别：CRITICAL > ERROR > WARNING > INFO > DEBUG，默认级别为 WARNING
            format="%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s:  %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            filename=self.logFile,
            filemode="a",
        )

    def write_logger(self, content):
        logging.debug(content)
        # 可以写其他的函数,使用其他级别的log

    def error_logger(self, content):
        logging.error(content)

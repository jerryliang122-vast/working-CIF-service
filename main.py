from PyQt6.QtWidgets import QApplication, QWidget
from Ui_untitled import Ui_Form
import sys


class wm(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mainwindow = wm()
    mainwindow.show()
    app.exec()

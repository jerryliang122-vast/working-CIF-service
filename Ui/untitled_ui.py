# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListView, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTabWidget, QTableView,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(900, 504)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(900, 504))
        Form.setMaximumSize(QSize(900, 504))
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font.setBold(True)
        font.setKerning(True)
        font.setStyleStrategy(QFont.NoAntialias)
        Form.setFont(font)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 901, 501))
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setBold(False)
        font1.setKerning(True)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.tabWidget.setFont(font1)
        self.tabWidget.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.tabWidget.setUsesScrollButtons(True)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 351, 171))
        self.groupBox.setFont(font1)
        self.address = QPlainTextEdit(self.groupBox)
        self.address.setObjectName(u"address")
        self.address.setGeometry(QRect(40, 20, 301, 41))
        self.address.setFont(font1)
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 31, 16))
        self.label.setFont(font1)
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 60, 83, 31))
        self.horizontalLayoutWidget.setFont(font1)
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 0, 0, 0)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.PKGS = QLineEdit(self.horizontalLayoutWidget)
        self.PKGS.setObjectName(u"PKGS")
        self.PKGS.setFont(font1)

        self.horizontalLayout.addWidget(self.PKGS)

        self.horizontalLayoutWidget_2 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(110, 60, 111, 31))
        self.horizontalLayoutWidget_2.setFont(font1)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 0, 5, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_3)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.KGS = QLineEdit(self.horizontalLayoutWidget_2)
        self.KGS.setObjectName(u"KGS")
        self.KGS.setEnabled(True)
        self.KGS.setFont(font1)

        self.horizontalLayout_2.addWidget(self.KGS)

        self.horizontalLayoutWidget_3 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(220, 60, 122, 31))
        self.horizontalLayoutWidget_3.setFont(font1)
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.CBM = QLineEdit(self.horizontalLayoutWidget_3)
        self.CBM.setObjectName(u"CBM")
        self.CBM.setFont(font1)

        self.horizontalLayout_3.addWidget(self.CBM)

        self.horizontalLayoutWidget_4 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(30, 90, 181, 31))
        self.horizontalLayoutWidget_4.setFont(font1)
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 5, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.size = QLineEdit(self.horizontalLayoutWidget_4)
        self.size.setObjectName(u"size")
        self.size.setEnabled(True)
        self.size.setFont(font1)

        self.horizontalLayout_4.addWidget(self.size)

        self.horizontalLayoutWidget_5 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(210, 90, 131, 31))
        self.horizontalLayoutWidget_5.setFont(font1)
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.HS = QLineEdit(self.horizontalLayoutWidget_5)
        self.HS.setObjectName(u"HS")
        self.HS.setFont(font1)

        self.horizontalLayout_5.addWidget(self.HS)

        self.horizontalLayoutWidget_6 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(30, 120, 151, 31))
        self.horizontalLayoutWidget_6.setFont(font1)
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.label_7)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.cargoname = QLineEdit(self.horizontalLayoutWidget_6)
        self.cargoname.setObjectName(u"cargoname")
        self.cargoname.setFont(font1)

        self.horizontalLayout_6.addWidget(self.cargoname)

        self.clause = QComboBox(self.groupBox)
        self.clause.addItem("")
        self.clause.addItem("")
        self.clause.addItem("")
        self.clause.setObjectName(u"clause")
        self.clause.setGeometry(QRect(290, 120, 51, 31))
        self.clause.setFont(font1)
        self.horizontalLayoutWidget_13 = QWidget(self.groupBox)
        self.horizontalLayoutWidget_13.setObjectName(u"horizontalLayoutWidget_13")
        self.horizontalLayoutWidget_13.setGeometry(QRect(180, 120, 111, 31))
        self.horizontalLayoutWidget_13.setFont(font1)
        self.horizontalLayout_13 = QHBoxLayout(self.horizontalLayoutWidget_13)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.horizontalLayoutWidget_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_13.addWidget(self.label_13)

        self.port = QLineEdit(self.horizontalLayoutWidget_13)
        self.port.setObjectName(u"port")
        self.port.setFont(font1)

        self.horizontalLayout_13.addWidget(self.port)

        self.groupBox_2 = QGroupBox(self.tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(350, 0, 251, 171))
        self.groupBox_2.setFont(font1)
        self.daili_list = QListView(self.groupBox_2)
        self.daili_list.setObjectName(u"daili_list")
        self.daili_list.setGeometry(QRect(0, 80, 251, 91))
        self.daili_list.setFont(font1)
        self.daili_list.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.daili_list.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.horizontalLayoutWidget_7 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(50, 50, 131, 31))
        self.horizontalLayoutWidget_7.setFont(font1)
        self.horizontalLayout_7 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.gangkou = QComboBox(self.horizontalLayoutWidget_7)
        self.gangkou.setObjectName(u"gangkou")
        self.gangkou.setFont(font1)

        self.horizontalLayout_7.addWidget(self.gangkou)

        self.horizontalLayoutWidget_8 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_8.setObjectName(u"horizontalLayoutWidget_8")
        self.horizontalLayoutWidget_8.setGeometry(QRect(0, 20, 121, 31))
        self.horizontalLayoutWidget_8.setFont(font1)
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget_8)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.hangxian = QComboBox(self.horizontalLayoutWidget_8)
        self.hangxian.setObjectName(u"hangxian")
        self.hangxian.setFont(font1)

        self.horizontalLayout_8.addWidget(self.hangxian)

        self.horizontalLayoutWidget_9 = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(120, 20, 131, 31))
        self.horizontalLayoutWidget_9.setFont(font1)
        self.horizontalLayout_9 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(6, 0, 0, 0)
        self.label_10 = QLabel(self.horizontalLayoutWidget_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_10)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.guojia = QComboBox(self.horizontalLayoutWidget_9)
        self.guojia.setObjectName(u"guojia")
        self.guojia.setFont(font1)

        self.horizontalLayout_9.addWidget(self.guojia)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(610, 0, 281, 171))
        self.groupBox_3.setFont(font1)
        self.horizontalLayoutWidget_10 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(50, 140, 191, 31))
        self.horizontalLayoutWidget_10.setFont(font1)
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.add_agent_email = QPushButton(self.horizontalLayoutWidget_10)
        self.add_agent_email.setObjectName(u"add_agent_email")
        self.add_agent_email.setFont(font1)

        self.horizontalLayout_10.addWidget(self.add_agent_email)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.delete_agent = QPushButton(self.horizontalLayoutWidget_10)
        self.delete_agent.setObjectName(u"delete_agent")
        self.delete_agent.setFont(font1)

        self.horizontalLayout_10.addWidget(self.delete_agent)

        self.agent_email_list = QPlainTextEdit(self.groupBox_3)
        self.agent_email_list.setObjectName(u"agent_email_list")
        self.agent_email_list.setGeometry(QRect(10, 50, 261, 91))
        self.agent_email_list.setFont(font1)
        self.horizontalLayoutWidget_11 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_11.setObjectName(u"horizontalLayoutWidget_11")
        self.horizontalLayoutWidget_11.setGeometry(QRect(40, 20, 201, 31))
        self.horizontalLayoutWidget_11.setFont(font1)
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget_11)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)

        self.agent_name = QLineEdit(self.horizontalLayoutWidget_11)
        self.agent_name.setObjectName(u"agent_name")
        self.agent_name.setFont(font1)

        self.horizontalLayout_11.addWidget(self.agent_name)

        self.groupBox_4 = QGroupBox(self.tab)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 170, 601, 301))
        self.groupBox_4.setFont(font1)
        self.emailtext = QTextEdit(self.groupBox_4)
        self.emailtext.setObjectName(u"emailtext")
        self.emailtext.setGeometry(QRect(10, 20, 341, 271))
        self.emailtext.setFont(font1)
        self.groupBox_7 = QGroupBox(self.groupBox_4)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setGeometry(QRect(359, 10, 231, 131))
        self.groupBox_7.setFont(font1)
        self.aiimport = QPlainTextEdit(self.groupBox_7)
        self.aiimport.setObjectName(u"aiimport")
        self.aiimport.setGeometry(QRect(10, 20, 211, 51))
        self.aiimport.setFont(font1)
        self.horizontalLayoutWidget_15 = QWidget(self.groupBox_7)
        self.horizontalLayoutWidget_15.setObjectName(u"horizontalLayoutWidget_15")
        self.horizontalLayoutWidget_15.setGeometry(QRect(10, 80, 211, 41))
        self.horizontalLayoutWidget_15.setFont(font1)
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.auto_identification = QPushButton(self.horizontalLayoutWidget_15)
        self.auto_identification.setObjectName(u"auto_identification")
        self.auto_identification.setFont(font1)

        self.horizontalLayout_18.addWidget(self.auto_identification)

        self.auto_paste = QPushButton(self.horizontalLayoutWidget_15)
        self.auto_paste.setObjectName(u"auto_paste")
        self.auto_paste.setMaximumSize(QSize(16777215, 16777215))
        self.auto_paste.setFont(font1)

        self.horizontalLayout_18.addWidget(self.auto_paste)

        self.auto_clean = QPushButton(self.horizontalLayoutWidget_15)
        self.auto_clean.setObjectName(u"auto_clean")
        self.auto_clean.setFont(font1)

        self.horizontalLayout_18.addWidget(self.auto_clean)

        self.groupBox_8 = QGroupBox(self.groupBox_4)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setGeometry(QRect(360, 139, 231, 151))
        self.groupBox_8.setFont(font1)
        self.aioutput = QTextEdit(self.groupBox_8)
        self.aioutput.setObjectName(u"aioutput")
        self.aioutput.setGeometry(QRect(10, 20, 211, 121))
        self.aioutput.setFont(font1)
        self.groupBox_5 = QGroupBox(self.tab)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(610, 170, 281, 211))
        self.groupBox_5.setFont(font1)
        self.Preview_email = QPushButton(self.groupBox_5)
        self.Preview_email.setObjectName(u"Preview_email")
        self.Preview_email.setGeometry(QRect(30, 180, 75, 24))
        self.Preview_email.setFont(font1)
        self.horizontalLayoutWidget_12 = QWidget(self.groupBox_5)
        self.horizontalLayoutWidget_12.setObjectName(u"horizontalLayoutWidget_12")
        self.horizontalLayoutWidget_12.setGeometry(QRect(50, 20, 191, 31))
        self.horizontalLayoutWidget_12.setFont(font1)
        self.horizontalLayout_12 = QHBoxLayout(self.horizontalLayoutWidget_12)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.horizontalLayoutWidget_12)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_12)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)

        self.inquiry_number = QLineEdit(self.horizontalLayoutWidget_12)
        self.inquiry_number.setObjectName(u"inquiry_number")
        self.inquiry_number.setFont(font1)

        self.horizontalLayout_12.addWidget(self.inquiry_number)

        self.send_email = QPushButton(self.groupBox_5)
        self.send_email.setObjectName(u"send_email")
        self.send_email.setGeometry(QRect(110, 180, 75, 24))
        self.send_email.setFont(font1)
        self.delete_data = QPushButton(self.groupBox_5)
        self.delete_data.setObjectName(u"delete_data")
        self.delete_data.setGeometry(QRect(190, 180, 75, 24))
        self.delete_data.setFont(font1)
        self.addresslist = QTableView(self.groupBox_5)
        self.addresslist.setObjectName(u"addresslist")
        self.addresslist.setGeometry(QRect(20, 50, 251, 121))
        self.addresslist.setFont(font1)
        self.groupBox_6 = QGroupBox(self.tab)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setGeometry(QRect(610, 380, 281, 91))
        self.groupBox_6.setFont(font1)
        self.aoto = QPushButton(self.groupBox_6)
        self.aoto.setObjectName(u"aoto")
        self.aoto.setGeometry(QRect(214, 13, 61, 61))
        self.aoto.setFont(font1)
        self.random_number = QPlainTextEdit(self.groupBox_6)
        self.random_number.setObjectName(u"random_number")
        self.random_number.setGeometry(QRect(20, 20, 191, 51))
        self.random_number.setFont(font1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.groupBox_9 = QGroupBox(self.tab_4)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setGeometry(QRect(0, 0, 461, 221))
        self.label_18 = QLabel(self.groupBox_9)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(10, 20, 341, 16))
        self.groupBox_10 = QGroupBox(self.groupBox_9)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setGeometry(QRect(10, 80, 161, 131))
        self.verticalLayoutWidget = QWidget(self.groupBox_10)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 20, 160, 111))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_20 = QLabel(self.verticalLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_20.addWidget(self.label_20)

        self.cfs_yg_pkgs_charge = QLineEdit(self.verticalLayoutWidget)
        self.cfs_yg_pkgs_charge.setObjectName(u"cfs_yg_pkgs_charge")

        self.horizontalLayout_20.addWidget(self.cfs_yg_pkgs_charge)


        self.verticalLayout.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_21 = QLabel(self.verticalLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_21.addWidget(self.label_21)

        self.cfs_yg_weight_charge = QLineEdit(self.verticalLayoutWidget)
        self.cfs_yg_weight_charge.setObjectName(u"cfs_yg_weight_charge")

        self.horizontalLayout_21.addWidget(self.cfs_yg_weight_charge)


        self.verticalLayout.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.verticalLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_22.addWidget(self.label_22)

        self.cfs_yg_cmb_charge = QLineEdit(self.verticalLayoutWidget)
        self.cfs_yg_cmb_charge.setObjectName(u"cfs_yg_cmb_charge")

        self.horizontalLayout_22.addWidget(self.cfs_yg_cmb_charge)


        self.verticalLayout.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_23 = QLabel(self.verticalLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_23.addWidget(self.label_23)

        self.cfs_yg_mini_charge = QLineEdit(self.verticalLayoutWidget)
        self.cfs_yg_mini_charge.setObjectName(u"cfs_yg_mini_charge")

        self.horizontalLayout_23.addWidget(self.cfs_yg_mini_charge)


        self.verticalLayout.addLayout(self.horizontalLayout_23)

        self.groupBox_11 = QGroupBox(self.groupBox_9)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setGeometry(QRect(170, 80, 161, 131))
        self.verticalLayoutWidget_2 = QWidget(self.groupBox_11)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(0, 20, 160, 111))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_24 = QLabel(self.verticalLayoutWidget_2)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_24.addWidget(self.label_24)

        self.cfs_ys_pkgs_charge = QLineEdit(self.verticalLayoutWidget_2)
        self.cfs_ys_pkgs_charge.setObjectName(u"cfs_ys_pkgs_charge")

        self.horizontalLayout_24.addWidget(self.cfs_ys_pkgs_charge)


        self.verticalLayout_2.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_25 = QLabel(self.verticalLayoutWidget_2)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_25.addWidget(self.label_25)

        self.cfs_ys_weight_charge = QLineEdit(self.verticalLayoutWidget_2)
        self.cfs_ys_weight_charge.setObjectName(u"cfs_ys_weight_charge")

        self.horizontalLayout_25.addWidget(self.cfs_ys_weight_charge)


        self.verticalLayout_2.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_26 = QLabel(self.verticalLayoutWidget_2)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_26.addWidget(self.label_26)

        self.cfs_ys_cbm_charge = QLineEdit(self.verticalLayoutWidget_2)
        self.cfs_ys_cbm_charge.setObjectName(u"cfs_ys_cbm_charge")

        self.horizontalLayout_26.addWidget(self.cfs_ys_cbm_charge)


        self.verticalLayout_2.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_27 = QLabel(self.verticalLayoutWidget_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_27.addWidget(self.label_27)

        self.cfs_ys_mini_charge = QLineEdit(self.verticalLayoutWidget_2)
        self.cfs_ys_mini_charge.setObjectName(u"cfs_ys_mini_charge")

        self.horizontalLayout_27.addWidget(self.cfs_ys_mini_charge)


        self.verticalLayout_2.addLayout(self.horizontalLayout_27)

        self.horizontalLayoutWidget_22 = QWidget(self.groupBox_9)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(10, 40, 321, 41))
        self.horizontalLayout_31 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_19 = QLabel(self.horizontalLayoutWidget_22)
        self.label_19.setObjectName(u"label_19")

        self.horizontalLayout_19.addWidget(self.label_19)

        self.cfs_name = QLineEdit(self.horizontalLayoutWidget_22)
        self.cfs_name.setObjectName(u"cfs_name")

        self.horizontalLayout_19.addWidget(self.cfs_name)


        self.horizontalLayout_31.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_28 = QLabel(self.horizontalLayoutWidget_22)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_28.addWidget(self.label_28)

        self.cfs_bl_charge = QLineEdit(self.horizontalLayoutWidget_22)
        self.cfs_bl_charge.setObjectName(u"cfs_bl_charge")

        self.horizontalLayout_28.addWidget(self.cfs_bl_charge)


        self.horizontalLayout_31.addLayout(self.horizontalLayout_28)

        self.verticalLayoutWidget_3 = QWidget(self.groupBox_9)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(340, 140, 121, 61))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.wright_yaml = QPushButton(self.verticalLayoutWidget_3)
        self.wright_yaml.setObjectName(u"wright_yaml")

        self.verticalLayout_3.addWidget(self.wright_yaml)

        self.clean_cfs_charge = QPushButton(self.verticalLayoutWidget_3)
        self.clean_cfs_charge.setObjectName(u"clean_cfs_charge")

        self.verticalLayout_3.addWidget(self.clean_cfs_charge)

        self.verticalLayoutWidget_5 = QWidget(self.groupBox_9)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(340, 40, 121, 91))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_29 = QLabel(self.verticalLayoutWidget_5)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_29.addWidget(self.label_29)

        self.cfs_van_charge = QLineEdit(self.verticalLayoutWidget_5)
        self.cfs_van_charge.setObjectName(u"cfs_van_charge")

        self.horizontalLayout_29.addWidget(self.cfs_van_charge)


        self.verticalLayout_5.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_30 = QLabel(self.verticalLayoutWidget_5)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_30.addWidget(self.label_30)

        self.cfs_ows_charge = QLineEdit(self.verticalLayoutWidget_5)
        self.cfs_ows_charge.setObjectName(u"cfs_ows_charge")

        self.horizontalLayout_30.addWidget(self.cfs_ows_charge)


        self.verticalLayout_5.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_33 = QLabel(self.verticalLayoutWidget_5)
        self.label_33.setObjectName(u"label_33")

        self.horizontalLayout_34.addWidget(self.label_33)

        self.cfs_Insurance_charge = QLineEdit(self.verticalLayoutWidget_5)
        self.cfs_Insurance_charge.setObjectName(u"cfs_Insurance_charge")

        self.horizontalLayout_34.addWidget(self.cfs_Insurance_charge)


        self.verticalLayout_5.addLayout(self.horizontalLayout_34)

        self.groupBox_12 = QGroupBox(self.tab_4)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setGeometry(QRect(470, 0, 421, 211))
        self.stander_list = QListView(self.groupBox_12)
        self.stander_list.setObjectName(u"stander_list")
        self.stander_list.setGeometry(QRect(0, 20, 311, 181))
        self.pushButton_4 = QPushButton(self.groupBox_12)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(320, 70, 75, 23))
        self.pushButton_5 = QPushButton(self.groupBox_12)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(320, 140, 75, 23))
        self.groupBox_13 = QGroupBox(self.tab_4)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setGeometry(QRect(0, 220, 461, 251))
        self.cfs_price_output = QTextEdit(self.groupBox_13)
        self.cfs_price_output.setObjectName(u"cfs_price_output")
        self.cfs_price_output.setGeometry(QRect(10, 20, 441, 231))
        self.groupBox_14 = QGroupBox(self.tab_4)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.groupBox_14.setGeometry(QRect(470, 210, 421, 261))
        self.verticalLayoutWidget_4 = QWidget(self.groupBox_14)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(20, 10, 141, 131))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_31 = QLabel(self.verticalLayoutWidget_4)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_32.addWidget(self.label_31)

        self.chose_cfs_name = QComboBox(self.verticalLayoutWidget_4)
        self.chose_cfs_name.addItem("")
        self.chose_cfs_name.addItem("")
        self.chose_cfs_name.setObjectName(u"chose_cfs_name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(3)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chose_cfs_name.sizePolicy().hasHeightForWidth())
        self.chose_cfs_name.setSizePolicy(sizePolicy1)

        self.horizontalLayout_32.addWidget(self.chose_cfs_name)


        self.verticalLayout_4.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_40 = QLabel(self.verticalLayoutWidget_4)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_42.addWidget(self.label_40)

        self.cfs_inout_chose = QComboBox(self.verticalLayoutWidget_4)
        self.cfs_inout_chose.addItem("")
        self.cfs_inout_chose.addItem("")
        self.cfs_inout_chose.setObjectName(u"cfs_inout_chose")

        self.horizontalLayout_42.addWidget(self.cfs_inout_chose)


        self.verticalLayout_4.addLayout(self.horizontalLayout_42)

        self.cfs_pallets = QCheckBox(self.verticalLayoutWidget_4)
        self.cfs_pallets.setObjectName(u"cfs_pallets")

        self.verticalLayout_4.addWidget(self.cfs_pallets)

        self.cfs_night_in = QCheckBox(self.verticalLayoutWidget_4)
        self.cfs_night_in.setObjectName(u"cfs_night_in")

        self.verticalLayout_4.addWidget(self.cfs_night_in)

        self.cfs_van = QCheckBox(self.verticalLayoutWidget_4)
        self.cfs_van.setObjectName(u"cfs_van")

        self.verticalLayout_4.addWidget(self.cfs_van)

        self.verticalLayoutWidget_6 = QWidget(self.groupBox_14)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(160, 10, 175, 202))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_32 = QLabel(self.verticalLayoutWidget_6)
        self.label_32.setObjectName(u"label_32")

        self.horizontalLayout_33.addWidget(self.label_32)

        self.cfs_number = QLineEdit(self.verticalLayoutWidget_6)
        self.cfs_number.setObjectName(u"cfs_number")

        self.horizontalLayout_33.addWidget(self.cfs_number)


        self.verticalLayout_6.addLayout(self.horizontalLayout_33)

        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_34 = QLabel(self.verticalLayoutWidget_6)
        self.label_34.setObjectName(u"label_34")

        self.horizontalLayout_35.addWidget(self.label_34)

        self.cfs_discount_price = QLineEdit(self.verticalLayoutWidget_6)
        self.cfs_discount_price.setObjectName(u"cfs_discount_price")

        self.horizontalLayout_35.addWidget(self.cfs_discount_price)


        self.verticalLayout_6.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_35 = QLabel(self.verticalLayoutWidget_6)
        self.label_35.setObjectName(u"label_35")

        self.horizontalLayout_36.addWidget(self.label_35)

        self.where_cfs_discount = QComboBox(self.verticalLayoutWidget_6)
        self.where_cfs_discount.addItem("")
        self.where_cfs_discount.addItem("")
        self.where_cfs_discount.setObjectName(u"where_cfs_discount")

        self.horizontalLayout_36.addWidget(self.where_cfs_discount)


        self.verticalLayout_6.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.cfs_discount = QCheckBox(self.verticalLayoutWidget_6)
        self.cfs_discount.setObjectName(u"cfs_discount")
        self.cfs_discount.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cfs_discount.sizePolicy().hasHeightForWidth())
        self.cfs_discount.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"Adobe Arabic"])
        font2.setBold(False)
        font2.setKerning(True)
        font2.setStyleStrategy(QFont.NoAntialias)
        self.cfs_discount.setFont(font2)
        self.cfs_discount.setAcceptDrops(False)
        self.cfs_discount.setLayoutDirection(Qt.LeftToRight)
        self.cfs_discount.setAutoFillBackground(False)
        self.cfs_discount.setCheckable(True)
        self.cfs_discount.setChecked(False)
        self.cfs_discount.setAutoRepeat(False)
        self.cfs_discount.setTristate(False)

        self.horizontalLayout_37.addWidget(self.cfs_discount)


        self.verticalLayout_6.addLayout(self.horizontalLayout_37)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.use_cfs_numebr_calculate = QPushButton(self.verticalLayoutWidget_6)
        self.use_cfs_numebr_calculate.setObjectName(u"use_cfs_numebr_calculate")

        self.verticalLayout_8.addWidget(self.use_cfs_numebr_calculate)

        self.use_cargo_info_calculate = QPushButton(self.verticalLayoutWidget_6)
        self.use_cargo_info_calculate.setObjectName(u"use_cargo_info_calculate")

        self.verticalLayout_8.addWidget(self.use_cargo_info_calculate)


        self.verticalLayout_6.addLayout(self.verticalLayout_8)

        self.layoutWidget = QWidget(self.groupBox_14)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 140, 141, 120))
        self.verticalLayout_7 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_36 = QLabel(self.layoutWidget)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_38.addWidget(self.label_36)

        self.cfs_pkgs = QLineEdit(self.layoutWidget)
        self.cfs_pkgs.setObjectName(u"cfs_pkgs")

        self.horizontalLayout_38.addWidget(self.cfs_pkgs)


        self.verticalLayout_7.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_37 = QLabel(self.layoutWidget)
        self.label_37.setObjectName(u"label_37")

        self.horizontalLayout_39.addWidget(self.label_37)

        self.cfs_tone = QLineEdit(self.layoutWidget)
        self.cfs_tone.setObjectName(u"cfs_tone")

        self.horizontalLayout_39.addWidget(self.cfs_tone)


        self.verticalLayout_7.addLayout(self.horizontalLayout_39)

        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_38 = QLabel(self.layoutWidget)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_40.addWidget(self.label_38)

        self.cfs_cbm = QLineEdit(self.layoutWidget)
        self.cfs_cbm.setObjectName(u"cfs_cbm")

        self.horizontalLayout_40.addWidget(self.cfs_cbm)


        self.verticalLayout_7.addLayout(self.horizontalLayout_40)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_39 = QLabel(self.layoutWidget)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_41.addWidget(self.label_39)

        self.cargo_dims = QLineEdit(self.layoutWidget)
        self.cargo_dims.setObjectName(u"cargo_dims")

        self.horizontalLayout_41.addWidget(self.cargo_dims)


        self.verticalLayout_7.addLayout(self.horizontalLayout_41)

        self.tabWidget.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.groupBox_20 = QGroupBox(self.tab_6)
        self.groupBox_20.setObjectName(u"groupBox_20")
        self.groupBox_20.setGeometry(QRect(0, 0, 271, 211))
        self.horizontalLayoutWidget_21 = QWidget(self.groupBox_20)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(10, 20, 241, 31))
        self.horizontalLayout_47 = QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_43 = QLabel(self.horizontalLayoutWidget_21)
        self.label_43.setObjectName(u"label_43")

        self.horizontalLayout_44.addWidget(self.label_43)

        self.nom_line = QComboBox(self.horizontalLayoutWidget_21)
        self.nom_line.setObjectName(u"nom_line")

        self.horizontalLayout_44.addWidget(self.nom_line)


        self.horizontalLayout_47.addLayout(self.horizontalLayout_44)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_18)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_44 = QLabel(self.horizontalLayoutWidget_21)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_45.addWidget(self.label_44)

        self.nom_countries = QComboBox(self.horizontalLayoutWidget_21)
        self.nom_countries.setObjectName(u"nom_countries")

        self.horizontalLayout_45.addWidget(self.nom_countries)


        self.horizontalLayout_47.addLayout(self.horizontalLayout_45)

        self.horizontalLayoutWidget_20 = QWidget(self.groupBox_20)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(80, 50, 111, 27))
        self.horizontalLayout_46 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.horizontalLayoutWidget_20)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_46.addWidget(self.label_45)

        self.nom_port = QComboBox(self.horizontalLayoutWidget_20)
        self.nom_port.setObjectName(u"nom_port")

        self.horizontalLayout_46.addWidget(self.nom_port)

        self.nom_port_list = QListView(self.groupBox_20)
        self.nom_port_list.setObjectName(u"nom_port_list")
        self.nom_port_list.setGeometry(QRect(0, 80, 261, 111))
        self.groupBox_19 = QGroupBox(self.tab_6)
        self.groupBox_19.setObjectName(u"groupBox_19")
        self.groupBox_19.setGeometry(QRect(270, 0, 271, 211))
        self.horizontalLayoutWidget_23 = QWidget(self.groupBox_19)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(10, 20, 251, 41))
        self.horizontalLayout_48 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.horizontalLayoutWidget_23)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_48.addWidget(self.label_46)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_48.addItem(self.horizontalSpacer_19)

        self.nom_agent_name = QLineEdit(self.horizontalLayoutWidget_23)
        self.nom_agent_name.setObjectName(u"nom_agent_name")

        self.horizontalLayout_48.addWidget(self.nom_agent_name)

        self.nom_agent_email_list = QPlainTextEdit(self.groupBox_19)
        self.nom_agent_email_list.setObjectName(u"nom_agent_email_list")
        self.nom_agent_email_list.setGeometry(QRect(20, 60, 231, 101))
        self.horizontalLayoutWidget_24 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(300, 160, 211, 41))
        self.horizontalLayout_49 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.nom_agent_add = QPushButton(self.horizontalLayoutWidget_24)
        self.nom_agent_add.setObjectName(u"nom_agent_add")

        self.horizontalLayout_49.addWidget(self.nom_agent_add)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_20)

        self.nom_agent_delete = QPushButton(self.horizontalLayoutWidget_24)
        self.nom_agent_delete.setObjectName(u"nom_agent_delete")

        self.horizontalLayout_49.addWidget(self.nom_agent_delete)

        self.groupBox_21 = QGroupBox(self.tab_6)
        self.groupBox_21.setObjectName(u"groupBox_21")
        self.groupBox_21.setGeometry(QRect(540, 0, 351, 471))
        self.nom_file_list_update = QPushButton(self.groupBox_21)
        self.nom_file_list_update.setObjectName(u"nom_file_list_update")
        self.nom_file_list_update.setGeometry(QRect(50, 170, 251, 23))
        self.horizontalLayoutWidget_25 = QWidget(self.groupBox_21)
        self.horizontalLayoutWidget_25.setObjectName(u"horizontalLayoutWidget_25")
        self.horizontalLayoutWidget_25.setGeometry(QRect(30, 200, 281, 31))
        self.horizontalLayout_50 = QHBoxLayout(self.horizontalLayoutWidget_25)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.horizontalLayoutWidget_25)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_50.addWidget(self.label_47)

        self.nom_email_subject = QLineEdit(self.horizontalLayoutWidget_25)
        self.nom_email_subject.setObjectName(u"nom_email_subject")

        self.horizontalLayout_50.addWidget(self.nom_email_subject)

        self.groupBox_22 = QGroupBox(self.groupBox_21)
        self.groupBox_22.setObjectName(u"groupBox_22")
        self.groupBox_22.setGeometry(QRect(20, 230, 301, 141))
        self.nom_email_list = QTableView(self.groupBox_22)
        self.nom_email_list.setObjectName(u"nom_email_list")
        self.nom_email_list.setGeometry(QRect(10, 20, 281, 111))
        self.nom_email_send = QPushButton(self.groupBox_21)
        self.nom_email_send.setObjectName(u"nom_email_send")
        self.nom_email_send.setGeometry(QRect(40, 390, 101, 23))
        self.nom_clean_screen = QPushButton(self.groupBox_21)
        self.nom_clean_screen.setObjectName(u"nom_clean_screen")
        self.nom_clean_screen.setGeometry(QRect(214, 390, 91, 23))
        self.nom_file_list = QTableView(self.groupBox_21)
        self.nom_file_list.setObjectName(u"nom_file_list")
        self.nom_file_list.setGeometry(QRect(10, 20, 331, 151))
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.groupBox_15 = QGroupBox(self.tab_5)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.groupBox_15.setGeometry(QRect(10, 0, 421, 211))
        self.bill_number = QPlainTextEdit(self.groupBox_15)
        self.bill_number.setObjectName(u"bill_number")
        self.bill_number.setGeometry(QRect(10, 20, 401, 181))
        self.groupBox_16 = QGroupBox(self.tab_5)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.groupBox_16.setGeometry(QRect(440, 0, 441, 211))
        self.horizontalLayoutWidget_16 = QWidget(self.groupBox_16)
        self.horizontalLayoutWidget_16.setObjectName(u"horizontalLayoutWidget_16")
        self.horizontalLayoutWidget_16.setGeometry(QRect(10, 20, 159, 51))
        self.horizontalLayout_43 = QHBoxLayout(self.horizontalLayoutWidget_16)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.horizontalLayoutWidget_16)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_43.addWidget(self.label_41)

        self.bill_split = QLineEdit(self.horizontalLayoutWidget_16)
        self.bill_split.setObjectName(u"bill_split")

        self.horizontalLayout_43.addWidget(self.bill_split)

        self.label_42 = QLabel(self.groupBox_16)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(10, 70, 158, 31))
        self.bill_splitout = QPlainTextEdit(self.groupBox_16)
        self.bill_splitout.setObjectName(u"bill_splitout")
        self.bill_splitout.setGeometry(QRect(10, 100, 161, 101))
        self.bill_output = QPushButton(self.groupBox_16)
        self.bill_output.setObjectName(u"bill_output")
        self.bill_output.setGeometry(QRect(180, 100, 75, 23))
        self.bill_clean = QPushButton(self.groupBox_16)
        self.bill_clean.setObjectName(u"bill_clean")
        self.bill_clean.setGeometry(QRect(180, 170, 75, 23))
        self.groupBox_17 = QGroupBox(self.tab_5)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.groupBox_17.setGeometry(QRect(10, 210, 421, 251))
        self.bill_out = QPlainTextEdit(self.groupBox_17)
        self.bill_out.setObjectName(u"bill_out")
        self.bill_out.setGeometry(QRect(10, 20, 401, 221))
        self.groupBox_18 = QGroupBox(self.tab_5)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.groupBox_18.setGeometry(QRect(440, 210, 441, 251))
        self.bill_out2 = QPlainTextEdit(self.groupBox_18)
        self.bill_out2.setObjectName(u"bill_out2")
        self.bill_out2.setGeometry(QRect(10, 20, 421, 221))
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayoutWidget_14 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_14.setObjectName(u"horizontalLayoutWidget_14")
        self.horizontalLayoutWidget_14.setGeometry(QRect(10, 10, 401, 41))
        self.horizontalLayout_14 = QHBoxLayout(self.horizontalLayoutWidget_14)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_14 = QLabel(self.horizontalLayoutWidget_14)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_15.addWidget(self.label_14)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_14)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget_14)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_15.addWidget(self.lineEdit)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_15 = QLabel(self.horizontalLayoutWidget_14)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_16.addWidget(self.label_15)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_15)

        self.lineEdit_2 = QLineEdit(self.horizontalLayoutWidget_14)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_16.addWidget(self.lineEdit_2)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_16)

        self.horizontalLayoutWidget_17 = QWidget(self.tab_2)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(10, 50, 167, 41))
        self.horizontalLayout_17 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label_16 = QLabel(self.horizontalLayoutWidget_17)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_17.addWidget(self.label_16)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)

        self.label_17 = QLabel(self.horizontalLayoutWidget_17)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_17.addWidget(self.label_17)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_16)

        self.pushButton = QPushButton(self.horizontalLayoutWidget_17)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_17.addWidget(self.pushButton)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u8be2\u4ef7\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u5730\u5740", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u91cd\u91cfKG", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4f53\u79efCBM", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u8d27\u7269\u5355\u4ef6\u4f53\u79ef", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"HS\u7f16\u7801", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8d27\u7269\u63cf\u8ff0", None))
        self.clause.setItemText(0, QCoreApplication.translate("Form", u"DAP", None))
        self.clause.setItemText(1, QCoreApplication.translate("Form", u"DDU", None))
        self.clause.setItemText(2, QCoreApplication.translate("Form", u"DDP", None))

        self.label_13.setText(QCoreApplication.translate("Form", u"\u6e2f\u53e3", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u9009\u62e9\u4ee3\u7406", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6e2f\u53e3", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u822a\u7ebf", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u4ee3\u7406\u4fe1\u606f", None))
        self.add_agent_email.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.delete_agent.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u4ee3\u7406\u540d\u79f0", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b\u4ee5\u53ca\u6e32\u67d3\u754c\u9762", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b\u8f93\u5165\u6846", None))
        self.auto_identification.setText(QCoreApplication.translate("Form", u"\u8bc6\u522b", None))
        self.auto_paste.setText(QCoreApplication.translate("Form", u"\u7c98\u8d34", None))
        self.auto_clean.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"\u81ea\u52a8\u8bc6\u522b\u8f93\u51fa\u6846", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"\u53d1\u9001\u90ae\u4ef6", None))
        self.Preview_email.setText(QCoreApplication.translate("Form", u"\u9884\u89c8", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u8be2\u4ef7\u7f16\u53f7", None))
        self.send_email.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.delete_data.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"\u7f16\u53f7\u52a0\u8f7d", None))
        self.aoto.setText(QCoreApplication.translate("Form", u"\u751f\u6210", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"\u8be2\u4ef7", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"\u4ed3\u5e93\u8d39\u7528\u6807\u51c6\u767b\u8bb0", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u767b\u8bb0\u7684\u4ed3\u5e93\u8d39\u7528\u6807\u51c6\u5c06\u4f1a\u5b58\u50a8\u5728conf\u6587\u4ef6\u5939\u4e2d,\u540e\u7eed\u53ef\u4ee5\u76f4\u63a5\u8c03\u7528", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"\u4e0a\u4e0b\u8f66\u8d39-\u5355\u4ef7-\u5916\u6e2f", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u6258\u76d8", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u91cd\u91cf", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u4f53\u79ef-\u7acb\u65b9", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u6700\u4f4e\u6536\u8d39\u6807\u51c6", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"\u4e0a\u4e0b\u8f66\u8d39-\u5355\u4ef7-\u6d0b\u5c71", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u6258\u76d8", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u91cd\u91cf", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"\u4f53\u79ef-\u7acb\u65b9", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"\u6700\u4f4e\u6536\u8d39\u6807\u51c6", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u767b\u8bb0\u540d\u79f0", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"BL\u8d39\u7528\u603b\u4ef7", None))
        self.wright_yaml.setText(QCoreApplication.translate("Form", u"\u5199\u5165", None))
        self.clean_cfs_charge.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"\u53a2\u5f0f\u8f66", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"\u8d85\u5927\u8d39", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u4fdd\u9669\u8d39", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Form", u"\u6807\u51c6\u5217\u8868", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"\u8bfb\u53d6", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"\u63a7\u5236\u53f0", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u4ed3\u5e93\u540d\u79f0", None))
        self.chose_cfs_name.setItemText(0, QCoreApplication.translate("Form", u"\u5916\u6e2f\u4ed3\u5e93", None))
        self.chose_cfs_name.setItemText(1, QCoreApplication.translate("Form", u"\u6d0b\u5c71\u4ed3\u5e93", None))

        self.label_40.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e0b\u8f66\u8d39\u9009\u62e9", None))
        self.cfs_inout_chose.setItemText(0, QCoreApplication.translate("Form", u"\u5916\u6e2f", None))
        self.cfs_inout_chose.setItemText(1, QCoreApplication.translate("Form", u"\u6d0b\u5c71", None))

        self.cfs_pallets.setText(QCoreApplication.translate("Form", u"\u6258\u76d8\u8d27", None))
        self.cfs_night_in.setText(QCoreApplication.translate("Form", u"\u591c\u95f4\u8fdb\u4ed3", None))
        self.cfs_van.setText(QCoreApplication.translate("Form", u"\u53a2\u5f0f\u8f66", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u8fdb\u4ed3\u7f16\u53f7", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\u6253\u6298\u8d39\u7387", None))
        self.cfs_discount_price.setText(QCoreApplication.translate("Form", u"0.8", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u5728\u54ea\u4e2a\u5730\u65b9\u6253\u6298", None))
        self.where_cfs_discount.setItemText(0, QCoreApplication.translate("Form", u"\u4e0a\u4e0b\u8f66\u8d39", None))
        self.where_cfs_discount.setItemText(1, QCoreApplication.translate("Form", u"\u603b\u8d39\u7528", None))

        self.cfs_discount.setText(QCoreApplication.translate("Form", u"\u662f\u5426\u6253\u6298", None))
        self.use_cfs_numebr_calculate.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u8fdb\u4ed3\u7f16\u53f7\u8ba1\u7b97", None))
        self.use_cargo_info_calculate.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u8d27\u7269\u4fe1\u606f\u8ba1\u7b97", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"\u4ef6\u6570", None))
        self.label_37.setText(QCoreApplication.translate("Form", u"\u91cd\u91cfKG", None))
        self.label_38.setText(QCoreApplication.translate("Form", u"\u4f53\u79ef", None))
        self.label_39.setText(QCoreApplication.translate("Form", u"\u5c3a\u5bf8\u53ef\u7a7a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"\u4ed3\u5e93\u8d39\u7528\u8ba1\u7b97", None))
        self.groupBox_20.setTitle(QCoreApplication.translate("Form", u"\u9009\u62e9\u4ee3\u7406", None))
        self.label_43.setText(QCoreApplication.translate("Form", u"\u822a\u7ebf", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"\u56fd\u5bb6", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"\u6e2f\u53e3", None))
        self.groupBox_19.setTitle(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u4ee3\u7406", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"\u4ee3\u7406\u540d\u79f0", None))
        self.nom_agent_add.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0", None))
        self.nom_agent_delete.setText(QCoreApplication.translate("Form", u"\u5220\u9664", None))
        self.groupBox_21.setTitle(QCoreApplication.translate("Form", u"\u6587\u4ef6\u5217\u8868\u9009\u62e9\u4ee5\u53ca\u4e3b\u9898\u8bbe\u7f6e", None))
        self.nom_file_list_update.setText(QCoreApplication.translate("Form", u"\u5237\u65b0", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"\u90ae\u4ef6\u4e3b\u9898", None))
        self.nom_email_subject.setText(QCoreApplication.translate("Form", u"The list of nomination goods//", None))
        self.groupBox_22.setTitle(QCoreApplication.translate("Form", u"\u90ae\u4ef6\u5730\u5740", None))
        self.nom_email_send.setText(QCoreApplication.translate("Form", u"\u53d1\u9001", None))
        self.nom_clean_screen.setText(QCoreApplication.translate("Form", u"\u6e05\u5c4f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"\u53d1\u9001nomination list", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Form", u"\u8f93\u5165\u7f16\u53f7", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"\u63a7\u5236\u9762\u677f", None))
        self.label_41.setText(QCoreApplication.translate("Form", u"\u8f93\u5165\u7f16\u53f7\u5206\u9694\u7b26", None))
        self.bill_split.setText(QCoreApplication.translate("Form", u",", None))
        self.label_42.setText(QCoreApplication.translate("Form", u"\u9700\u8981\u5254\u9664\u7684\u7f16\u53f7\u7528\u82f1\u6587,\u5206\u9694", None))
        self.bill_splitout.setPlainText(QCoreApplication.translate("Form", u"-(\\d+)|\\*(HB|MB|H\\d+)", None))
        self.bill_output.setText(QCoreApplication.translate("Form", u"\u8f93\u51fa", None))
        self.bill_clean.setText(QCoreApplication.translate("Form", u"\u6e05\u9664", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Form", u"\u8f93\u51fa\u7f16\u53f7\u7ed3\u679c", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Form", u"\u7f16\u53f7\u7edf\u8ba1\u7ed3\u679c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"\u8d26\u5355\u7edf\u8ba1", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"\u4e1a\u52a1\u7f16\u53f7", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"\u63d0\u5355\u53f7", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"AI\u72b6\u6001", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u79bb\u7ebf", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u68c0\u67e5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"\u9884\u4ed8\u8d27\u603b\u7ed3", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
    # retranslateUi


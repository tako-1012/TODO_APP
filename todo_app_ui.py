# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todo_app.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QDateTimeEdit, QFrame, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSlider, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 650)
        MainWindow.setMaximumSize(QSize(800, 650))
        MainWindow.setTabletTracking(False)
        MainWindow.setIconSize(QSize(10, 24))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(260, 20, 261, 31))
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignCenter)
        self.task_input = QLineEdit(self.centralwidget)
        self.task_input.setObjectName(u"task_input")
        self.task_input.setGeometry(QRect(260, 60, 201, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.task_input.setFont(font1)
        self.task_input.setClearButtonEnabled(False)
        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(470, 60, 51, 71))
        self.task_deadline = QDateTimeEdit(self.centralwidget)
        self.task_deadline.setObjectName(u"task_deadline")
        self.task_deadline.setGeometry(QRect(260, 90, 201, 22))
        self.task_deadline.setWrapping(False)
        self.task_deadline.setFrame(True)
        self.task_deadline.setAlignment(Qt.AlignCenter)
        self.task_deadline.setReadOnly(False)
        self.task_deadline.setProperty(u"showGroupSeparator", False)
        self.task_deadline.setCalendarPopup(True)
        self.task_deadline.setTimeSpec(Qt.LocalTime)
        self.task_estimated_time = QSlider(self.centralwidget)
        self.task_estimated_time.setObjectName(u"task_estimated_time")
        self.task_estimated_time.setGeometry(QRect(260, 110, 171, 31))
        self.task_estimated_time.setFocusPolicy(Qt.StrongFocus)
        self.task_estimated_time.setMinimum(1)
        self.task_estimated_time.setMaximum(1)
        self.task_estimated_time.setPageStep(5)
        self.task_estimated_time.setOrientation(Qt.Horizontal)
        self.task_estimated_time_disp = QLabel(self.centralwidget)
        self.task_estimated_time_disp.setObjectName(u"task_estimated_time_disp")
        self.task_estimated_time_disp.setGeometry(QRect(440, 110, 21, 31))
        self.task_estimated_time_disp.setFont(font1)
        self.task_estimated_time_disp.setFrameShape(QFrame.Box)
        self.task_estimated_time_disp.setFrameShadow(QFrame.Plain)
        self.task_estimated_time_disp.setLineWidth(2)
        self.task_estimated_time_disp.setAlignment(Qt.AlignCenter)
        self.todo_list_widget = QTableWidget(self.centralwidget)
        self.todo_list_widget.setObjectName(u"todo_list_widget")
        self.todo_list_widget.setGeometry(QRect(50, 190, 701, 400))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.todo_list_widget.sizePolicy().hasHeightForWidth())
        self.todo_list_widget.setSizePolicy(sizePolicy)
        self.todo_list_widget.setMaximumSize(QSize(701, 400))
        self.sort_by_deadline_button = QPushButton(self.centralwidget)
        self.sort_by_deadline_button.setObjectName(u"sort_by_deadline_button")
        self.sort_by_deadline_button.setGeometry(QRect(670, 120, 80, 21))
        self.sort_by_estimated_time_button = QPushButton(self.centralwidget)
        self.sort_by_estimated_time_button.setObjectName(u"sort_by_estimated_time_button")
        self.sort_by_estimated_time_button.setGeometry(QRect(670, 140, 80, 21))
        self.sort_by_priority_button = QPushButton(self.centralwidget)
        self.sort_by_priority_button.setObjectName(u"sort_by_priority_button")
        self.sort_by_priority_button.setGeometry(QRect(670, 160, 80, 21))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TODO\u30ea\u30b9\u30c8", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u8ffd\u52a0", None))
        self.task_deadline.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd H:mm", None))
        self.task_estimated_time_disp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>0</p></body></html>", None))
        self.sort_by_deadline_button.setText(QCoreApplication.translate("MainWindow", u"\u671f\u65e5\u9806", None))
        self.sort_by_estimated_time_button.setText(QCoreApplication.translate("MainWindow", u"\u898b\u8fbc\u307f\u6642\u9593\u9806", None))
        self.sort_by_priority_button.setText(QCoreApplication.translate("MainWindow", u"\u512a\u5148\u5ea6\u9806", None))
    # retranslateUi


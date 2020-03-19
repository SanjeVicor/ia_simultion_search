# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config-simulator.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1056, 553)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.contentVLayout = QVBoxLayout()
        self.contentVLayout.setObjectName(u"contentVLayout")

        self.gridLayout_2.addLayout(self.contentVLayout, 1, 0, 1, 1)

        self.mapGrd = QGridLayout()
        self.mapGrd.setSpacing(1)
        self.mapGrd.setObjectName(u"mapGrd")

        self.gridLayout_2.addLayout(self.mapGrd, 1, 1, 1, 1)

        self.XGrd = QGridLayout()
        self.XGrd.setObjectName(u"XGrd")

        self.gridLayout_2.addLayout(self.XGrd, 0, 1, 1, 1)

        self.go_back = QPushButton(self.centralwidget)
        self.go_back.setObjectName(u"go_back")
        self.go_back.setMaximumSize(QSize(74, 16777215))
        self.go_back.setStyleSheet(u"background-color: rgb(52, 101, 164);")
        icon = QIcon()
        icon.addFile(u"go-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.go_back.setIcon(icon)

        self.gridLayout_2.addWidget(self.go_back, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.go_back.setText(QCoreApplication.translate("MainWindow", u"ir atras", None))
    # retranslateUi


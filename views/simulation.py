# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulator.ui'
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
        MainWindow.resize(1058, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rewardLbl = QLabel(self.centralwidget)
        self.rewardLbl.setObjectName(u"rewardLbl")
        self.rewardLbl.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_2.addWidget(self.rewardLbl, 0, 0, 1, 1)

        self.mapGrd = QGridLayout()
        self.mapGrd.setSpacing(1)
        self.mapGrd.setObjectName(u"mapGrd")

        self.gridLayout_2.addLayout(self.mapGrd, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rewardLbl.setText(QCoreApplication.translate("MainWindow", u"Costo Actual :", None))
    # retranslateUi


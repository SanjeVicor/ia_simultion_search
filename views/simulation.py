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
        MainWindow.resize(492, 376)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.rewardLbl = QLabel(self.centralwidget)
        self.rewardLbl.setObjectName(u"rewardLbl")
        self.rewardLbl.setMaximumSize(QSize(16777215, 15))

        self.gridLayout_2.addWidget(self.rewardLbl, 2, 0, 1, 1)

        self.restart_btn = QPushButton(self.centralwidget)
        self.restart_btn.setObjectName(u"restart_btn")

        self.gridLayout_2.addWidget(self.restart_btn, 5, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ColumnLyt = QHBoxLayout()
        self.ColumnLyt.setSpacing(1)
        self.ColumnLyt.setObjectName(u"ColumnLyt")

        self.verticalLayout_5.addLayout(self.ColumnLyt)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.RowLyt = QVBoxLayout()
        self.RowLyt.setSpacing(1)
        self.RowLyt.setObjectName(u"RowLyt")

        self.horizontalLayout_2.addLayout(self.RowLyt)

        self.mapGrd = QGridLayout()
        self.mapGrd.setSpacing(1)
        self.mapGrd.setObjectName(u"mapGrd")

        self.horizontalLayout_2.addLayout(self.mapGrd)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_5, 4, 0, 1, 1)

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
        self.restart_btn.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
    # retranslateUi


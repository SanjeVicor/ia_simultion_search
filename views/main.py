# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
        MainWindow.resize(603, 125)
        MainWindow.setStyleSheet(u"background-color: rgb(136, 138, 133);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loadFileBtn = QPushButton(self.centralwidget)
        self.loadFileBtn.setObjectName(u"loadFileBtn")
        self.loadFileBtn.setGeometry(QRect(10, 50, 88, 27))
        self.loadFileBtn.setStyleSheet(u"color: rgb(238, 238, 236);\n"
"background-color: rgba(0, 0, 0, 0);\n"
"border-color: rgba(191, 64, 64, 0);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 19))
        self.fileDirectionLbl = QLabel(self.centralwidget)
        self.fileDirectionLbl.setObjectName(u"fileDirectionLbl")
        self.fileDirectionLbl.setGeometry(QRect(90, 10, 491, 19))
        self.loadBtn = QPushButton(self.centralwidget)
        self.loadBtn.setObjectName(u"loadBtn")
        self.loadBtn.setEnabled(False)
        self.loadBtn.setGeometry(QRect(260, 70, 88, 27))
        self.loadBtn.setStyleSheet(u"background-color: rgb(52, 101, 164);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.loadFileBtn.setText(QCoreApplication.translate("MainWindow", u"Cargar Mapa", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Direcci\u00f3n :", None))
        self.fileDirectionLbl.setText("")
        self.loadBtn.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
    # retranslateUi


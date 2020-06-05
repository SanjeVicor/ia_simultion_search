# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'priority.ui'
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(539, 162)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"")
        self.label_5.setScaledContents(True)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setItalic(True)
        self.label_6.setFont(font1)
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.ketHLyt = QHBoxLayout()
        self.ketHLyt.setObjectName(u"ketHLyt")

        self.verticalLayout.addLayout(self.ketHLyt)

        self.priorityHLyt = QHBoxLayout()
        self.priorityHLyt.setObjectName(u"priorityHLyt")

        self.verticalLayout.addLayout(self.priorityHLyt)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)

        self.verticalLayout.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Prioridad Direccional", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Prioridad direccional", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Arrastre a la prioridad correspondiente", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Aceptar", None))
    # retranslateUi


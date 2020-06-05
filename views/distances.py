# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'distances.ui'
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
        Dialog.resize(368, 218)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.ManBtn = QPushButton(Dialog)
        self.ManBtn.setObjectName(u"ManBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.ManBtn.sizePolicy().hasHeightForWidth())
        self.ManBtn.setSizePolicy(sizePolicy1)
        self.ManBtn.setMinimumSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.ManBtn)

        self.EuBtn = QPushButton(Dialog)
        self.EuBtn.setObjectName(u"EuBtn")
        sizePolicy1.setHeightForWidth(self.EuBtn.sizePolicy().hasHeightForWidth())
        self.EuBtn.setSizePolicy(sizePolicy1)
        self.EuBtn.setMinimumSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.EuBtn)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Distancias", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Eliga la medida de distancia", None))
        self.ManBtn.setText(QCoreApplication.translate("Dialog", u"Medida Manhattan", None))
        self.EuBtn.setText(QCoreApplication.translate("Dialog", u"Medida Euclidiana", None))
    # retranslateUi


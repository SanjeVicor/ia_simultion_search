# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simulations_dialog.ui'
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
        Dialog.resize(366, 377)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.manualBtn = QPushButton(Dialog)
        self.manualBtn.setObjectName(u"manualBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.manualBtn.sizePolicy().hasHeightForWidth())
        self.manualBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.manualBtn)

        self.depthBtn = QPushButton(Dialog)
        self.depthBtn.setObjectName(u"depthBtn")
        sizePolicy.setHeightForWidth(self.depthBtn.sizePolicy().hasHeightForWidth())
        self.depthBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.depthBtn)

        self.breathBtn = QPushButton(Dialog)
        self.breathBtn.setObjectName(u"breathBtn")
        sizePolicy.setHeightForWidth(self.breathBtn.sizePolicy().hasHeightForWidth())
        self.breathBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.breathBtn)

        self.backtrackingBtn = QPushButton(Dialog)
        self.backtrackingBtn.setObjectName(u"backtrackingBtn")
        sizePolicy.setHeightForWidth(self.backtrackingBtn.sizePolicy().hasHeightForWidth())
        self.backtrackingBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.backtrackingBtn)

        self.UCSBtn = QPushButton(Dialog)
        self.UCSBtn.setObjectName(u"UCSBtn")
        sizePolicy.setHeightForWidth(self.UCSBtn.sizePolicy().hasHeightForWidth())
        self.UCSBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.UCSBtn)

        self.greedyBtn = QPushButton(Dialog)
        self.greedyBtn.setObjectName(u"greedyBtn")
        sizePolicy.setHeightForWidth(self.greedyBtn.sizePolicy().hasHeightForWidth())
        self.greedyBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.greedyBtn)

        self.AStarBtn = QPushButton(Dialog)
        self.AStarBtn.setObjectName(u"AStarBtn")
        sizePolicy.setHeightForWidth(self.AStarBtn.sizePolicy().hasHeightForWidth())
        self.AStarBtn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.AStarBtn)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Simulaciones", None))
        self.manualBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda Manual (Teclado)", None))
        self.depthBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda en Profundidad", None))
        self.breathBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda en Anchura", None))
        self.backtrackingBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda Backtracking", None))
        self.UCSBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda Coste Uniforme", None))
        self.greedyBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda Voraz primero el mejor", None))
        self.AStarBtn.setText(QCoreApplication.translate("Dialog", u"Busqueda A*", None))
    # retranslateUi


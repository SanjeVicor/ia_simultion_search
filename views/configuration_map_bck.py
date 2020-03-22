# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'secundary_window-pruebas.ui'
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


class Ui_TemplateWindow(object):
    def setupUi(self, TemplateWindow):
        if TemplateWindow.objectName():
            TemplateWindow.setObjectName(u"TemplateWindow")
        TemplateWindow.resize(506, 749)
        self.centralwidget = QWidget(TemplateWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.updateBtn = QPushButton(self.centralwidget)
        self.updateBtn.setObjectName(u"updateBtn")
        self.updateBtn.setMaximumSize(QSize(100, 200))
        self.updateBtn.setStyleSheet(u"background-color: rgb(52, 101, 164);\n"
"color: rgb(238, 238, 236);")

        self.gridLayout.addWidget(self.updateBtn, 22, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(370, 16777215))
        font = QFont()
        font.setPointSize(24)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 8, 0, 1, 1)

        self.landTxt = QPlainTextEdit(self.centralwidget)
        self.landTxt.setObjectName(u"landTxt")
        self.landTxt.setMaximumSize(QSize(370, 30))

        self.gridLayout.addWidget(self.landTxt, 6, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.coordTxt = QTextEdit(self.centralwidget)
        self.coordTxt.setObjectName(u"coordTxt")
        self.coordTxt.setMaximumSize(QSize(370, 30))

        self.gridLayout.addWidget(self.coordTxt, 20, 0, 1, 1)

        self.nextBtn = QPushButton(self.centralwidget)
        self.nextBtn.setObjectName(u"nextBtn")
        self.nextBtn.setEnabled(False)
        self.nextBtn.setMaximumSize(QSize(100, 16777215))

        self.gridLayout.addWidget(self.nextBtn, 25, 0, 1, 1)

        self.XGrd = QGridLayout()
        self.XGrd.setSpacing(0)
        self.XGrd.setObjectName(u"XGrd")
        self.XGrd.setContentsMargins(3, -1, 3, -1)

        self.gridLayout.addLayout(self.XGrd, 1, 2, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.label_2, 16, 0, 1, 1)

        self.landLst = QListWidget(self.centralwidget)
        self.landLst.setObjectName(u"landLst")
        self.landLst.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.landLst, 2, 0, 1, 1)

        self.addLandBtn = QPushButton(self.centralwidget)
        self.addLandBtn.setObjectName(u"addLandBtn")
        self.addLandBtn.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.addLandBtn, 7, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(370, 16777215))
        font1 = QFont()
        font1.setPointSize(27)
        self.label_6.setFont(font1)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)

        self.go_backBtn = QPushButton(self.centralwidget)
        self.go_backBtn.setObjectName(u"go_backBtn")
        self.go_backBtn.setMaximumSize(QSize(74, 16777215))
        self.go_backBtn.setStyleSheet(u"background-color: rgb(114, 159, 207);")
        icon = QIcon()
        icon.addFile(u"go-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.go_backBtn.setIcon(icon)

        self.gridLayout.addWidget(self.go_backBtn, 0, 0, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.label, 17, 0, 1, 1)

        self.landLbl = QLabel(self.centralwidget)
        self.landLbl.setObjectName(u"landLbl")
        self.landLbl.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.landLbl, 21, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(370, 16777215))

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.mapGrd = QGridLayout()
        self.mapGrd.setObjectName(u"mapGrd")
        self.mapGrd.setHorizontalSpacing(0)
        self.mapGrd.setVerticalSpacing(3)
        self.mapGrd.setContentsMargins(3, 3, 3, 3)

        self.gridLayout.addLayout(self.mapGrd, 2, 2, 17, 1)

        self.YGrd = QGridLayout()
        self.YGrd.setObjectName(u"YGrd")
        self.YGrd.setHorizontalSpacing(0)
        self.YGrd.setVerticalSpacing(3)
        self.YGrd.setContentsMargins(3, 3, 3, 3)

        self.gridLayout.addLayout(self.YGrd, 2, 1, 16, 1)

        TemplateWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(TemplateWindow)
        self.statusbar.setObjectName(u"statusbar")
        TemplateWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TemplateWindow)

        QMetaObject.connectSlotsByName(TemplateWindow)
    # setupUi

    def retranslateUi(self, TemplateWindow):
        TemplateWindow.setWindowTitle(QCoreApplication.translate("TemplateWindow", u"MainWindow", None))
        self.updateBtn.setText(QCoreApplication.translate("TemplateWindow", u"Actualizar", None))
        self.label_7.setText(QCoreApplication.translate("TemplateWindow", u"Asignar Terrenos", None))
        self.label_5.setText(QCoreApplication.translate("TemplateWindow", u"Nombre", None))
        self.nextBtn.setText(QCoreApplication.translate("TemplateWindow", u"Terminar", None))
        self.label_2.setText(QCoreApplication.translate("TemplateWindow", u"Ingresa las coordenadas de la siguiente manera : 1 , A", None))
        self.addLandBtn.setText(QCoreApplication.translate("TemplateWindow", u"Agregar", None))
        self.label_6.setText(QCoreApplication.translate("TemplateWindow", u"Agregar terreno", None))
        self.label_8.setText(QCoreApplication.translate("TemplateWindow", u"Haz click en un terreno (imagen)", None))
        self.go_backBtn.setText(QCoreApplication.translate("TemplateWindow", u"ir atras", None))
        self.label.setText(QCoreApplication.translate("TemplateWindow", u"Ingresa un n\u00famero especifico del mapa", None))
        self.landLbl.setText(QCoreApplication.translate("TemplateWindow", u"No seleccionado", None))
        self.label_4.setText(QCoreApplication.translate("TemplateWindow", u"Terrenos", None))
    # retranslateUi


# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character_selection.ui'
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
        MainWindow.resize(1005, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.formLayoutWidget = QWidget(self.centralwidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(440, 10, 561, 561))
        self.character_edit_lyt = QFormLayout(self.formLayoutWidget)
        self.character_edit_lyt.setObjectName(u"character_edit_lyt")
        self.character_edit_lyt.setContentsMargins(0, 0, 0, 0)
        self.accept_btn = QPushButton(self.formLayoutWidget)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setFlat(False)

        self.character_edit_lyt.setWidget(1, QFormLayout.FieldRole, self.accept_btn)

        self.images_lst = QListWidget(self.formLayoutWidget)
        self.images_lst.setObjectName(u"images_lst")

        self.character_edit_lyt.setWidget(2, QFormLayout.LabelRole, self.images_lst)

        self.image_lbl = QLabel(self.formLayoutWidget)
        self.image_lbl.setObjectName(u"image_lbl")

        self.character_edit_lyt.setWidget(2, QFormLayout.FieldRole, self.image_lbl)

        self.search_img_btn = QPushButton(self.formLayoutWidget)
        self.search_img_btn.setObjectName(u"search_img_btn")

        self.character_edit_lyt.setWidget(3, QFormLayout.LabelRole, self.search_img_btn)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 20pt \"DejaVu Sans\";")

        self.character_edit_lyt.setWidget(4, QFormLayout.SpanningRole, self.label)

        self.name_txt = QLineEdit(self.formLayoutWidget)
        self.name_txt.setObjectName(u"name_txt")

        self.character_edit_lyt.setWidget(1, QFormLayout.LabelRole, self.name_txt)

        self.go_back_btn = QPushButton(self.centralwidget)
        self.go_back_btn.setObjectName(u"go_back_btn")
        self.go_back_btn.setGeometry(QRect(10, 10, 88, 27))
        self.go_back_btn.setStyleSheet(u"background-color: rgb(114, 159, 207);")
        icon = QIcon()
        icon.addFile(u"go-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.go_back_btn.setIcon(icon)
        self.formLayoutWidget_2 = QWidget(self.centralwidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(9, 59, 421, 511))
        self.select_character_lyt = QFormLayout(self.formLayoutWidget_2)
        self.select_character_lyt.setObjectName(u"select_character_lyt")
        self.select_character_lyt.setContentsMargins(0, 0, 0, 0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.accept_btn.setText(QCoreApplication.translate("MainWindow", u"ir a simulaci\u00f3n", None))
        self.image_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.search_img_btn.setText(QCoreApplication.translate("MainWindow", u"Buscar m\u00e1s", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Costos", None))
        self.go_back_btn.setText(QCoreApplication.translate("MainWindow", u"ir atras", None))
    # retranslateUi


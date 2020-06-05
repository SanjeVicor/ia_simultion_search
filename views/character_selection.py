# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'character_selection_new.ui'
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
        MainWindow.resize(920, 507)
        font = QFont()
        font.setFamily(u"Sans Serif")
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.go_back_btn = QPushButton(self.centralwidget)
        self.go_back_btn.setObjectName(u"go_back_btn")
        self.go_back_btn.setStyleSheet(u"background-color: rgb(114, 159, 207);")
        icon = QIcon()
        icon.addFile(u"../../project_stable/views/go-back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.go_back_btn.setIcon(icon)

        self.gridLayout.addWidget(self.go_back_btn, 3, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.character_edit_lyt = QFormLayout()
        self.character_edit_lyt.setObjectName(u"character_edit_lyt")
        self.images_lst = QListWidget(self.centralwidget)
        self.images_lst.setObjectName(u"images_lst")

        self.character_edit_lyt.setWidget(2, QFormLayout.LabelRole, self.images_lst)

        self.search_img_btn = QPushButton(self.centralwidget)
        self.search_img_btn.setObjectName(u"search_img_btn")

        self.character_edit_lyt.setWidget(3, QFormLayout.LabelRole, self.search_img_btn)

        self.image_lbl = QLabel(self.centralwidget)
        self.image_lbl.setObjectName(u"image_lbl")
        self.image_lbl.setMaximumSize(QSize(300, 16777215))

        self.character_edit_lyt.setWidget(2, QFormLayout.FieldRole, self.image_lbl)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setFamily(u"DejaVu Sans Mono")
        font1.setPointSize(20)
        self.label_3.setFont(font1)

        self.character_edit_lyt.setWidget(4, QFormLayout.FieldRole, self.label_3)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 75 20pt \"DejaVu Sans\";")

        self.character_edit_lyt.setWidget(4, QFormLayout.LabelRole, self.label)

        self.name_txt = QLineEdit(self.centralwidget)
        self.name_txt.setObjectName(u"name_txt")
        self.name_txt.setMaximumSize(QSize(500, 16777215))

        self.character_edit_lyt.setWidget(1, QFormLayout.FieldRole, self.name_txt)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.character_edit_lyt.setWidget(0, QFormLayout.FieldRole, self.label_2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.character_edit_lyt.setWidget(1, QFormLayout.LabelRole, self.label_5)


        self.horizontalLayout.addLayout(self.character_edit_lyt)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 52))
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(75)
        self.label_4.setFont(font2)

        self.verticalLayout.addWidget(self.label_4)

        self.select_character_lyt = QFormLayout()
        self.select_character_lyt.setObjectName(u"select_character_lyt")

        self.verticalLayout.addLayout(self.select_character_lyt)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.accept_btn = QPushButton(self.centralwidget)
        self.accept_btn.setObjectName(u"accept_btn")
        self.accept_btn.setFlat(False)

        self.gridLayout.addWidget(self.accept_btn, 2, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.go_back_btn.setText(QCoreApplication.translate("MainWindow", u"ir atras", None))
        self.search_img_btn.setText(QCoreApplication.translate("MainWindow", u"Cargar m\u00e1s personajes", None))
        self.image_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Costos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Terrenos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Nombre del personaje", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Eliga la imagen del personaje", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Selecciona un personaje para empezar a editar", None))
        self.accept_btn.setText(QCoreApplication.translate("MainWindow", u"ir a simulaci\u00f3n", None))
    # retranslateUi


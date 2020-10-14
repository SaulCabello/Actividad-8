# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(294, 503)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 420, 75, 23))
        self.spinBox_7 = QSpinBox(self.groupBox)
        self.spinBox_7.setObjectName(u"spinBox_7")
        self.spinBox_7.setGeometry(QRect(120, 140, 42, 22))
        self.spinBox_7.setMaximum(500)
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 60, 61, 21))
        self.label_11 = QLabel(self.groupBox)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(240, 220, 41, 16))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 300, 61, 21))
        self.spinBox_3 = QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName(u"spinBox_3")
        self.spinBox_3.setGeometry(QRect(170, 380, 42, 22))
        self.spinBox_3.setMaximum(255)
        self.spinBox_8 = QSpinBox(self.groupBox)
        self.spinBox_8.setObjectName(u"spinBox_8")
        self.spinBox_8.setGeometry(QRect(120, 180, 42, 22))
        self.spinBox_8.setMaximum(500)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 61, 21))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 180, 61, 21))
        self.lineEdit_2 = QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 220, 113, 20))
        self.spinBox_2 = QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(170, 340, 42, 22))
        self.spinBox_2.setMaximum(255)
        self.lineEdit = QLineEdit(self.groupBox)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 20, 113, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 61, 21))
        self.spinBox_6 = QSpinBox(self.groupBox)
        self.spinBox_6.setObjectName(u"spinBox_6")
        self.spinBox_6.setGeometry(QRect(120, 100, 42, 22))
        self.spinBox_6.setMaximum(500)
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 220, 61, 21))
        self.label_8 = QLabel(self.groupBox)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 260, 61, 21))
        self.spinBox = QSpinBox(self.groupBox)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(170, 300, 42, 22))
        self.spinBox.setMaximum(255)
        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(70, 380, 61, 21))
        self.spinBox_5 = QSpinBox(self.groupBox)
        self.spinBox_5.setObjectName(u"spinBox_5")
        self.spinBox_5.setGeometry(QRect(120, 60, 42, 22))
        self.spinBox_5.setMaximum(500)
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(70, 340, 61, 21))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 21))

        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 294, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Aceptar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Origen x:", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Rojo:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Origen Y:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Destino y:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Destino x:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Velocidad:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Color (RGB):", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Azul", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Verde:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
    # retranslateUi


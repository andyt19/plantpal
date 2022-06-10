# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addPlantFrameDPINSL.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_homeFrame(object):
    def setupUi(self, homeFrame):
        if not homeFrame.objectName():
            homeFrame.setObjectName(u"homeFrame")
        homeFrame.resize(600, 800)
        homeFrame.setMinimumSize(QSize(600, 800))
        homeFrame.setMaximumSize(QSize(600, 800))
        self.background = QWidget(homeFrame)
        self.background.setObjectName(u"background")
        self.background.setGeometry(QRect(0, 0, 601, 801))
        self.background.setStyleSheet(u"QWidget#background{\n"
"background-color: #a2b5b0;}")
        self.waterWgt = QWidget(self.background)
        self.waterWgt.setObjectName(u"waterWgt")
        self.waterWgt.setGeometry(QRect(50, 100, 500, 661))
        self.waterWgt.setStyleSheet(u"QWidget#waterWgt{border-radius: 15px;\n"
"background-color: #C5DCD6;}")
        self.nameField = QLineEdit(self.waterWgt)
        self.nameField.setObjectName(u"nameField")
        self.nameField.setGeometry(QRect(50, 60, 401, 51))
        self.nameField.setStyleSheet(u"background-color: #f7f7f7;\n"
"font: \"Lato\";\n"
"font-size: 22px;")
        self.nameLabel = QLabel(self.waterWgt)
        self.nameLabel.setObjectName(u"nameLabel")
        self.nameLabel.setGeometry(QRect(50, 20, 71, 31))
        self.nameLabel.setStyleSheet(u"font: \"Lato\";\n"
"font-size: 26px;")
        self.varietyLabel = QLabel(self.waterWgt)
        self.varietyLabel.setObjectName(u"varietyLabel")
        self.varietyLabel.setGeometry(QRect(50, 140, 101, 31))
        self.varietyLabel.setStyleSheet(u"font: \"Lato\";\n"
"font-size: 26px;")
        self.varietyField = QLineEdit(self.waterWgt)
        self.varietyField.setObjectName(u"varietyField")
        self.varietyField.setGeometry(QRect(50, 180, 401, 51))
        self.varietyField.setStyleSheet(u"background-color: #f7f7f7;\n"
"font: \"Lato\";\n"
"font-size: 22px;")
        self.waterLabel1 = QLabel(self.waterWgt)
        self.waterLabel1.setObjectName(u"waterLabel1")
        self.waterLabel1.setGeometry(QRect(50, 280, 151, 31))
        self.waterLabel1.setStyleSheet(u"font: \"Lato\";\n"
"font-size: 26px;")
        self.waterField = QLineEdit(self.waterWgt)
        self.waterField.setObjectName(u"waterField")
        self.waterField.setGeometry(QRect(200, 270, 31, 51))
        self.waterField.setCursor(QCursor(Qt.IBeamCursor))
        self.waterField.setStyleSheet(u"background-color: #f7f7f7;\n"
"font: \"Lato\";\n"
"font-size: 22px;")
        self.waterField.setAlignment(Qt.AlignCenter)
        self.lastWateredLabel = QLabel(self.waterWgt)
        self.lastWateredLabel.setObjectName(u"lastWateredLabel")
        self.lastWateredLabel.setGeometry(QRect(50, 360, 161, 31))
        self.lastWateredLabel.setToolTipDuration(1)
        self.lastWateredLabel.setStyleSheet(u"font: \"Lato\";\n"
"font-size: 26px;")
        self.waterLabel2 = QLabel(self.waterWgt)
        self.waterLabel2.setObjectName(u"waterLabel2")
        self.waterLabel2.setGeometry(QRect(240, 280, 61, 31))
        self.waterLabel2.setStyleSheet(u"font: \"Lato\";\n"
"font-size: 26px;")
        self.lastWateredField = QDateEdit(self.waterWgt)
        self.lastWateredField.setObjectName(u"lastWateredField")
        self.lastWateredField.setGeometry(QRect(50, 400, 131, 41))
        font = QFont()
        font.setPointSize(14)
        self.lastWateredField.setFont(font)
        self.lastWateredField.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.lastWateredField.setMaximumDateTime(QDateTime(QDate(9999, 8, 30), QTime(23, 59, 59)))
        self.lastWateredField.setMinimumDateTime(QDateTime(QDate(1752, 10, 14), QTime(0, 0, 0)))
        self.lastWateredField.setCalendarPopup(True)
        self.bdayLabel = QLabel(self.waterWgt)
        self.bdayLabel.setObjectName(u"bdayLabel")
        self.bdayLabel.setGeometry(QRect(280, 360, 161, 31))
        self.bdayLabel.setStyleSheet(u"font: \"Lato\";\n"
"font-size: 26px;")
        self.bdayField = QDateEdit(self.waterWgt)
        self.bdayField.setObjectName(u"bdayField")
        self.bdayField.setGeometry(QRect(280, 400, 131, 41))
        self.bdayField.setFont(font)
        self.bdayField.setDateTime(QDateTime(QDate(2000, 1, 1), QTime(0, 0, 0)))
        self.bdayField.setMaximumDateTime(QDateTime(QDate(9999, 8, 30), QTime(23, 59, 59)))
        self.bdayField.setMinimumDateTime(QDateTime(QDate(1752, 10, 14), QTime(0, 0, 0)))
        self.bdayField.setCalendarPopup(True)
        self.submitBtn = QPushButton(self.waterWgt)
        self.submitBtn.setObjectName(u"submitBtn")
        self.submitBtn.setGeometry(QRect(170, 510, 161, 51))
        self.submitBtn.setStyleSheet(u"*{\n"
"font: \"Lato\";\n"
"border: 4px solid '#bbd1cb';\n"
"border-radius: 10px;\n"
"font-size: 26px;\n"
"background-color: #bbd1cb\n"
"}\n"
"*:hover{\n"
"border: 4px solid '#b4c8c2';\n"
"background-color:'#b4c8c2';\n"
"}\n"
"")
        self.errorLabel = QLabel(self.waterWgt)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(140, 470, 221, 31))
        font1 = QFont()
        font1.setFamily(u"Lato Semibold")
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setWeight(75)
        self.errorLabel.setFont(font1)
        self.errorLabel.setStyleSheet(u"color: #cc0000;")
        self.plantWidget_2 = QWidget(self.waterWgt)
        self.plantWidget_2.setObjectName(u"plantWidget_2")
        self.plantWidget_2.setGeometry(QRect(20, 490, 480, 100))
        self.plantWidget_2.setMinimumSize(QSize(480, 100))
        self.plantWidget_2.setMaximumSize(QSize(480, 100))
        self.plantWidget_2.setStyleSheet(u"background-color: #afd498;")
        self.nameLabel_12 = QLabel(self.plantWidget_2)
        self.nameLabel_12.setObjectName(u"nameLabel_12")
        self.nameLabel_12.setGeometry(QRect(10, 20, 241, 41))
        font2 = QFont()
        font2.setFamily(u"Lato")
        font2.setPointSize(16)
        self.nameLabel_12.setFont(font2)
        self.waterBtn_11 = QPushButton(self.plantWidget_2)
        self.waterBtn_11.setObjectName(u"waterBtn_11")
        self.waterBtn_11.setGeometry(QRect(380, 29, 81, 41))
        self.waterBtn_11.setMinimumSize(QSize(81, 41))
        self.waterBtn_11.setMaximumSize(QSize(81, 41))
        self.waterBtn_11.setStyleSheet(u"*{\n"
"font: \"Lato\";\n"
"color: #2f2f2f;\n"
"border: 2px solid #97d0d5;\n"
"background-color: #9ed8de;\n"
"border-radius: 5px;\n"
"font-size: 18px;\n"
"}\n"
"*:hover{\n"
"border: 4px solid #97d0d5;\n"
"background-color: #97d0d5;\n"
"}\n"
"")
        self.nameLabel_13 = QLabel(self.plantWidget_2)
        self.nameLabel_13.setObjectName(u"nameLabel_13")
        self.nameLabel_13.setGeometry(QRect(10, 60, 241, 31))
        font3 = QFont()
        font3.setFamily(u"Lato Light")
        font3.setPointSize(12)
        self.nameLabel_13.setFont(font3)
        self.nameLabel_14 = QLabel(self.plantWidget_2)
        self.nameLabel_14.setObjectName(u"nameLabel_14")
        self.nameLabel_14.setGeometry(QRect(270, 30, 101, 41))
        font4 = QFont()
        font4.setFamily(u"Lato Light")
        font4.setPointSize(14)
        self.nameLabel_14.setFont(font4)
        self.nameLabel_14.setStyleSheet(u"color: #6a3d27;")
        self.backBtn = QPushButton(self.background)
        self.backBtn.setObjectName(u"backBtn")
        self.backBtn.setGeometry(QRect(50, 30, 81, 50))
        self.backBtn.setStyleSheet(u"*{\n"
"font: \"Lato\";\n"
"font-size: 64px;\n"
"border-radius: 5px;\n"
"color: #ebebeb;\n"
"}\n"
"")
        self.plantWidget = QWidget(self.background)
        self.plantWidget.setObjectName(u"plantWidget")
        self.plantWidget.setGeometry(QRect(570, 420, 480, 100))
        self.plantWidget.setMinimumSize(QSize(480, 100))
        self.plantWidget.setMaximumSize(QSize(480, 100))
        self.plantWidget.setStyleSheet(u"background-color: #afd498;")
        self.nameLabel_10 = QLabel(self.plantWidget)
        self.nameLabel_10.setObjectName(u"nameLabel_10")
        self.nameLabel_10.setGeometry(QRect(10, 20, 241, 41))
        self.nameLabel_10.setFont(font2)
        self.waterBtn_10 = QPushButton(self.plantWidget)
        self.waterBtn_10.setObjectName(u"waterBtn_10")
        self.waterBtn_10.setGeometry(QRect(380, 29, 81, 41))
        self.waterBtn_10.setMinimumSize(QSize(81, 41))
        self.waterBtn_10.setMaximumSize(QSize(81, 41))
        self.waterBtn_10.setStyleSheet(u"*{\n"
"font: \"Lato\";\n"
"color: #2f2f2f;\n"
"border: 2px solid #97d0d5;\n"
"background-color: #9ed8de;\n"
"border-radius: 5px;\n"
"font-size: 18px;\n"
"}\n"
"*:hover{\n"
"border: 4px solid #97d0d5;\n"
"background-color: #97d0d5;\n"
"}\n"
"")
        self.editBtn_10 = QPushButton(self.plantWidget)
        self.editBtn_10.setObjectName(u"editBtn_10")
        self.editBtn_10.setGeometry(QRect(280, 30, 81, 41))
        self.editBtn_10.setMinimumSize(QSize(81, 41))
        self.editBtn_10.setMaximumSize(QSize(81, 41))
        self.editBtn_10.setStyleSheet(u"*{\n"
"font: \"Lato\";\n"
"color :#2f2f2f;\n"
"border: 2px solid #cfd6d4;\n"
"background-color: #dce3e1;\n"
"border-radius: 5px;\n"
"font-size: 18px;\n"
"}\n"
"*:hover{\n"
"border: 4px solid #cfd6d4;\n"
"background-color: #cfd6d4;\n"
"}\n"
"")
        self.nameLabel_11 = QLabel(self.plantWidget)
        self.nameLabel_11.setObjectName(u"nameLabel_11")
        self.nameLabel_11.setGeometry(QRect(10, 60, 241, 31))
        self.nameLabel_11.setFont(font3)

        self.retranslateUi(homeFrame)

        QMetaObject.connectSlotsByName(homeFrame)
    # setupUi

    def retranslateUi(self, homeFrame):
        homeFrame.setWindowTitle(QCoreApplication.translate("homeFrame", u"plantpal", None))
        self.nameField.setText("")
        self.nameLabel.setText(QCoreApplication.translate("homeFrame", u"Name", None))
        self.varietyLabel.setText(QCoreApplication.translate("homeFrame", u"Variety", None))
        self.varietyField.setText("")
        self.waterLabel1.setText(QCoreApplication.translate("homeFrame", u"Water every", None))
        self.waterField.setText("")
        self.waterField.setPlaceholderText(QCoreApplication.translate("homeFrame", u"5", None))
        self.lastWateredLabel.setText(QCoreApplication.translate("homeFrame", u"Last Watered", None))
        self.waterLabel2.setText(QCoreApplication.translate("homeFrame", u"days", None))
        self.bdayLabel.setText(QCoreApplication.translate("homeFrame", u"Birthday", None))
        self.submitBtn.setText(QCoreApplication.translate("homeFrame", u"Add Plant", None))
        self.errorLabel.setText("")
        self.nameLabel_12.setText(QCoreApplication.translate("homeFrame", u"LONG PLANT NAME", None))
        self.waterBtn_11.setText(QCoreApplication.translate("homeFrame", u"Water", None))
        self.nameLabel_13.setText(QCoreApplication.translate("homeFrame", u"Monstera Deliciosa", None))
        self.nameLabel_14.setText(QCoreApplication.translate("homeFrame", u"15 days ago", None))
        self.backBtn.setText(QCoreApplication.translate("homeFrame", u"\u2190", None))
        self.nameLabel_10.setText(QCoreApplication.translate("homeFrame", u"LONG PLANT NAME", None))
        self.waterBtn_10.setText(QCoreApplication.translate("homeFrame", u"Water", None))
        self.editBtn_10.setText(QCoreApplication.translate("homeFrame", u"Edit", None))
        self.nameLabel_11.setText(QCoreApplication.translate("homeFrame", u"Monstera Deliciosa", None))
    # retranslateUi


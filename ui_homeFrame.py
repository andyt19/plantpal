# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeFramezoQcRY.ui'
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
        self.waterWgt.setGeometry(QRect(50, 100, 500, 190))
        self.waterWgt.setStyleSheet(u"QWidget#waterWgt{border-radius: 15px;\n"
"background-color: #C5DCD6;}")
        self.waterLabel = QLabel(self.waterWgt)
        self.waterLabel.setObjectName(u"waterLabel")
        self.waterLabel.setGeometry(QRect(0, 0, 500, 50))
        self.waterLabel.setStyleSheet(u"padding: 10px;\n"
"font: \"Lato\";\n"
"font-size: 20px;\n"
"background-color: #d6efe8;\n"
"border-top-left-radius: 15px;\n"
"border-top-right-radius: 15px;\n"
"")
        self.scrollArea_2 = QScrollArea(self.waterWgt)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(-1, 49, 501, 131))
        self.scrollArea_2.setStyleSheet(u"border-radius: 15px;\n"
"background-color: #C5DCD6;")
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 501, 131))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plantWidget = QWidget(self.scrollAreaWidgetContents_2)
        self.plantWidget.setObjectName(u"plantWidget")
        self.plantWidget.setMinimumSize(QSize(480, 100))
        self.plantWidget.setMaximumSize(QSize(480, 100))
        self.plantWidget.setStyleSheet(u"background-color: #afd498;")
        self.nameLabel_8 = QLabel(self.plantWidget)
        self.nameLabel_8.setObjectName(u"nameLabel_8")
        self.nameLabel_8.setGeometry(QRect(10, 20, 241, 41))
        font = QFont()
        font.setFamily(u"Lato")
        font.setPointSize(16)
        self.nameLabel_8.setFont(font)
        self.waterBtn_9 = QPushButton(self.plantWidget)
        self.waterBtn_9.setObjectName(u"waterBtn_9")
        self.waterBtn_9.setGeometry(QRect(380, 29, 81, 41))
        self.waterBtn_9.setMinimumSize(QSize(81, 41))
        self.waterBtn_9.setMaximumSize(QSize(81, 41))
        self.waterBtn_9.setStyleSheet(u"*{\n"
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
        self.nameLabel_9 = QLabel(self.plantWidget)
        self.nameLabel_9.setObjectName(u"nameLabel_9")
        self.nameLabel_9.setGeometry(QRect(10, 60, 241, 31))
        font1 = QFont()
        font1.setFamily(u"Lato Light")
        font1.setPointSize(12)
        self.nameLabel_9.setFont(font1)

        self.verticalLayout.addWidget(self.plantWidget)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.addPlantBtn = QPushButton(self.background)
        self.addPlantBtn.setObjectName(u"addPlantBtn")
        self.addPlantBtn.setGeometry(QRect(400, 30, 150, 50))
        self.addPlantBtn.setStyleSheet(u"*{\n"
"font: \"Lato\";\n"
"border: 4px solid '#bbd1cb';\n"
"border-radius: 10px;\n"
"font-size: 20px;\n"
"background-color: #bbd1cb\n"
"}\n"
"*:hover{\n"
"border: 4px solid '#b4c8c2';\n"
"background-color:'#b4c8c2';\n"
"}\n"
"")
        self.plantsWgt = QWidget(self.background)
        self.plantsWgt.setObjectName(u"plantsWgt")
        self.plantsWgt.setGeometry(QRect(50, 329, 500, 410))
        self.plantsWgt.setStyleSheet(u"background-color: #C5DCD6;\n"
"border-radius: 15px;")
        self.scrollArea = QScrollArea(self.plantsWgt)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(-1, 6, 501, 391))
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 501, 391))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(homeFrame)

        QMetaObject.connectSlotsByName(homeFrame)
    # setupUi

    def retranslateUi(self, homeFrame):
        homeFrame.setWindowTitle(QCoreApplication.translate("homeFrame", u"plantpal", None))
        self.waterLabel.setText(QCoreApplication.translate("homeFrame", u"Needs Watering", None))
        self.nameLabel_8.setText(QCoreApplication.translate("homeFrame", u"LONG PLANT NAME", None))
        self.waterBtn_9.setText(QCoreApplication.translate("homeFrame", u"Water", None))
        self.nameLabel_9.setText(QCoreApplication.translate("homeFrame", u"Monstera Deliciosa", None))
        self.addPlantBtn.setText(QCoreApplication.translate("homeFrame", u"Add Plant", None))
    # retranslateUi


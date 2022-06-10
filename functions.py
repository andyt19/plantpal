from datetime import date, datetime
import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton, QFileDialog, QDialog, QStackedWidget
from PyQt5.QtGui import QPixmap, QCursor, QIntValidator, QFont
from PyQt5.QtCore import QDate, QSize, QRect

DB_NAME = "plants.db"

# connect to the SQL db
def connect():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    return cursor, conn

class homeScreen(QDialog):
    def __init__(self):
        super(homeScreen, self).__init__()
        loadUi("homeFrame.ui", self)

        self.addPlantBtn.clicked.connect(self.addPlant)

        self.loadPlants()
        self.loadNeedWater()

    # populate the needwater list
    def loadNeedWater(self):
        cursor, conn = connect()

        currDay = date.today()

        for row in cursor.execute("SELECT * from plant"):
            # take last_watered (string), convert it into a datetime, then convert to a date
            lastWatered = datetime.strptime(row[4], '%Y-%m-%d').date()

            # display plants that need water
            dayDiff = (currDay - lastWatered).days
            if dayDiff >= row[3]:
                self.plantWidget = QWidget(self.scrollAreaWidgetContents_2)
                self.plantWidget.setObjectName(u"plantWidget")
                self.plantWidget.setMinimumSize(QSize(480, 100))
                self.plantWidget.setMaximumSize(QSize(480, 100))
                self.plantWidget.setStyleSheet(u"background-color: #afd498;")

                self.nameLabel = QLabel(self.plantWidget)
                self.nameLabel.setObjectName(u"nameLabel")
                self.nameLabel.setGeometry(QRect(20, 20, 241, 41))
                font = QFont()
                font.setFamily(u"Lato")
                font.setPointSize(16)
                self.nameLabel.setFont(font)
                self.nameLabel.setText(row[1])

                self.varietyLabel = QLabel(self.plantWidget)
                self.varietyLabel.setObjectName(u"varietyLabel")
                self.varietyLabel.setGeometry(QRect(20, 60, 241, 31))
                font1 = QFont()
                font1.setFamily(u"Lato Light")
                font1.setPointSize(12)
                self.varietyLabel.setFont(font1)
                self.varietyLabel.setText(row[2])

                self.daysLabel = QLabel(self.plantWidget)
                self.daysLabel.setObjectName(u"daysLabel")
                self.daysLabel.setGeometry(QRect(270, 30, 241, 31))
                self.daysLabel.setStyleSheet(u"font: \"Lato\";\n"
                    "font-size: 14px;\n"
                    "color: #6a3d27;\n"
                    "")
                if dayDiff == 1: 
                    self.daysLabel.setText(f"{dayDiff} day ago")
                else:
                    self.daysLabel.setText(f"{dayDiff} days ago")

                self.waterBtn = QPushButton(self.plantWidget)
                self.waterBtn.setObjectName(u"waterBtn")
                self.waterBtn.setGeometry(QRect(380, 29, 81, 41))
                self.waterBtn.setMinimumSize(QSize(81, 41))
                self.waterBtn.setMaximumSize(QSize(81, 41))
                self.waterBtn.setStyleSheet(u"*{\n"
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
                self.waterBtn.setText("Water")
                self.waterBtn.clicked.connect(lambda checked, id=row[0]: self.water(id))

                self.verticalLayout.addWidget(self.plantWidget)

        conn.close()

    # populate plant display list
    def loadPlants(self):
        cursor, conn = connect()

        for row in cursor.execute("SELECT * from plant"):
            self.plantWidget = QWidget(self.scrollAreaWidgetContents)
            self.plantWidget.setObjectName(u"plantWidget")
            self.plantWidget.setMinimumSize(QSize(480, 100))
            self.plantWidget.setMaximumSize(QSize(480, 100))
            self.plantWidget.setStyleSheet(u"background-color: #afd498;")

            self.nameLabel = QLabel(self.plantWidget)
            self.nameLabel.setObjectName(u"nameLabel")
            self.nameLabel.setGeometry(QRect(20, 20, 241, 41))
            self.nameLabel.setText(row[1])
            font = QFont()
            font.setPointSize(16)
            self.nameLabel.setFont(font)

            self.varietyLabel = QLabel(self.plantWidget)
            self.varietyLabel.setObjectName(u"varietyLabel")
            self.varietyLabel.setGeometry(QRect(20, 60, 241, 31))
            font1 = QFont()
            font1.setFamily(u"Lato Light")
            font1.setPointSize(12)
            self.varietyLabel.setFont(font1)
            self.varietyLabel.setText(row[2])

            self.waterBtn = QPushButton(self.plantWidget)
            self.waterBtn.setObjectName(u"waterBtn")
            self.waterBtn.setGeometry(QRect(380, 29, 81, 41))
            self.waterBtn.setMinimumSize(QSize(81, 41))
            self.waterBtn.setMaximumSize(QSize(81, 41))
            self.waterBtn.setText("Water")
            self.waterBtn.setStyleSheet(u"*{\n"
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
            self.waterBtn.clicked.connect(lambda checked, id=row[0]: self.water(id))
            
            self.editBtn = QPushButton(self.plantWidget)
            self.editBtn.setObjectName(u"editBtn")
            self.editBtn.setGeometry(QRect(280, 30, 81, 41))
            self.editBtn.setMinimumSize(QSize(81, 41))
            self.editBtn.setMaximumSize(QSize(81, 41))
            self.editBtn.setText("Edit")
            self.editBtn.setStyleSheet(u"*{\n"
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

            self.verticalLayout_2.addWidget(self.plantWidget)
            
        conn.commit()

        conn.close()

    def addPlant(self):
        add = addPlantScreen()
        widget.addWidget(add)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def water(self, id):
        cursor, conn = connect()

        currDate = date.today()
        cursor.execute("UPDATE plant SET last_watered = ? WHERE pid = ?", (currDate, id))
        print(f'currDate: {currDate} with id: {id}')
        conn.commit()

        conn.close()

        add = homeScreen()
        widget.addWidget(add)
        widget.setCurrentIndex(widget.currentIndex()+1)

class addPlantScreen(QDialog):
    def __init__(self):
        super(addPlantScreen, self).__init__()
        loadUi("addPlantFrame.ui", self)
        

        self.backBtn.clicked.connect(self.back)
        self.submitBtn.clicked.connect(self.submit)

       
        self.waterField.setValidator(QIntValidator(1, 99))
         # set calendars default to current day
        self.lastWateredField.setDate(QDate.currentDate())
        self.bdayField.setDate(QDate.currentDate())


    def back(self):
        widget.setCurrentIndex(0)

    def submit(self):
        name = self.nameField.text()
        variety = self.varietyField.text()
        waterSched = self.waterField.text()
        lastWatered = self.lastWateredField.date().toPyDate()
        birthday = self.bdayField.date().toPyDate()
        
        if len(name) == 0 or len(variety) == 0 or len(waterSched) == 0:
            self.errorLabel.setText("Fields cannot be empty")
        else:
            print("attempting to submit data....")
            print(f"name: {name}, type: {type(name)}")
            print(f"variety: {variety}, type: {type(variety)}")
            print(f"waterSched: {waterSched}, type: {type(waterSched)}")
            print(f"lastWatered: {lastWatered}, type: {type(lastWatered)}")
            print(f"birthday: {birthday}, type: {type(birthday)}")

            conn = sqlite3.connect("plants.db")
            cursor = conn.cursor()

            cursor.execute("INSERT INTO plant (name, variety, watering_sched, last_watered, birthday) VALUES (?, ?, ?, ?, ?)", (name, variety, waterSched, lastWatered, birthday))
            conn.commit()
            print("SUCCESSFULLY ADDED TO DATABASE")
            conn.close()

            widget.setCurrentIndex(0)
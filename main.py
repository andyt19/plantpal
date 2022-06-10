from datetime import date, datetime
import sys
import sqlite3
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QDialog, QStackedWidget
from PyQt5.QtGui import QIntValidator, QFont
from PyQt5.QtCore import QDate, QSize, QRect

DB_NAME = "plants.db"

# helper function to connect to the SQL db
def connectdb():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    return cursor, conn

# helper function to navigate different UI screens
def goTo(screen):
    widget.addWidget(screen)
    toDel = widget.currentWidget()
    widget.setCurrentIndex(widget.currentIndex()+1)
    widget.removeWidget(toDel)

    return
    
class homeScreen(QDialog):
    def __init__(self):
        super(homeScreen, self).__init__()
        loadUi("homeFrame.ui", self)

        self.addPlantBtn.clicked.connect(self.add)

        self.loadPlants()
        self.loadNeedWater()

    # populate the needwater list
    def loadNeedWater(self):
        cursor, conn = connectdb()

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
                self.plantWidget.setStyleSheet(u"background-color: #b3d89a;")

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
                self.daysLabel.setGeometry(QRect(300, 70, 241, 31))
                self.daysLabel.setStyleSheet(u"font: \"Lato\";\n"
                    "font-size: 14px;\n"
                    "color: #6a3d27;\n"
                    "")
                if dayDiff == 1: 
                    self.daysLabel.setText(f"Last watered yesterday")
                else:
                    self.daysLabel.setText(f"Last watered {dayDiff} days ago")

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

        return

    # populate plant display list
    def loadPlants(self):
        cursor, conn = connectdb()

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
            
            self.viewBtn = QPushButton(self.plantWidget)
            self.viewBtn.setObjectName(u"viewBtn")
            self.viewBtn.setGeometry(QRect(280, 30, 81, 41))
            self.viewBtn.setMinimumSize(QSize(81, 41))
            self.viewBtn.setMaximumSize(QSize(81, 41))
            self.viewBtn.setText("View")
            self.viewBtn.setStyleSheet(u"*{\n"
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
            self.viewBtn.clicked.connect(lambda checked, id=row[0]: self.view(id))

            self.verticalLayout_2.addWidget(self.plantWidget)

        conn.close()

        return

    def add(self):
        add = addPlantScreen()
        goTo(add)

        return

    def water(self, id):
        cursor, conn = connectdb()

        currDate = date.today()
        cursor.execute("UPDATE plant SET last_watered = ? WHERE pid = ?", (currDate, id))

        conn.commit()

        conn.close()

        # update the homescreen
        add = homeScreen()
        goTo(add)

        return

    def view(self, id):
        view = viewPlantScreen(id)
        goTo(view)

        return

class viewPlantScreen(QDialog):
    def __init__(self, id):
        super(viewPlantScreen, self).__init__()
        self.id = str(id) # convert to str so we can compare it to pid in db
        
        loadUi("viewPlantFrame.ui", self)

        self.backBtn.clicked.connect(self.back)
        self.editBtn.clicked.connect(lambda checked, pid=self.id: self.edit(pid))

        cursor, conn = connectdb()

        cursor.execute("SELECT * from plant where pid = ?", (self.id,))
        row = cursor.fetchone()

        # setting labels
        self.nameLabel.setText(row[1])
        self.varietyLabel.setText(row[2])
        
        currDay = date.today()
        lastWatered = datetime.strptime(row[4], '%Y-%m-%d').date() # have to convert str into a date object
        dayDiff = (currDay - lastWatered).days
        if dayDiff == 0:
            tmpTxt = 'today'
        elif dayDiff == 1:
            tmpTxt = 'yesterday'
        else:
            tmpTxt = f'{dayDiff} days ago'
        self.daysLabel.setText(tmpTxt)

        self.schedDaysLabel.setText(f"{row[3]} days")
        self.birthdayLabel.setText(row[5])

        conn.close()

    def back(self):
        add = homeScreen()
        goTo(add)

        return

    def edit(self, id):
        edit = editPlantScreen(id)
        goTo(edit)

        return

class editPlantScreen(QDialog):
    def __init__(self, id):
        super(editPlantScreen, self).__init__()
        self.id = id

        loadUi("editPlantFrame.ui", self)

        self.backBtn.clicked.connect(lambda checked, pid=self.id: self.back(pid))
        self.updateBtn.clicked.connect(lambda checked, pid=self.id: self.update(pid))
        self.deleteBtn.clicked.connect(lambda checked, pid=self.id: self.deleteClicked(pid))

        cursor, conn = connectdb()
        cursor.execute("SELECT * from plant where pid = ?", (self.id,))
        row = cursor.fetchone()

        # inserting existing data into input fields
        self.nameField.setText(row[1])
        self.varietyField.setText(row[2])
        self.waterField.setValidator(QIntValidator(1, 99))
        self.waterField.setText(str(row[3]))

        lastWatered = datetime.strptime(row[4], '%Y-%m-%d').date()
        self.lastWateredField.setDate(lastWatered)
        birthday = datetime.strptime(row[5], '%Y-%m-%d').date()
        self.bdayField.setDate(birthday)

        conn.close()
    
    def back(self, id):
        view = viewPlantScreen(id)
        goTo(view)

        return

    def update(self, id):
        name = self.nameField.text()
        variety = self.varietyField.text()
        waterSched = self.waterField.text()
        lastWatered = self.lastWateredField.date().toPyDate()
        birthday = self.bdayField.date().toPyDate()
        
        if len(variety) == 0:
            variety = 'Unknown'
        if len(name) == 0 or len(waterSched) == 0:
            self.errorLabel.setText('Name/Schedule cannot be empty')
        elif int(waterSched) <= 0:
            self.errorLabel.setText('Watering schedule cannot be 0')
        elif lastWatered > date.today() or birthday > date.today():
            self.errorLabel.setText('Day cannot be in the future')
        else:
            cursor, conn = connectdb()

            cursor.execute('''  UPDATE plant 
                                SET name = ?, 
                                    variety = ?, 
                                    watering_sched = ?, 
                                    last_watered = ?, 
                                    birthday = ?
                                WHERE pid = ?''', (name, variety, waterSched, lastWatered, birthday, id))
            conn.commit()

            conn.close()

            self.back(id)

        return

    def deleteClicked(self, id):
        cursor, conn = connectdb()

        cursor.execute('''DELETE FROM plant where pid = ?''', (id,))
        conn.commit()
        conn.close()

        # return to home screen
        add = homeScreen()
        goTo(add)

        return


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
        add = homeScreen()
        goTo(add)

        return

    def submit(self):
        name = self.nameField.text()
        variety = self.varietyField.text()
        waterSched = self.waterField.text()
        lastWatered = self.lastWateredField.date().toPyDate()
        birthday = self.bdayField.date().toPyDate()
        

        if len(variety) == 0:
            variety = 'Unknown'
        if len(name) == 0 or len(waterSched) == 0:
            self.errorLabel.setText('Name/Schedule cannot be empty')
        elif int(waterSched) <= 0:
            self.errorLabel.setText('Watering schedule cannot be 0')
        elif lastWatered > date.today() or birthday > date.today():
            self.errorLabel.setText('Day cannot be in the future')
        else:
            conn = sqlite3.connect("plants.db")
            cursor = conn.cursor()

            cursor.execute('''  INSERT INTO plant 
                                (name, variety, watering_sched, last_watered, birthday)
                                VALUES 
                                (?, ?, ?, ?, ?)''', (name, variety, waterSched, lastWatered, birthday))
            conn.commit()

            conn.close()

            self.back()

        return

app = QApplication(sys.argv)
home = homeScreen()
widget = QStackedWidget()

widget.addWidget(home)
widget.setFixedWidth(600)
widget.setFixedHeight(800)

widget.show()

sys.exit(app.exec())

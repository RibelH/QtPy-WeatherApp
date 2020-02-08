from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import sys



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("QtPyWeather")
        self.setWindowIcon(QtGui.QIcon("C:/Users/Robert/Pictures/weather.png"))
        list = self.info()

        #Label creation
        #TODO: Temperatur Anzeige mit Farbe
        label = QLabel(list[0]+"°C")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        label.setStyleSheet("color:blue; font-size:14px")

        #Toolbar creation
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #Button creation
        button_action = QAction(QIcon("bug.png"),"My button", self)
        button_action.setStatusTip("This is my button")
        button_action.triggered.connect(lambda: self.onMyToolBarButtonClick("Hallo"))
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        #TODO: Refresh Button for new Temperature
        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self,s):
        print("click",s)

    def info(self):

        #Get weather data
        city = "Kreuzlingen"
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(city)
        res = requests.get(url)
        data = res.json()


        #Store weather Data
        temp = str(data["main"]["temp"])
        desc = data["weather"][0]["description"]
        result = "Die Temperatur in {} beträgt:\n".format(city) + (28 + len(city)) * "-"

        return temp, desc, result


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
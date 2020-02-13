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
        #Resizing window
        self.resize(400,200)


        #Label Title creation
        label_t = QLabel(list[2])
        label_t.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label_t.setStyleSheet("font-size:20px")
        #Label creation
        #TODO: Temperatur Anzeige mit Farbe
        label = QLabel(list[0]+"°C")
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(label)
        label.setStyleSheet("color:black; font-size:20px; background-color:white")
        #Label Description creation
        desc_label = QLabel(list[1])
        desc_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        #self.setCentralWidget(desc_label)
        desc_label.setStyleSheet("color: white; background-color:black; font-size:20px")


        #Layout Creation
        layout = QVBoxLayout()
        #Add Widget to Layout
        layout.addWidget(label_t)
        layout.addWidget(label)
        layout.addWidget(desc_label)
        #Set layout for widget to show in Window
        widget = QLabel()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


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
        #Separtor creation
        toolbar.addSeparator()
        #Button2 creation
        # TODO: Refresh Button for new Temperature
        button_action2 = QAction(QIcon("C:/Gui/arrow-circle-double"), "My button2", self)
        button_action2.setStatusTip("just refreshed")
        button_action2.triggered.connect(lambda: self.onMyToolBarButtonClick("Refresh"))
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        #Speparator
        toolbar.addSeparator()
        #Adding Widget to Toolbar
        toolbar.addWidget(QLabel("Hello"))
        toolbar.addWidget(QCheckBox())

        self.setStatusBar(QStatusBar(self))


        #Menu creation
        menu = self.menuBar()

        file_menu = menu.addMenu("&File")
        file_menu.addAction(button_action)
        file_menu.addSeparator()

        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)




    def onMyToolBarButtonClick(self,s):
        print("click",s)

    def contextMenuEvent(self, event):
        print("Context menu event!")
        super(MainWindow, self).contextMenuEvent(event)

    def info(self):

        #Get weather data
        city = "Kreuzlingen"
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(city)
        res = requests.get(url)
        data = res.json()


        #Store weather Data
        temp = str(data["main"]["temp"])
        desc = data["weather"][0]["description"]
        result = "Die Temperatur in {} beträgt:\n".format(city)

        return temp, desc, result


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
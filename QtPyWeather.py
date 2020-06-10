from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import sys
#TODO: Weather Night/Day Difference
#TODO: Feature (Change City)



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("QtPyWeatherAPP")
        self.setWindowIcon(QtGui.QIcon("C:/Users/Robert/Pictures/weather.png"))

        #Default City
        self.city = "Kreuzlingen"

        list = self.info(self.city)

        #Resizing window
        self.resize(400,400)

        #Button to change City
        button_change_city = QPushButton("Change City",self)
        button_change_city.clicked.connect(lambda:label.setText(self.update_temp(self.textbox.text())))
        button_change_city.clicked.connect(lambda: desc_label.setText(self.update_desc(self.textbox.text())))
        button_change_city.clicked.connect(lambda: label_t.setText(self.update_title(self.textbox.text())))

        #Textbox creation
        self.textbox = QLineEdit(self)
        self.textbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.textbox.resize(280,40)


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

        #Label Description Image
        label_img = QLabel()
        image = QPixmap(self.img_d(list[1]))
        label_img.setPixmap(image)
        label_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        label_img.setStyleSheet("background-color:#78ECF6")



        #Layout Creation
        layout = QVBoxLayout()
        #Add Widget to Layout
        layout.addWidget(self.textbox)
        layout.addWidget(button_change_city)
        layout.addWidget(label_t)
        layout.addWidget(label_img)
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
        Refresh_button = QAction(QIcon("C:/Gui/arrow-circle-double"), "Refresh Stats", self)
        Refresh_button.setStatusTip("Refresh?")
        Refresh_button.triggered.connect(lambda: label.setText(self.update_temp(self.city)))
        Refresh_button.triggered.connect(lambda: desc_label.setText(self.update_desc(self.city)))
        Refresh_button.setCheckable(False)
        toolbar.addAction(Refresh_button)
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
        file_submenu.addAction(Refresh_button)

    def update_title(self, cit):
        l = self.info(cit)
        new_info = l[2]
        return new_info

    #Functino to update Temperature
    def update_temp(self, cit):
        l = self.info(cit)
        new_info = l[0]+"°C"
        return new_info

    #Function to update Description
    def update_desc(self, cit):
        l = self.info(cit)
        new_info = l[1]
        return new_info

    #ToolBarButton Function
    def onMyToolBarButtonClick(self,s):
        print("click",s)

    #ContextMenu Function
    def contextMenuEvent(self, event):
        print("Context menu event!")
        super(MainWindow, self).contextMenuEvent(event)

    #Function to get Description Image
    def img_d(self, descrip):
        images = ["c:\Gui\cloudy_sun.png", "c:\Gui\sun.png", "c:\Gui\\rain.png"]
        if "rain" in descrip:
            return images[2]
        elif "clear sky" in descrip:
            return images[1]
        elif "cloud" in descrip:
            return images[0]
        else:
            return images[0]

    #Function to get Weather Data
    def info(self, cit):
        #Get weather data
        try:
            city = cit
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(city)
            res = requests.get(url)
            data = res.json()

            #Store weather Data
            temp = str(data["main"]["temp"])
            desc = data["weather"][0]["description"]
            result = "Die Temperatur in {} beträgt:\n".format(city)

            return temp, desc, result
        except KeyError:
            city = "Kreuzlingen"
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(
                city)
            res = requests.get(url)
            data = res.json()

            # Store weather Data
            temp = str(data["main"]["temp"])
            desc = data["weather"][0]["description"]
            result = "Die Temperatur in {} beträgt:\n".format(city)

            return temp, desc, result



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
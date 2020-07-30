from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import requests
import sys
#TODO: Weather Night/Day Difference




class MainWindow(QMainWindow):
    """Initializing MainWindow and all functions needed"""
#-----------------------__INIT__.START----------------------#
    city = ""

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        global city
        #Windowtitle
        self.setWindowTitle("QtPyWeatherAPP")
        #WindowIcon
        self.setWindowIcon(QtGui.QIcon("C:/Users/Robert/Pictures/weather.png"))
        #Stylesheet stored in variable
        self.stylesheet = """
        
        QLineEdit{
            font-size:20px;
            height:40px;
            width:100px;
        }
        QPushButton {
            font: bold; 
            background-color: black; 
            font-size:12px; 
            height:40px;
            width:100px; 
            color:white;
            border: 2px solid #646262;
        }
        QPushButton:hover {
            background-color: #C0C0C0;
            color: black;
        }
        QPushButton:pressed {
            background-color: #6C6C6C;
            color: white;
        }
        """
        #Default City
        city =""

        #Stores weather data in list
        list = self.info(city)

        #Resizing window
        self.resize(400,500)

        #Button to change City
        self.button_change_city = QPushButton("Change City",self)
        self.button_change_city.clicked.connect(lambda:self.label.setText(self.update_temp(self.textbox.text())))
        self.button_change_city.clicked.connect(lambda: self.desc_label.setText(self.update_desc(self.textbox.text())))
        self.button_change_city.clicked.connect(lambda: self.label_t.setText(self.update_title(self.textbox.text())))
        self.button_change_city.clicked.connect(lambda: self.update_city(self.textbox.text()))
        #self.button_change_city.clicked.connect(lambda: self.textbox.setText(""))

        #Textbox creation
        self.textbox = QLineEdit(self)
        self.textbox.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.textbox.resize(280,40)


        #self.label Title creation
        self.label_t = QLabel(list[2])
        self.label_t.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_t.setStyleSheet("font-size:20px; background-color:#a5f8ff")

        #self.label creation
        #TODO: Temperatur Anzeige mit Farbe
        self.label = QLabel(list[0]+"°C")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.label)
        self.label.setStyleSheet("color:black; font-size:20px; background-color:white")

        #self.label Description creation
        self.desc_label = QLabel(list[1])
        self.desc_label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.desc_label.setStyleSheet("color: white; background-color:black; font-size:20px")

        #self.label Description Image
        self.label_img = QLabel()
        image = QPixmap(self.img_d(list[1]))
        self.label_img.setPixmap(image)
        self.label_img.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.label_img.setStyleSheet("background-color:#78ECF6")



        #Layout Creation
        layout = QVBoxLayout()

        #Add Widget to Layout
        layout.addWidget(self.textbox)
        layout.addWidget(self.button_change_city)
        layout.addWidget(self.label_t)
        layout.addWidget(self.label_img)
        layout.addWidget(self.label)
        layout.addWidget(self.desc_label)
         

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
        Refresh_button.triggered.connect(lambda: self.label.setText(self.update_temp(city)))
        Refresh_button.triggered.connect(lambda: self.desc_label.setText(self.update_desc(city)))
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

        #Submenu creation
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(Refresh_button)

        #Setting Stylesheet
        app.setStyleSheet(self.stylesheet)
    #-------------------------__INIT__.END-------------------------#

    #Function to update Title
    def update_title(self, cit):
        l = self.info(cit)
        new_info = l[2]
        return new_info

    #Function to update Temperature
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
    def info(self, cit = "Kreuzlingen"):
        #Get weather data with Exceptionhandling
        try:
            #Try to get DATA with cit variable
            city = cit
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(city)
            res = requests.get(url)
            data = res.json()

            #Store weather Data
            temp = str(data["main"]["temp"])
            desc = self.capitalizing(data["weather"][0]["description"])
            result = self.capitalizing("{}".format(city))

            return temp, desc, result
        except:
            #If cit variable gives KeyError get data of Default City
            city = "Kreuzlingen"
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=ac7c75b9937a495021393024d0a90c44&units=metric".format(
                city)
            res = requests.get(url)
            data = res.json()

            # Store weather Data
            temp = str(data["main"]["temp"])
            desc = self.capitalizing(data["weather"][0]["description"])
            result = self.capitalizing("{}".format(city))
            return temp, desc, result

    #Function updates current city value
    def update_city(self, cit):
        global city
        city = cit

    #Capitalizing Output Strings
    def capitalizing(self,long_string):
        """Capitalizing all words of the given string"""
        words = long_string.split()
        if len(words)>1:
            cap_words = [word.capitalize() for word in words if len(words) > 1]
            s = " ".join(cap_words)
            return s
        else:
            s = long_string.capitalize()
            return s


#--------------------------------------------------------------------------------------#
#initializing window
app = QApplication(sys.argv)
window = MainWindow()

#Displaying Window
window.show()

#Documentation -----TEST------
print(window.__doc__)
print(window.capitalizing.__doc__)

app.exec_()

#----------------------------------------------------------------------------------------#
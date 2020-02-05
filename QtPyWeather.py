from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys



class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("QtPyWeather")
        self.setWindowIcon(QtGui.QIcon("C:/Users/Robert/Pictures/weather.png"))

        #Label creation
        label = QLabel("Weather")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)

        #Toolbar creation
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        #Button creation
        button_action = QAction(QIcon("bug.png"),"My button", self)
        button_action.setStatusTip("This is my button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self,s):
        print("click",s)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
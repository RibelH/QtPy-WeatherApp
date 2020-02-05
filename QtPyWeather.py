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

        label = QLabel("Weather")




        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
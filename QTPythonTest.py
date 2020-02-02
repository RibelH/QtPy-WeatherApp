import sys
import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
#WindowSetting
w = QWidget()
w.setGeometry(100,100,500,500)
w.setWindowTitle("My first QtTest")
w.setWindowIcon(QIcon("C:/Users/Robert/Pictures/weather.png"))

w.show()

sys.exit(app.exec_())
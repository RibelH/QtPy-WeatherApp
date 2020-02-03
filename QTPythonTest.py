import sys
import PyQt5
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QObject

def MainWindow():
    app = QApplication(sys.argv)
    #WindowSetting
    w =QWidget()
    w.setGeometry(100,100,500,500)
    w.setWindowTitle("My first QtTest")
    ic = "C:/Users/Robert/Pictures/weather.png"
    w.setWindowIcon(QIcon(ic))
    #Label
    label = QLabel(w)
    label.setText("Hello")
    label.move(50,20)
    #Button
    b1 = QPushButton(w,text= "Button 1" )
    # b1.setText("Button 1")
    b1.move(100,100)

    #Button signal linking
    b1.clicked.connect(lambda: b1_clicked("B1"))

    w.show()
    sys.exit(app.exec_())

def b1_clicked(x):
    print(x)

if __name__ =='__main__':
    MainWindow()
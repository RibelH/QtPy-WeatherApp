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
    stylesheet = """
        QPushButton {
            font: bold; 
            background-color: black; 
            font-size:12px; 
            height:40px;
            width:100px; 
            color:white;
            border: 2px solid #646262
        }
        QPushButton:hover {
            background-color: #C0C0C0;
            color: black;
        }
        QPushButton:pressed {
            background-color: #6C6C6C;
            color: white
        }
    """
    app.setStyleSheet(stylesheet)
    #Label creating
    label = QLabel(w)
    label.setText("Hello")
    label.move(50,20)

    #Button
    b1 = QPushButton(w, text="Button 1")
    b1.move(100, 100)
    b1.setObjectName("b1_button")

    b2 = QPushButton(w, text="Button 2")
    b2.move(300,100)



    #Button signal linking
    b1.clicked.connect(lambda: b1_clicked("You just clicked Button 1"))

    w.show()
    sys.exit(app.exec_())

def b1_clicked(x):
    print(x)

if __name__ =='__main__':
    MainWindow()
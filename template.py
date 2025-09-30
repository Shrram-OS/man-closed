from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Man")

        self.showFullScreen()
        
        self.setStyleSheet(open("static/css/main/pass.css").read())

       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
)
import sys
from main_menu import MainMenu

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(0, 0, 1920, 1080)
        self.resize(1920, 1080)
        self.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setWindowTitle("Main")
        self.setMenuBar(None)
        self.setStyleSheet(open("static/css/main/main.css").read())

        
        
        self.current_screen = None
        
        self.show_screen(MainMenu)
    
    def show_screen(self, screen_class, *args, **kwargs):
        if self.current_screen is not None:
            self.current_screen.deleteLater()


        self.current_screen = screen_class(self, *args, **kwargs)
        self.setCentralWidget(self.current_screen)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

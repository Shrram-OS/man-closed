from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 

import sys
# from emul.pascal import Pascal
# from emul.fon import Fon_Neyman
# from emul.lisp import Lisp
# from emul.python import Python


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Man")

        self.showFullScreen()
        
        self.setStyleSheet(open("static/css/main/bg.css").read())

        BUTTON_W, BUTTON_H = 360, 80
        GAP = 30
        START_Y, START_X = 400, 400

        BUTTON_W, BUTTON_H = 360, 80
        GAP = 30
        START_Y, START_X = 400, 400

        self.new_game_button = QPushButton("New Game", self)
        self.new_game_button.setGeometry(START_X, START_Y, BUTTON_W, BUTTON_H)

        self.continue_button = QPushButton("Continue", self)
        self.continue_button.setGeometry(START_X, START_Y + GAP + (BUTTON_H * 1), BUTTON_W, BUTTON_H)

        self.choose_epoch_button = QPushButton("Choose Epoch", self)
        self.choose_epoch_button.setGeometry(START_X, START_Y + GAP + (BUTTON_H * 2), BUTTON_W, BUTTON_H)

        self.about_project_button = QPushButton("About Project", self)
        self.about_project_button.setGeometry(START_X, START_Y + GAP + (BUTTON_H * 3), BUTTON_W, BUTTON_H)

        self.exit_button = QPushButton("Exit", self)
        self.exit_button.setGeometry(START_X, START_Y + GAP + (BUTTON_H * 4), BUTTON_W, BUTTON_H)

        # self.exit_button.setGeometry()
    #     self.pascal_button = QPushButton(self)
    #     self.pascal_button.move(50, 50)
    #     self.pascal_button.setStyleSheet(open("static/css/main/pascal.css").read())
    #     self.pascal_button.setText("Pascalina")
    #     self.pascal_button.clicked.connect(self.pascal)

    #     self.fon_button = QPushButton(self)
    #     self.fon_button.move(200, 50)
    #     self.fon_button.setStyleSheet(open("static/css/main/fon_neyman.css").read())
    #     self.fon_button.setText("Fon Neyman")
    #     self.fon_button.clicked.connect(self.fon)

    #     self.lisp_button = QPushButton(self)
    #     self.lisp_button.move(350, 50)
    #     self.lisp_button.setStyleSheet(open("static/css/main/lisp.css").read())
    #     self.lisp_button.setText("Lisp")
    #     self.lisp_button.clicked.connect(self.lisp)

    #     self.python_button = QPushButton(self)
    #     self.python_button.move(500, 50)
    #     self.python_button.setStyleSheet(open("static/css/main/python.css").read())
    #     self.python_button.setText("Python")
    #     self.python_button.clicked.connect(self.python)   
    
    # def python(self):
    #     self.python = Python()
    #     self.python.show()

    # def fon(self):
    #     self.fon = Fon_Neyman()
    #     self.fon.show()

    # def pascal(self):
    #     self.pascal = Pascal()
    #     self.pascal.show()
    
    # def lisp(self):
    #     self.lisp = Lisp()
    #     self.lisp.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
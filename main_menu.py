from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
)
from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from level import LevelScreen


class MainMenu(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        self.setGeometry(0, 0, 1920, 1080)
        self.resize(1920, 1080)
        self.move(0, 0)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.setWindowTitle("Main")
        # self.setObjectName("mainmenu")

        self.setStyleSheet(open("static/css/main/main_menu.css").read())
        

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(300, 120, 300, 50)  # отступы слева, сверху, справа, снизу
        main_layout.setSpacing(30)  # расстояние между элементами


        self.text = QLabel("...")
        self.text.setAlignment(Qt.AlignHCenter)
        self.text.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        main_layout.addWidget(self.text)


        self.continue_button = QPushButton("Continue")
        self.continue_button.setFixedSize(360, 80)
        self.continue_button.clicked.connect(self.on_continue)
        main_layout.addWidget(self.continue_button)

        self.new_game_button = QPushButton("New Game")
        self.new_game_button.setFixedSize(360, 80)
        main_layout.addWidget(self.new_game_button)

        self.choose_epoch_button = QPushButton("Choose Epoch")
        self.choose_epoch_button.setFixedSize(360, 80)
        main_layout.addWidget(self.choose_epoch_button)

        self.about_project_button = QPushButton("About Project")
        self.about_project_button.setFixedSize(360, 80)
        main_layout.addWidget(self.about_project_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.setFixedSize(360, 80)
        self.exit_button.clicked.connect(sys.exit)
        main_layout.addWidget(self.exit_button)


        main_layout.addStretch()

        # self.dots = []
        # self.anims = []

        # buttons = [self.continue_button, self.new_game_button, self.choose_epoch_button,
        #         self.about_project_button, self.exit_button]
        
        # DOT_SIZE = 8
        
        # dx = BUTTON_W - DOT_SIZE
        # dy = BUTTON_H - DOT_SIZE
        # perimeter = 2*(dx + dy)

        # t0 = 0.0
        # t1 = dx / perimeter           # верхняя сторона
        # t2 = (dx + dy) / perimeter    # правая сторона
        # t3 = (2*dx + dy) / perimeter  # нижняя сторона
        # t4 = 1.0                       # левая сторона



        # for btn in buttons:
        #     dot = QWidget(self)
        #     dot.setFixedSize(DOT_SIZE, DOT_SIZE)
        #     dot.setStyleSheet("background:white; border-radius:3px;")
            
        #     effect = QtWidgets.QGraphicsDropShadowEffect()
        #     effect.setBlurRadius(60)
        #     effect.setColor(QtGui.QColor(255,255,255))
        #     effect.setOffset(0)
        #     dot.setGraphicsEffect(effect)
            
        #     START_X, START_Y = btn.x(), btn.y()
        #     BUTTON_W, BUTTON_H = btn.width(), btn.height()
        #     anim = QPropertyAnimation(dot, b"geometry", self)
        #     anim.setDuration(4000)
        #     anim.setLoopCount(-1)
        #     # anim.setKeyValueAt(0.0, QRect(START_X, START_Y, DOT_SIZE, DOT_SIZE))
        #     # anim.setKeyValueAt(0.25, QRect(START_X + BUTTON_W - DOT_SIZE, START_Y, DOT_SIZE, DOT_SIZE))
        #     # anim.setKeyValueAt(0.5, QRect(START_X + BUTTON_W - DOT_SIZE, START_Y + BUTTON_H - DOT_SIZE, DOT_SIZE, DOT_SIZE))
        #     # anim.setKeyValueAt(0.75, QRect(START_X, START_Y + BUTTON_H - DOT_SIZE, DOT_SIZE, DOT_SIZE))
        #     # anim.setKeyValueAt(1.0, QRect(START_X, START_Y, DOT_SIZE, DOT_SIZE))
        #     anim.setKeyValueAt(t0, QRect(START_X, START_Y, DOT_SIZE, DOT_SIZE))                  # верх левый
        #     anim.setKeyValueAt(t1, QRect(START_X + dx, START_Y, DOT_SIZE, DOT_SIZE))            # верх правый
        #     anim.setKeyValueAt(t2, QRect(START_X + dx, START_Y + dy, DOT_SIZE, DOT_SIZE))       # низ правый
        #     anim.setKeyValueAt(t3, QRect(START_X, START_Y + dy, DOT_SIZE, DOT_SIZE))            # низ левый
        #     anim.setKeyValueAt(t4, QRect(START_X, START_Y, DOT_SIZE, DOT_SIZE))                  # верх левый
        #     anim.start()
            
        #     self.dots.append(dot)
        #     self.anims.append(anim)
        

    def on_continue(self):
        self.main_window.show_screen(LevelScreen, 0)

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainMenu(None)
    win.show()
    sys.exit(app.exec_())

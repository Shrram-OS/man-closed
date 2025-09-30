from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import * 
from PyQt5 import QtWidgets
from PyQt5.QtGui import * 
from PyQt5.QtCore import Qt
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtCore
import sys


class WinHud(QWidget):
    # def __init__(self, sub):
    def __init__(self):
        super().__init__()
        # self.sub = sub

        self.setWindowFlag(Qt.FramelessWindowHint)


        

        # главный vertical layout — контент под HUD
        self.main = QVBoxLayout(self)
        self.main.setContentsMargins(0, 0, 0, 0)
        self.main.setSpacing(0)

        # место куда наследники будут добавлять контент (и именно туда content'ы)
        self.content_layout = QVBoxLayout()
        self.content_layout.setContentsMargins(0, 0, 0, 0)
        self.content_layout.setSpacing(0)
        self.main.addLayout(self.content_layout)

        # карта parent_widget -> (hud_widget, reposition_callable)
        self._overlay_map = {}


        self.oldPos = None 

    def create_overlay_hud(self, parent_widget, margin=0):
        """
        Создаёт HUD как дочерний виджет parent_widget и прижимает его
        к правому верхнему углу parent_widget. margin — расстояние от краёв.
        """
        hud = QWidget(parent_widget)
        hud.setAttribute(Qt.WA_TranslucentBackground)  # если хочешь прозрачность
        hud_layout = QHBoxLayout(hud)
        hud_layout.setContentsMargins(0, 0, 0, 0)
        hud_layout.setSpacing(0)

        reloadBtn = QPushButton("↻")
        reloadBtn.setFixedSize(35, 35)
        reloadBtn.setStyleSheet(open("static/css/hud/reload_button.css").read())
        reloadBtn.clicked.connect(self.reboot)
        hud_layout.addWidget(reloadBtn)

        closeBtn = QPushButton("✖")
        closeBtn.setFixedSize(35, 35)
        closeBtn.setStyleSheet(open("static/css/hud/close_button.css").read())
        closeBtn.clicked.connect(self.close)
        hud_layout.addWidget(closeBtn)

        hud_layout.addStretch()
        hud.adjustSize()

        def reposition():
            pw = parent_widget.width()
            hw = hud.width()
            # прижать к правому верхнему углу с указанным margin
            hud.move(max(0, pw - hw - margin), margin)
            hud.raise_()

        reposition()
        parent_widget.installEventFilter(self)
        self._overlay_map[parent_widget] = (hud, reposition)
        return hud



    # def _on_close_clicked(self):
    #     w = self.sub if self.sub else self.window() 
    #     if isinstance(w, QMdiSubWindow):
    #         w.close()
    #     else:
    #         self.close()


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.oldPos:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = None




    def reboot(self):
        # Define the func in child class // А если не на пендосском, то функцию ребута нужно отдельно делать в каждом классе. Не забывая обнулять значения и ресетать gui
        pass

    
      

       

class TestHud(WinHud):
    def __init__(self):
        super().__init__(None)

        self.setWindowTitle("Man")

        # self.showFullScreen()
        
        # self.setStyleSheet(open("static/css/main/pass.css").read())
        WINDOW_W, WINDOW_H = 700, 400
        self.setGeometry((1920-WINDOW_W)//2, (1080-WINDOW_H)//2, WINDOW_W, WINDOW_H)

    def reboot(self):
        print(22)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = TestHud()
    win.show()
    sys.exit(app.exec_())
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import QRect
from emulators.hud import WinHud
from PyQt5.QtCore import Qt

class PascalineEmulator(WinHud):
    def __init__(self, answer_map, update_task):
        super().__init__()
        self.answer_map = answer_map
        self.update_task = update_task

        self.setStyleSheet("static/css/emuls/pascal.css")  


        self.setWindowTitle("Pascalina")
        self.total = 0


       

        content = QWidget()
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)

        self.image_label = QLabel(content)
        pixmap = QPixmap("static/img/pascal.png")  
        self.image_label.setPixmap(pixmap)
        self.image_label.setFixedSize(pixmap.size())
        content_layout.addWidget(self.image_label)

        content.setFixedSize(pixmap.size())

        self.content_layout.addWidget(content)


        self.create_overlay_hud(content, margin=0)
        
        self.image_label.mousePressEvent = self.on_image_click


        

        self.font = QFont()
        self.font.setPointSize(14)

        self.text_hs = QLabel(self.image_label)
        self.text_hs.setFont(self.font)
        self.text_hs.move(74, 20)

        self.text_ts = QLabel(self.image_label)
        self.text_ts.setFont(self.font)
        self.text_ts.move(243, 20)

        self.text_s = QLabel(self.image_label)
        self.text_s.setFont(self.font)
        self.text_s.move(402, 20)

        self.text_h = QLabel(self.image_label)
        self.text_h.setFont(self.font)
        self.text_h.move(567, 20)

        self.text_t = QLabel(self.image_label)
        self.text_t.setFont(self.font)
        self.text_t.move(730, 20)

        self.text_u = QLabel(self.image_label)
        self.text_u.setFont(self.font)
        self.text_u.move(896, 20)

        # "Невидимые кнопки" области
        self.button_rectangles = [
            QRect(1, 136, 166, 186),
            QRect(167, 136, 166, 186),
            QRect(333, 136, 166, 186),
            QRect(499, 136, 166, 186),
            QRect(665, 136, 166, 186),
            QRect(825, 136, 166, 186),
        ]

        self.hud()

    def hud(self):
        self.text_hs.setText(str((self.total // 100000) % 10))
        self.text_ts.setText(str((self.total // 10000) % 10))
        self.text_s.setText(str((self.total // 1000) % 10))
        self.text_h.setText(str((self.total // 100) % 10))
        self.text_t.setText(str((self.total // 10) % 10))
        self.text_u.setText(str(self.total % 10))

    def reboot(self):
        self.total = 0
        self.hud()


    def on_image_click(self, event):
        if event.button() == Qt.LeftButton:
            for i, rect in enumerate(self.button_rectangles[::-1]):
                if rect.contains(event.x(), event.y()):
                    self.total += 1 * 10**i
                    self.hud()
                    if self.total in self.answer_map:
                        self.update_task(self.answer_map[self.total])
                    return  

            self.oldPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PascalineEmulator()
    window.show()
    sys.exit(app.exec_())

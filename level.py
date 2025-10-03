from PyQt5.QtCore import Qt, QPropertyAnimation, QRect
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel, QVBoxLayout
)
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QMdiSubWindow
import sys

from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
)
from config import config
class LevelScreen(QWidget):
    def __init__(self, main_window, level_id):
        super().__init__()

        self.setObjectName("LevelScreen")
        self.setStyleSheet(open("static/css/main/level.css").read())
        self.main_window = main_window
        self.level_id = level_id

        self.resize(1920, 1080)
        self.move(0, 0)

        self.layout = QVBoxLayout()
        self.config = config[level_id]



        # Заголовок
        heading = QLabel(f"{self.config['title']}")
        heading.setAlignment(Qt.AlignHCenter)
        heading.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        heading.setObjectName("heading")
        self.layout.addWidget(heading, stretch=1)

        

        # Эпоха
        era_label = QLabel(f"{self.config["era"]}")
        era_label.setAlignment(Qt.AlignCenter)
        era_label.setStyleSheet("font-size: 20px; color: gray;")
        era_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(era_label, stretch=0)

        # Год
        era_label = QLabel(f"{self.config["year"]}")
        era_label.setAlignment(Qt.AlignCenter)
        era_label.setStyleSheet("font-size: 18px; color: gray;")
        era_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.layout.addWidget(era_label, stretch=0)


        # Конт для текста и задач
        central_layout = QHBoxLayout()
        central_layout.setSpacing(20)
        
        
        # Текст
        description = QLabel(f"{self.config["description"]}")
        description.setWordWrap(True)
        description.setObjectName("description")
        description.setContentsMargins(10, 0, 0, 0)
        description.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        central_layout.addWidget(description, stretch=3)


        # Задачи

        self.answer_map = {}

        tasks_container = QVBoxLayout()
        tasks_container.setSpacing(10)

        self.tasks_id = {}   

        self.done = set()

        self.tasks = self.config["tasks"]
        
        for task in self.tasks:
            task_text = task["text"]

            self.answer_map.update(task["a_id"])  


            task_button = QPushButton(task_text)
            task_button.setFixedHeight(100)

            self.tasks_id[task["id"]] = task_button


            tasks_container.addWidget(task_button)
        tasks_container.addStretch()
        
        central_layout.addLayout(tasks_container, stretch=1)

        
        self.layout.addLayout(central_layout)
        

        if self.config["emulator"]:
            btn_emulator = QPushButton("Открыть эмулятор")
            btn_emulator.clicked.connect(self.show_emul)
            btn_emulator.setFixedHeight(50)
            self.layout.addWidget(btn_emulator, stretch=1)

        self.btn_next = QPushButton("Следующий уровень")
        self.btn_next.setFixedHeight(50)
        self.btn_next.clicked.connect(self.go_next)
        self.layout.addWidget(self.btn_next, stretch=1)

        self.setLayout(self.layout)

        self.emul_widget = None  


    def single_shot(self):
        self.btn_next.setStyleSheet("QPushButton {color: white}; QPushButton:hover {color: white}")
        self.btn_next.setText("Следующий уровень")


    def go_next(self):
        if self.all_tasks_done():
            next_level = self.level_id + 1
            self.main_window.show_screen(LevelScreen, next_level)

        else:
            self.btn_next.setText("Не все задачи выполнены")
            self.btn_next.setStyleSheet("QPushButton {color: red}; QPushButton:hover {color:red}")
            QTimer.singleShot(3000, self.single_shot)
            


    def all_tasks_done(self):

        return len(self.done) == len(self.tasks)

    def show_emul(self):
        if self.emul_widget is None:


            self.emul_widget = self.config["emulator"](self.answer_map, self.update_task)
            self.emul_widget.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)

            self.emul_widget.show()

        else:
            # если уже создан – просто показать
            self.emul_widget.show()

    

    def update_task(self, task_id):
        task_button = self.tasks_id[task_id]    
        task_button.setStyleSheet("QPushButton { background-color: #1A2E3B; border: 2px solid #00CCFF; color: #00CCFF}")

        self.done.add(task_id)

    





if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LevelScreen(None, 0)
    win.show()
    sys.exit(app.exec_())

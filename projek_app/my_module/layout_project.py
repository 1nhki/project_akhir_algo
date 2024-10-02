from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QListWidget, QRadioButton, QLineEdit\
                             , QVBoxLayout, QHBoxLayout, QMenu 
                             )
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import (Qt, QSize)
from .gui import Button

class home():
    def __init__(self) -> None:   
        self.list_program = ["high and low", "roulette", "fish"]
        self.home_label = QLabel("WELCOME")
        self.abcd = list()
        for i in range(len(self.list_program)):
            self.abcd.append(QRadioButton())
            self.abcd[i].setText(self.list_program[i])

        self.button_start = Button((200, 100), "start")
            
        for i in range(len(self.abcd)) :
            self.abcd[i].setStyleSheet("font : 30px Arial;"
                                """QRadioButton::indicator {
                                image: url (asset/unchecked_box.png)
                                    }""")
            
        """     qpixmap      """
        img_home = QPixmap("asset/home_14782571.png")
        img_home = img_home.scaled(90, 90)
        self.home_label.setFixedSize(150,150)
        self.home_label.setPixmap(img_home)
        self.home_label.setStyleSheet("border : 2px solid cyan;"
                                "border-radius : 20px;"
                                "background-color : white")
        self.home_label.setAlignment(Qt.AlignCenter)
            
        """layout"""
        self.home_layout = QVBoxLayout()
        self.home_layout.addWidget(self.home_label, alignment=Qt.AlignCenter)
        for i in range(len(self.abcd)) :
            self.home_layout.addWidget(self.abcd[i], alignment=Qt.AlignCenter)
        self.home_layout.addWidget(self.button_start, alignment=Qt.AlignCenter)


class high_low():
    def __init__(self) -> None:
        self.label_HIGH_LOW = QListWidget()
        self.label_HIGH_LOW.setStyleSheet("background-image : url(asset/solid-painted-concrete-wall-textured-backdrop.jpg)")
        self.label_HIGH_LOW.addItem("welcome to high_and_low")
        self.label_HIGH_LOW.addItem("there is a number between 1 to 100")
        self.label_HIGH_LOW.addItem("guess it")
        self.line_edit = QLineEdit()
        self.line_edit.setAlignment(Qt.AlignCenter)
        self.keterangan = QLabel("your answer :")
        self.line_edit.setFixedSize(300,150)
        self.button_HIGH_LOW = Button((100, 50), "START", 20)
        self.button_HIGH_LOW_balik = Button((100, 50), "back", 20)

        self.keterangan.setStyleSheet("font : 30px Arial;"
                                "border : 5px solid black;"
                                "background-color : white;"
                                "color : black")
        self.line_edit.setStyleSheet("border : 5px solid black;"
                                "border-radius : 20px;"
                                "background-color : white;"
                                "color : black;"
                                "font : 50px Arial")
        """layout"""
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.label_HIGH_LOW, alignment=Qt.AlignTop)
        self.main_layout.addWidget(self.keterangan, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.line_edit, alignment=Qt.AlignCenter)
        self.main_layout.addWidget(self.button_HIGH_LOW, alignment=Qt.AlignCenter )
        self.main_layout.addWidget(self.button_HIGH_LOW_balik, alignment=Qt.AlignCenter )



class shooting():
    def __init__(self) -> None:
        self.label_shooting_range = QListWidget()
        self.label_shooting_range.setStyleSheet("background-image : url(asset/solid-painted-concrete-wall-textured-backdrop.jpg)")
        self.label_shooting_range.addItem("u and ur oppoent have 3 hp")
        self.label_shooting_range.setFixedSize(300, 350)
        self.button_shooting = []
        self.button_shooting.append(Button((200, 100),"shoot", 40))
        self.button_shooting.append(Button((200, 100),"BACK", 40))

        """layout"""
        self.shooting_layout = QVBoxLayout()  
        self.second_shooting_layout = QHBoxLayout()
        self.shooting_layout.addWidget(self.label_shooting_range, alignment=Qt.AlignCenter)
        self.second_shooting_layout.addWidget(self.button_shooting[0])
        self.second_shooting_layout.addWidget(self.button_shooting[1])
        self.shooting_layout.addLayout(self.second_shooting_layout)

        

class fish() :
    def __init__(self) -> None:
        self.label_iwak_pool = QListWidget()
        self.label_iwak_pool.setFixedSize(600, 350)
        self.label_iwak_pool.setStyleSheet("background-image : url(asset/solid-painted-concrete-wall-textured-backdrop.jpg)")
        list_iwak_in_inv = QMenu()  
        self.button_iwak = []
        self.button_iwak.append(Button((90, 100), "fish", 40))
        self.button_iwak.append(Button((50, 60),"back", 20))
        """layout"""
        self.fishing_layout = QVBoxLayout()
        self.fishing_layout.addWidget(self.label_iwak_pool, alignment=Qt.AlignCenter)
        self.fishing_layout.addWidget(self.button_iwak[0], alignment=Qt.AlignCenter)
        self.fishing_layout.addWidget(self.button_iwak[1], alignment=Qt.AlignCenter)




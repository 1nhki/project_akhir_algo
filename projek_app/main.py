from PyQt5.QtCore import (Qt, QSize)
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QGroupBox, QButtonGroup, QLineEdit, QCheckBox, QListWidget)
from PyQt5.QtGui import (QPixmap, QIcon, QImage, QPalette, QBrush) #ini belum ada
from random import randint,choice, seed, random
from time import sleep, time_ns
import json

app = QApplication([])
class MainWindow(QWidget):
    def __init__(self, title, layout, size):
        super().__init__()
        self.setWindowTitle(title)                  
        self.resize(size[0], size[1])
        self.setLayout(layout)
        self.setWindowIcon(QIcon("projek_app/asset/home_14782571.png"))
        self.bg_img = QImage("projek_app/asset/black-brick-wall-textured-background.jpg")
        alamak= QPalette()
        alamak.setBrush(QPalette.Window, QBrush(self.bg_img))
        self.setPalette(alamak)
class Button(QPushButton):
    def __init__(self,size, string, font = 50):
        super().__init__()
        self.setText(string)        
        self.setFixedSize(size[0], size[1])
        css = f"""      border : 5px solid black;  
                        border-radius : 20px;
                        background-color : white;
                        font : {font}px arial;
                        color : black;
            """
        self.setStyleSheet(css)

  


"""listwidget"""
"""iwak"""
label_iwak_pool = QListWidget()
button_iwak = []
button_iwak.append(QPushButton("shoot"))
button_iwak.append(QPushButton("inventory"))

"""SHOOT"""
label_shooting_range = QListWidget()
label_shooting_range.setStyleSheet("background-image : url(projek_app/asset/solid-painted-concrete-wall-textured-backdrop.jpg)")
label_shooting_range.addItem("u and ur oppoent have 3 hp")
label_shooting_range.setFixedSize(300, 350)
button_shooting = []
button_shooting.append(Button((200, 100),"shoot", 40))
button_shooting.append(Button((200, 100),"inventory", 40))

"""HIGH_LOW"""
label_HIGH_LOW = QListWidget()
label_HIGH_LOW.setStyleSheet("background-image : url(projek_app/asset/solid-painted-concrete-wall-textured-backdrop.jpg)")
label_HIGH_LOW.addItem("welcome to high_and_low")
label_HIGH_LOW.addItem("there is a number between 1 to 100")
label_HIGH_LOW.addItem("guess it")
line_edit = QLineEdit()
line_edit.setAlignment(Qt.AlignCenter)
keterangan = QLabel("your answer :")
line_edit.setFixedSize(300,150)
button_HIGH_LOW = Button((100, 50), "START", 20)

keterangan.setStyleSheet("font : 30px Arial;"
                         "border : 5px solid black;"
                         "background-color : white;"
                         "color : black")
line_edit.setStyleSheet("border : 5px solid black;"
                        "border-radius : 20px;"
                        "background-color : white;"
                        "color : black;"
                        "font : 50px Arial")
"""Home"""
list_program = ["high and low", "roulette"]
home_label = QLabel("WELCOME")
abcd = list()
for i in range(len(list_program)):
    abcd.append(QRadioButton())
    abcd[i].setText(list_program[i])

button_start = Button((200, 100), "start")
    

abcd[0].setStyleSheet("font : 30px Arial;"
                      """QRadioButton::indicator {
                      image: url (projek_app/asset/unchecked_box.png)
                      }""")
abcd[1].setStyleSheet("font : 30px Arial")


"""     qpixmap      """
img_home = QPixmap("projek_app/asset/home_14782571.png")
img_home = img_home.scaled(90, 90)
home_label.setFixedSize(150,150)
home_label.setPixmap(img_home)
home_label.setStyleSheet("border : 2px solid cyan;"
                        "border-radius : 20px;"
                        "background-color : white")
home_label.setAlignment(Qt.AlignCenter)
"""layout"""
"""fishing"""
fishing_layout = QVBoxLayout()
"""SHOOTING"""
shooting_layout = QVBoxLayout()  
second_shooting_layout = QHBoxLayout()
shooting_layout.addWidget(label_shooting_range, alignment=Qt.AlignCenter)
second_shooting_layout.addWidget(button_shooting[0])
second_shooting_layout.addWidget(button_shooting[1])
shooting_layout.addLayout(second_shooting_layout)

"""HIGH_LOW"""
main_layout = QVBoxLayout()
main_layout.addWidget(label_HIGH_LOW, alignment=Qt.AlignTop)
main_layout.addWidget(keterangan, alignment=Qt.AlignCenter)
main_layout.addWidget(line_edit, alignment=Qt.AlignCenter)
main_layout.addWidget(button_HIGH_LOW, alignment=Qt.AlignCenter )
"""HOME"""
home_layout = QVBoxLayout()
home_layout.addWidget(home_label, alignment=Qt.AlignCenter)
home_layout.addWidget(abcd[1], alignment=Qt.AlignCenter)
home_layout.addWidget(abcd[0], alignment=Qt.AlignCenter)
home_layout.addWidget(button_start, alignment=Qt.AlignCenter)

"""  -------funCtion--------         """
"""shooting"""
class shoot():
    def __init__(self):
        self.attempt = 0
        self.revolve = []
        self.number_of_revolver = 0
        self.choose = 0
        self.hp_player = 3
        self.hp_opponent = 3
    def minus_hp_player(self):
        self.hp_player -= 1
    def minus_hp_opponent(self):
        self.hp_opponent -= 1   
    def reloading_gun(self):
        label_shooting_range.addItem("reloading..")
        sleep(0.3)
        self.number_of_revolver = randint(1, 8)
        self.revolve = [1 , 3, 4, 5, 6, 7, 8]
    def player_shoot(self):
        seed(time_ns())
        label_shooting_range.addItem("you shoot the opponent")
        self.choose = randint(1, 8)
        
        while True :
            try:
                self.revolve.remove(self.choose)
                break
            except:
                self.choose =  randint(1, 8)
        if self.choose == self.number_of_revolver :
            self.minus_hp_player()
            sleep(0.3)
            label_shooting_range.addItem("you hit yourself -1")
            label_shooting_range.addItem(f"player hp {self.hp_player}")
            self.reloading_gun()
        else :
            sleep(0.3)
            label_shooting_range.addItem('NOTHING')
    def opponent_shoot(self) :
        
        seed(time_ns())
        label_shooting_range.addItem("you shoot the opponent")
        self.choose = randint(1, 8)
        
        while True :
            try:
                self.revolve.remove(self.choose)
                break
            except:
                self.choose =  randint(1, 8)
        if self.choose == self.number_of_revolver :
            self.minus_hp_opponent()
            sleep(0.3)
            label_shooting_range.addItem("you hit opponent -1")
            label_shooting_range.addItem(f"opponent hp {self.hp_opponent}")
            self.reloading_gun()
        else :
            sleep(0.3)
            label_shooting_range.addItem('NOTHING')
         

    def awalan_round(self) :
        if self.number_of_revolver == 0 :
            self.reloading_gun()
        self.player_shoot()
        self.opponent_shoot()
"""high_low"""
class high_and_low():
    def __init__(self):
        self.counter = 0
        self.random = randint(1, 100)
    def game(self) :
        if self.random > int(line_edit.text()):
            label_HIGH_LOW.addItem("TOO LOW")
            self.counter += 1
        elif self.random < int(line_edit.text()):
            label_HIGH_LOW.addItem("TOO HIGH")
            self.counter += 1
        else :
            label_HIGH_LOW.addItem("YOU GUESS IT RIGHT")
            label_HIGH_LOW.addItem(f"YOUR ATTEMPT {self.counter}")
    
"""iwak"""
class iwak():
    def __init__(self) -> None:
        with open("iwak.json", 'r') as data :
            self.data = json.load(data)
    def gacha_time(self) :
        gacha = random()
        if gacha >= 0.95:
            self.kepilih = random.choice(self.data["epic"])
        elif gacha >= 0.9:
            self.kepilih = random.choice(self.data["rare"])
        else :
            self.kepilih = random.choice(self.data["common"])

'''start'''
def check():
    if abcd[0].isChecked() or abcd[1].isChecked() :
        if abcd[0].isChecked() :
            home_window.show()
            start_window.hide()
            return runner
        elif abcd[1].isChecked() :
             shooting_window.show()
             start_window.hide()


"""connect"""

runner = high_and_low()
runner2 = shoot()
button_start.clicked.connect(check)
alamak = button_HIGH_LOW.clicked.connect(runner.game)
button_shooting[0].clicked.connect(runner2.awalan_round)

"""window"""
fishing_window = MainWindow("fish", fishing_layout, (700,500))
start_window = MainWindow("start", home_layout, (450, 500))
home_window = MainWindow("Home", main_layout, (450, 500))
shooting_window = MainWindow("shooting", shooting_layout, (450, 500))

"""EXEC"""
fishing_window.show()
start_window.show()
app.exec_()
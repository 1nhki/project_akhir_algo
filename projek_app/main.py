from PyQt5.QtCore import (Qt, QSize)
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,QLabel, QVBoxLayout, QHBoxLayout, QRadioButton,
                             QGroupBox, QButtonGroup, QLineEdit, QCheckBox, QListWidget)
from PyQt5.QtGui import (QPixmap, QIcon, QImage, QPalette, QBrush) #ini belum ada
from random import randint, shuffle, seed
from time import sleep, time_ns

app = QApplication([])
class MainWindow(QWidget):
    def __init__(self, title, layout):
        super().__init__()
        self.setWindowTitle(title)
        self.resize(450, 500)
        self.setLayout(layout)
        self.setWindowIcon(QIcon("projek_app/asset/home_14782571.png"))
        self.bg_img = QImage("projek_app/asset/placard-templates-set-with-abstract-shapes-80s-memphis-geometric-style-flat-line-design-elements-ret/391481422432.jpg")
                                        

"""listwidget"""
"""SHOOT"""
label_shooting_range = QListWidget()
label_shooting_range.addItem("u and ur oppoent have 3 hp")
label_shooting_range.setFixedSize(300, 350)
button_shooting = []
button_shooting.append(QPushButton("shoot"))
button_shooting.append(QPushButton("inventory"))


"""HIGH_LOW"""
label_HIGH_LOW = QListWidget()
label_HIGH_LOW.addItem("welcome to high_and_low")
label_HIGH_LOW.addItem("there is a number between 1 to 100")
label_HIGH_LOW.addItem("guess it")
line_edit = QLineEdit()
keterangan = QLabel("your answer :")
button_HIGH_LOW = QPushButton("start")

keterangan.setStyleSheet("font : 30px Arial")
"""Home"""
list_program = ["high and low", "roulette"]
home_label = QLabel("WELCOME")
abcd = list()
for i in range(len(list_program)):
    abcd.append(QRadioButton())
    abcd[i].setText(list_program[i])

button_start = QPushButton("start")
button_start.setStyleSheet("font : 50px Arial")
button_start.setFixedHeight(100)
button_start.setFixedWidth(200)

abcd[0].setStyleSheet("font : 30px Arial")
abcd[1].setStyleSheet("font : 30px Arial")


"""     qpixmap      """
img_home = QPixmap("projek_app/asset/home_14782571.png")
img_home = img_home.scaled(90, 90)
home_label.setPixmap(img_home)
"""layout"""
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
main_layout.addWidget(button_HIGH_LOW)
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
        return "skibidi"
    
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
start_window = MainWindow("HOME", home_layout)
home_window = MainWindow("Home", main_layout)
shooting_window = MainWindow("shooting", shooting_layout)

"""EXEC"""
start_window.show()
app.exec_()
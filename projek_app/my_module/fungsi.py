from random import randint,choice, seed, random
from time import sleep, time_ns
from .layout_project import *
import json


"""home = home()
high_low = high_low()
shooting = shooting()
fish = fish()
"""
"""start"""
def check(window_home , list_window, home):
    if home.abcd[0].isChecked() or home.abcd[1].isChecked() or home.abcd[2].isChecked() :
        if home.abcd[0].isChecked() :
            list_window[1].show()
            window_home.hide()

        elif home.abcd[1].isChecked() :
             list_window[2].show()
             window_home.hide()

        elif home.abcd[2].isChecked() :
             list_window[3].show()
             window_home.hide()
            
class iwak():
    def __init__(self) -> None:
        with open("data_text/iwak.json", 'r') as data :
            self.data = json.load(data)
    def gacha_time(self, fish) :
        gacha = random()
        if gacha >= 0.95:
            self.kepilih = choice(self.data["epic"])
        elif gacha >= 0.9:
            self.kepilih = choice(self.data["rare"])
        else :
            self.kepilih = choice(self.data["common"])
        fish.label_iwak_pool.addItem(f"anda mendapat {self.kepilih[0]}")
    def balik(self, fish_window, start_window ) :
        fish_window.hide()
        start_window.show()


class high_and_low():
    def __init__(self):
        self.counter = 0
        self.random = randint(1, 100)
    def game(self, high_low) :
        if self.random > int(high_low.line_edit.text()):
            high_low.label_HIGH_LOW.addItem("TOO LOW")
            self.counter += 1
        elif self.random < int(high_low.line_edit.text()):
            high_low.label_HIGH_LOW.addItem("TOO HIGH")
            self.counter += 1
        else :
            high_low.label_HIGH_LOW.addItem("YOU GUESS IT RIGHT")
            high_low.label_HIGH_LOW.addItem(f"YOUR ATTEMPT {self.counter}")
    def balik(self, home_window, high_low_win) :
        home_window.show()
        high_low_win.hide()   


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
    def reloading_gun(self,shooting):
        shooting.label_shooting_range.addItem("reloading..")
        sleep(0.3)
        self.number_of_revolver = randint(1, 8)
        self.revolve = [1 , 3, 4, 5, 6, 7, 8]
    def player_shoot(self, shooting):
        seed(time_ns())
        shooting.label_shooting_range.addItem("you shoot the opponent")
        self.choose = randint(1, 8)
        
        while True :
            try:
                self.revolve.remove(self.choose)
                break
            except:
                self.choose =  randint(1, 8)
        if self.choose == self.number_of_revolver :
            self.minus_hp_player()
            shooting.label_shooting_range.addItem("you hit yourself -1")
            shooting.label_shooting_range.addItem(f"player hp {self.hp_player}")
            self.reloading_gun()
        else :
            shooting.label_shooting_range.addItem('NOTHING')
    def opponent_shoot(self, shooting) :
        
        seed(time_ns())
        shooting.label_shooting_range.addItem("you shoot the opponent")
        self.choose = randint(1, 8)
        
        while True :
            try:
                self.revolve.remove(self.choose)
                break
            except:
                self.choose =  randint(1, 8)
        if self.choose == self.number_of_revolver :
            self.minus_hp_opponent()
            shooting.label_shooting_range.addItem("you hit opponent -1")
            shooting.label_shooting_range.addItem(f"opponent hp {self.hp_opponent}")
            self.reloading_gun()
        else :
            shooting.label_shooting_range.addItem('NOTHING')
         

    def awalan_round(self, shooting_layout) :
        if self.number_of_revolver == 0 :
            self.reloading_gun(shooting_layout)
        self.player_shoot(shooting_layout)
        self.opponent_shoot(shooting_layout)
    
    def balik(self, shooting_window, start_window) :
        shooting_window.hide()
        start_window.show()
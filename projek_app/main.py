import my_module 
from PyQt5.QtWidgets import (QApplication)

app = QApplication([])

"""layout"""
high_low_layout = my_module.high_low()
shooting_layout = my_module.shooting()
start_layout = my_module.home()
fish_layout = my_module.fish()

"""window"""
fishing_window = my_module.MainWindow("fish", fish_layout.fishing_layout, (700,500))
start_window = my_module.MainWindow("start", start_layout.home_layout, (450, 500))
high_window = my_module.MainWindow("Higlow", high_low_layout.main_layout, (450, 500))
shooting_window = my_module.MainWindow("shooting", shooting_layout.shooting_layout, (450, 500))

"""function"""
high_low_function = my_module.high_and_low()
shooting_function = my_module.shoot()
start_function = my_module.check(start_window, [0,high_window, shooting_window, fishing_window], start_layout)
fish_function = my_module.iwak()

"""clicked.connect"""

start_layout.button_start.clicked.connect(lambda : my_module.check(start_window, [0,high_window, shooting_window, fishing_window], start_layout))
"""high_low"""
high_low_layout.button_HIGH_LOW.clicked.connect(lambda: high_low_function.game(high_low_layout))
high_low_layout.button_HIGH_LOW_balik.clicked.connect(lambda: high_low_function.balik(start_window, high_window))

"""shooting"""
shooting_layout.button_shooting[0].clicked.connect(lambda : shooting_function.awalan_round(shooting_layout))
shooting_layout.button_shooting[1].clicked.connect(lambda : shooting_function.balik(shooting_window,start_window))

"""fish"""
fish_layout.button_iwak[0].clicked.connect(lambda : fish_function.gacha_time(fish_layout))
fish_layout.button_iwak[1].clicked.connect(lambda : fish_function.balik(fishing_window, start_window))




start_window.show()





app.exec()

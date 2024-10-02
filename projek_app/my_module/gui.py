from PyQt5.QtWidgets import (QWidget, QPushButton)
from PyQt5.QtGui import (QPalette, QBrush, QImage, QIcon)

class MainWindow(QWidget):
    def __init__(self, title, layout, size):
        super().__init__()
        self.setWindowTitle(title)                  
        self.resize(size[0], size[1])
        self.setLayout(layout)
        self.setWindowIcon(QIcon("asset/home_14782571.png"))
        self.bg_img = QImage("asset/black-brick-wall-textured-background.jpg")
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

class button_iwak_inv(QPushButton):
    def __init__(self, string, scale = (90, 90)):
        super().__init__()
        self.setText(f"{string}")
        self.image = QIcon("asset/ikan/Raw_Cod_JE4_BE2.webp")
        
        self.setIcon(self.image)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QMessageBox, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QRadioButton


app = QApplication([])


window = QWidget()
window.setWindowTitle("Конкурс від Crazy People")
window.resize(500,500)
window.move(600,300)


def win():
    victory = QMessageBox()
    victory.setText("Вірно \n Ви виграли гіроскутер")
    victory.exec_()

def lose():
    novictory = QMessageBox()
    novictory.setText("Невірно \n Ви виграли блокнотик")
    novictory.exec_()



text = QLabel()
text.setText("В якому році канал отримав золоту кнопку від YouTube?")

but1 = QRadioButton("2005")
but2 = QRadioButton("2010")
but3 = QRadioButton("2015")
but4 = QRadioButton("2020")


lineV = QVBoxLayout()
lineH1 = QHBoxLayout()
lineH2 = QHBoxLayout()
lineH3 = QHBoxLayout()


lineH1.addWidget(text, alignment=Qt.AlignCenter)

lineH2.addWidget(but1, alignment=Qt.AlignCenter)
lineH2.addWidget(but2, alignment=Qt.AlignCenter)
lineH3.addWidget(but3, alignment=Qt.AlignCenter)
lineH3.addWidget(but4, alignment=Qt.AlignCenter)

but1.clicked.connect(lose)
but2.clicked.connect(lose)
but3.clicked.connect(win)
but4.clicked.connect(lose)

lineV.addLayout(lineH1)
lineV.addLayout(lineH2)
lineV.addLayout(lineH3)

window.setLayout(lineV)
window.show()
app.exec_()
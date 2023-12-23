from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from random import randint

def generator():
    label2.setText(str(randint(0,100)))
    label1.setText("Переможець")

app = QApplication([])

window = QWidget()
window.setWindowTitle("Генератор")
window.resize(500,500)
window.move(600,300)

label1 = QLabel("Натисни щоб дізнатися переможця!")
label2 = QLabel("?")
but = QPushButton("Згенерувати")

lineV = QVBoxLayout()
lineV.addWidget(label1, alignment = Qt.AlignCenter)
lineV.addWidget(label2, alignment = Qt.AlignCenter)
lineV.addWidget(but, alignment = Qt.AlignCenter)


window.setLayout(lineV)
but.clicked.connect(generator)

window.show()
app.exec_()
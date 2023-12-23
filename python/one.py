from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel


app = QApplication([])


window = QWidget()
window.setWindowTitle(" ")
window.resize(500,500)
window.move(600,300)


window.show()
app.exec_()
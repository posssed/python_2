from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication,
        QMessageBox, QWidget, QHBoxLayout, 
        QVBoxLayout, QPushButton, QLabel, 
        QRadioButton, QSpinBox, QGroupBox, 
        QListWidgetItem, QFormLayout, 
        QLineEdit, QButtonGroup)

app = QApplication([])

btn_Menu = QPushButton('Меню')
btn_Sleep = QPushButton('Відпочити')

box_Minutes = QSpinBox()
box_Minutes.setValue(30)

btn_OK = QPushButton('Відповісти')
lb_Question = QLabel('')


RadioGroupBox = QGroupBox("Варіанти відповідей")
RadioGroup = QButtonGroup()


rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


AnsGroupBox = QGroupBox("Результат тесту")
lb_Resalt = QLabel('')
lb_Correct = QLabel('')

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Resalt, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()


layout_line1.addWidget(btn_Menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_Sleep)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин'))

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)

layout_line4.addStretch(1)
layout_line4.addStretch(btn_OK, stretch=2)
layout_line4.addStretch(1)


layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
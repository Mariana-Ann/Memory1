from PyQt5.QtWidgets import QWidget, QLineEdit,QHBoxLayout, QVBoxLayout, QPushButton, QLabel

menu_win = QWidget()
lbl_quest=QLabel("Введіть запитання")
lbl_right=QLabel("Введіть вірну відповідь")
lbl_wrong_ans1=QLabel("Введіть першу неправильну")
lbl_wrong_ans2=QLabel("Введіть другу неправильну")
lbl_wrong_ans3=QLabel("Введіть третю неправильну")

le_questoin= QLineEdit()
le_right= QLineEdit()
le_wrong_ans1= QLineEdit()
le_wrong_ans2= QLineEdit()
le_wrong_ans3= QLineEdit()

lb_header_start=QLabel("Cтатистика")
lb_header_start.setStyleSheet("font size: 19px; font-weight:bold; ")
lb_statistic=QLabel()

btn_add_question=QPushButton("Додати запитання")
btn_clear=QPushButton("Очистити")
btn_back=QPushButton("Назад")
vl_labels=QVBoxLayout()
vl_labels.addWidget(lbl_quest)
vl_labels.addWidget(lbl_right)
vl_labels.addWidget(lbl_wrong_ans1)
vl_labels.addWidget(lbl_wrong_ans2)
vl_labels.addWidget(lbl_wrong_ans3)

vl_lineEdits=QVBoxLayout()

vl_lineEdits.addWidget(le_questoin)
vl_lineEdits.addWidget(le_right)
vl_lineEdits.addWidget(le_wrong_ans1)
vl_lineEdits.addWidget(le_wrong_ans2)
vl_lineEdits.addWidget(le_wrong_ans3)

h1_questions=QHBoxLayout()
h1_questions.addLayout(vl_labels)
h1_questions.addLayout(vl_lineEdits)

h1_buttons=QHBoxLayout()
h1_buttons.addWidget(btn_add_question)
h1_buttons.addWidget(btn_clear)
vl_general=QVBoxLayout()
vl_general.addLayout(h1_questions)
vl_general.addLayout(h1_buttons)
vl_general.addWidget(lb_header_start) #слово статистика
vl_general.addWidget(lb_statistic) # сама статистика
vl_general.addWidget(btn_back) # кнопка назад
menu_win.setLayout(vl_general)
menu_win.resize(400,300)
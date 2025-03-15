from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, \
    QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox
from PyQt5.QtCore import Qt
from random import shuffle # перемішуватимемо відповіді у картці питання

card_width, card_height = 600, 500 # початкові розміри вікна "картка"
win_card = QWidget()
win_card.resize(card_width, card_height) # розмір вікна
win_card.move(300, 300) #показує вікно в зазначених координатах
win_card.setWindowTitle('Memory Card') #назва

btn_menu= QPushButton('Меню')
btn_relax=QPushButton('Відпочити')
btn_answer= QPushButton('Відповісти')
label_question=QLabel('') # тут буде питання
box_Minutes = QSpinBox()
box_Minutes.setValue(30)


RadioGroupBox=QGroupBox('Варіанти відповідей') # рамка
RadioGoup=QButtonGroup() # група кнопок
rbtn_1=QRadioButton('1')
rbtn_2=QRadioButton('2')
rbtn_3=QRadioButton('3')
rbtn_4=QRadioButton('4')
RadioGoup.addButton(rbtn_1)
RadioGoup.addButton(rbtn_2)
RadioGoup.addButton(rbtn_3)
RadioGoup.addButton(rbtn_4)

AnsGroupBox=QGroupBox('Результати тесту')
lb_result=QLabel('') #правильно чи ні
lb_corret=QLabel("") #правильний варіант

layout_ans1 = QHBoxLayout()   # горизонтальна
layout_ans2 = QVBoxLayout() #вертикальна лінія
layout_ans3 = QVBoxLayout()


layout_ans2.addWidget(rbtn_1) #Дві відповіді в перший стовпець
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) #Дві відповіді у другий стовпець
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

#результат тесту
layout_res= QVBoxLayout()

layout_res.addWidget(lb_result,alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_corret,alignment=Qt.AlignCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
AnsGroupBox.hide()

layout_line1=QHBoxLayout()
layout_line2=QHBoxLayout()
layout_line3=QHBoxLayout()
layout_line4=QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_relax)
layout_line1.addWidget(box_Minutes)
layout_line1.addWidget(QLabel('хвилин'))


layout_line2.addWidget(label_question,alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(AnsGroupBox)


layout_line4.addStretch(1)
layout_line4.addWidget(btn_answer,stretch=2)
layout_line4.addStretch(1)


layout_card=QVBoxLayout()

layout_card.addLayout(layout_line1,stretch=1)
layout_card.addLayout(layout_line2,stretch=2)
layout_card.addLayout(layout_line3,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4,stretch=1)
layout_card.addStretch(1)
layout_card.addSpacing(5) # прогалини між вмістом


text_wrong = 'Неправильно'
text_correct = 'Правильно'

# у цій версії напишемо в коді одне запитання та відповіді до нього
# відповідні змінні поля майбутнього об'єкта "form" (тобто. анкета)
frm_question = 'Яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'

# Тепер нам потрібно показати ці дані,
# причому відповіді розподілити випадково між радіокнопками, і пам'ятати кнопку з правильною відповіддю.
# Для цього створимо набір посилань на радіокнопки та перемішаємо його
radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)
answer = radio_list[0] # ми не знаємо, який це з радіобаттонів, але можемо покласти сюди правильну відповідь і запам'ятати це
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]


win_card.setLayout(layout_card)
win_card.show()

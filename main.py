''' Вікно для картки питання '''
from random import choice, shuffle
from PyQt5.QtWidgets import QApplication
from time import sleep

app = QApplication([])

from main_window import *
from menu_window import *

class Question:
   def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
      self.question = question 
      self.answer = answer # правильна відповідь
      self.wrong_answer1 = wrong_answer1
      self.wrong_answer2 = wrong_answer2
      self.wrong_answer3 = wrong_answer3
      self.actual = True 
      self.count_asked = 0 # кількість спроб
      self.count_right = 0 # кількість правильних відповідей
   def got_right(self):
      self.count_asked+=1
      self.count_right+=1
   def got_wrong(self):
      self.count_asked+=1

q1 = Question('Яблуко', 'apple', 'application', 'pinapple', 'apply')
q2 = Question('Дім', 'house', 'horse', 'hurry', 'hour')      
q3 = Question('Миша', 'mouse', 'mouth', 'muse', 'museum')
q4 = Question('Число', 'number', 'digit', 'amount', 'summary')

radio_buttons = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
questions = [q1, q2, q3, q4]
#random_question = choice(questions)
#shuffle(radio_list)

def new_questions():
   global cur_q
   cur_q = choice(questions)
   label_question.setText(cur_q.question)
   lb_corret.setText(cur_q.answer)
   shuffle(radio_buttons)
   radio_buttons[0].setText(cur_q.wrong_answer1)
   radio_buttons[1].setText(cur_q.wrong_answer2)
   radio_buttons[2].setText(cur_q.wrong_answer3)
   radio_buttons[3].setText(cur_q.answer)
new_questions()

def check():
   RadioGoup.setExclusive(False)
   for answer in radio_buttons:
      if answer.isChecked():
         if answer.text() == lb_corret.text():
            cur_q.got_right()
            lb_result.setText('Вірно!')
            answer.setChecked(False)
            break
   else:
      lb_result.setText('Не вірно!')
      cur_q.got_wrong()

   RadioGoup.setExclusive(True)   

def show_result():
   RadioGroupBox.hide()
   AnsGroupBox.show()
   btn_answer.setText("Наступне питання")
    
def show_question():
   RadioGroupBox.show()
   AnsGroupBox.hide()
   btn_answer.setText("Відповісти")
   RadioGoup.setExclusive(False) #Зняти обмеження, щоб скинути вибір 
   rbtn_1.setChecked(False)
   rbtn_2.setChecked(False)
   rbtn_3.setChecked(False)
   rbtn_4.setChecked(False)
   RadioGoup.setExclusive(True)

def click_OK(self):
   if btn_answer.text() =="Відповісти":
      check()
      RadioGroupBox.hide() 
      AnsGroupBox.show()
      btn_answer.setText('Наступне запитання')
   else:
      new_questions()
      RadioGroupBox.show()
      AnsGroupBox.hide()
      btn_answer.setText('Відповісти')


show_question()

btn_answer.clicked.connect(click_OK)

def relax():
    win_card.hide()
    n = box_Minutes.value() * 60
    sleep(n)
    win_card.show()

btn_relax.clicked.connect(relax)
'''
def back_menu():
    menu_win.show()
    win_card.hide()
    
btn_menu.clicked.connect(back_menu)
'''
def back_main():
    menu_win.hide()
    win_card.show()    
btn_back.clicked.connect(back_main)

def clear():
    le_questoin.clear()
    le_right.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()

btn_clear.clicked.connect(clear)

def add_question():
   new_q = Question(le_questoin.text(), le_right.text(),
                    le_wrong_ans1.text(),le_wrong_ans2.text(),le_wrong_ans3.text())
   questions.append(new_q)
   clear()

btn_add_question.clicked.connect(add_question)
def menu_generation():
   if cur_q.count_asked == 0:
        c = 0
   else:
        c = (cur_q.count_right / cur_q.count_asked) * 100
   text = 'Всього було задано питань: ' + str(cur_q.count_asked) + '\n' + \
           'Вірних відповідей: ' + str(cur_q.count_right) + '\n' + \
           'Успішність: ' + str(round(c, 2)) + '%'


   lb_statistic.setText(text)
   menu_win.show()
   win_card.hide()
btn_menu.clicked.connect(menu_generation)




app.exec_()
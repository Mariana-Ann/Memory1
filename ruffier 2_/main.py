from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from instructions import txt_instruction, txt_test1, txt_test3, txt_sits
from kivy.uix.scrollview import ScrollView

age = 7
name = ""
p1, p2, p3 = 0, 0, 0
class ScrButton(Button):
    def __init__(self, screen, direction='right', goal='main', **kwargs):
        super().__init__(**kwargs)
        self.screen = screen
        self.direction = direction
        self.goal = goal
   
    def on_press(self):
        # Перехід до іншого екрану при натисканні
        self.screen.manager.transition.direction = self.direction
        self.screen.manager.current = self.goal


class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_instruction, size_hint=(0.9, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
        lbl1 = Label(text="Введіть ім'я:", size_hint=(0.3, 0.1), pos_hint={'x': 0.1, 'top': 0.45})
        self.in_name = TextInput(multiline=False, size_hint=(0.5, 0.1), pos_hint={'x': 0.4, 'top': 0.45})
        lbl2 = Label(text="Введіть вік:", size_hint=(0.3, 0.1), pos_hint={'x': 0.1, 'top': 0.6})
        self.in_age = TextInput(text="7", multiline=False, size_hint=(0.5, 0.1), pos_hint={'x': 0.4, 'top': 0.6})
        self.btn = Button(text="Почати", size_hint=(0.3, 0.15), pos_hint={'center_x': 0.5, 'y': 0.1})
        self.btn.on_press = self.next
        layout.add_widget(instr)
        layout.add_widget(lbl1)
        layout.add_widget(self.in_name)
        layout.add_widget(lbl2)
        layout.add_widget(self.in_age)
        layout.add_widget(self.btn)
        self.add_widget(layout)

    def next(self):
        global name
        name = self.in_name.text
        self.manager.current = "pulse1"

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_test1, size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
        lbl_result = Label(text="Введіть результат:", size_hint=(0.3, 0.1), pos_hint={'x': 0.1, 'top': 0.65})
        self.in_result = TextInput(text="0", multiline=False, size_hint=(0.5, 0.1), pos_hint={'x': 0.4, 'top': 0.65})
        self.btn = Button(text="Продовжити", size_hint=(0.3, 0.15), pos_hint={'center_x': 0.5, 'y': 0.1})
        self.btn.on_press = self.next
        layout.add_widget(instr)
        layout.add_widget(lbl_result)
        layout.add_widget(self.in_result)
        layout.add_widget(self.btn)
        self.add_widget(layout)

    def next(self):
        global p1
        p1 = int(self.in_result.text)
        self.manager.current = "sits"

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_sits, size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'top': 0.9})
        self.btn = Button(text="Продовжити", size_hint=(0.3, 0.15), pos_hint={'center_x': 0.5, 'y': 0.1})
        self.btn.on_press = self.next
        layout.add_widget(instr)
        layout.add_widget(self.btn)
        self.add_widget(layout)

    def next(self):
        self.manager.current = "pulse2"

class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        instr = Label(text=txt_test3, size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'top': 1})
        lbl_result1 = Label(text="Результат:", size_hint=(0.3, 0.1), pos_hint={'x': 0.1, 'top': 0.75})
        self.in_result1 = TextInput(text="0", multiline=False, size_hint=(0.5, 0.1), pos_hint={'x': 0.4, 'top': 0.75})
        lbl_result2 = Label(text="Результат після відпочинку:", size_hint=(0.3, 0.1), pos_hint={'x': 0.1, 'top': 0.6})
        self.in_result2 = TextInput(text="0", multiline=False, size_hint=(0.5, 0.1), pos_hint={'x': 0.4, 'top': 0.6})
        self.btn = Button(text="Завершити", size_hint=(0.3, 0.15), pos_hint={'center_x': 0.5, 'y': 0.1})
        self.btn.on_press = self.next
        layout.add_widget(instr)
        layout.add_widget(lbl_result1)
        layout.add_widget(self.in_result1)
        layout.add_widget(lbl_result2)
        layout.add_widget(self.in_result2)
        layout.add_widget(self.btn)
        self.add_widget(layout)

    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = "result"

class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()
        self.instr = Label(text="", size_hint=(0.8, 0.2), pos_hint={'center_x': 0.5, 'top': 1})
        layout.add_widget(self.instr)
        self.add_widget(layout)
        self.on_enter = self.before

    def before(self):
        global name
        self.instr.text = name + "\n"

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name="instr"))
        sm.add_widget(PulseScr(name="pulse1"))
        sm.add_widget(CheckSits(name="sits"))
        sm.add_widget(PulseScr2(name="pulse2"))
        sm.add_widget(Result(name="result"))
        return sm

app = HeartCheck()
app.run()

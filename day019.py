from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Box(BoxLayout):
   def __init__(self, **kwargs): 
        super(Box, self).__init__(**kwargs)
        txt = '#100DaysOfCode'
        btn = Button(text=txt, font_size=50)
        self.add_widget(btn)
       
        def clc(self):
            btn.text = 'Day 19'
            btn.font_size = 70
        btn.bind(on_press=clc)
class MyApp(App):
    def build(self):
        return Box()


if __name__ == '__main__':
    MyApp().run()
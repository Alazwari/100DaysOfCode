#Day 20

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class Day20Window(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        fruits = {'Cherry'}
        fruits.add('Orange')
        fruits.update(['Apple','Banana'])
        
        for i in fruits:
            lbl = Label(text=i)
            self.add_widget(lbl)


class Day20App(App):
    def build(self):
        return Day20Window()

if __name__=='__main__':
    Day20App().run()
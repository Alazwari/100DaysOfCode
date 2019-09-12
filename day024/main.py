#Day 24
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label


class Todo(GridLayout):
    def clear(self):
        self.ids.txt.text = ''

    def todo(self, i, items):
        items = items.append(i)
        self.clear()


class ToDoApp(App):
    def build(self):
        return Todo()

if __name__=='__main__':
    ToDoApp().run()
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout




class Calc(GridLayout):
    def pressed(self, txt):
        self.ids.tx.text += txt
        print(self.ids.tx.text)
    def calculation(self, calculation):
        if calculation:
            try:
                self.ids.tx.text = str(eval(calculation))
            except Exception:
                self.ids.tx.text = 'Error'

class Day023App(App):
    def build(self):
        return Calc()

if __name__=='__main__':
    Day023App().run()
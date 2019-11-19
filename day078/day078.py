from tkinter import *
from tkinter import messagebox
window=Tk()

window.title("Tic Tac Toe Game")
window.geometry("400x300")
window.config(background='#70a1ff')

lbl=Label(window,text="Player 1: X",font=('Helvetica','20'))
lbl.config(background='#70a1ff')
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','20'))
lbl.config(background='#70a1ff')
lbl.grid(row=2,column=0)


window.mainloop()

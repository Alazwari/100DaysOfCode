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



btn = ['btn1', 'btn2', 'btn3']


for col in range(len(btn)):
    for row in range(len(btn)):
        btn[col] = Button(window, text=" ",bg="#1e90ff", fg="Black",width=3,height=1,font=('Helvetica','20'), )
        btn[col].grid(column=col+1, row=row+1)


window.mainloop()
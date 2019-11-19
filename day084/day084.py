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



btn = ['btn1', 'btn2', 'btn3', 'btn4', 'btn5', 'btn6', 'btn7', 'btn8', 'btn9']


for col in range(1,4):
    for row in range(1, 4):
        btn[col] = Button(window, text=" ",bg="#1e90ff", fg="Black",width=3,height=1,font=('Helvetica','20'), )
        btn[col].grid(column=col, row=row)
        if row == 1:
            btn[col]['text'] = col
        elif row == 2:
            btn[col]['text'] = col+3
        else:
            btn[col]['text'] = col+6
        print(f'btn{row}')
        
window.mainloop()
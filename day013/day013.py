#Day 13

months = ['January','February','March','April','May','June','July','August','September','October','November','December']
print('To close the program write (exit)')
ask = None
while ask != 'exit':
    ask = input('Enter the month number: ')
    try:
        ask = int(ask)
        if ask <= 0:
            print('Enter 1 to 12, or exit to close the program')
        else:
            print(months[ask-1])
    except:
        if ask == 'exit':
            print('Thank yoy for using the program')
        else:
            print('Enter 1 to 12, or exit to close the program')
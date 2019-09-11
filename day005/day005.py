#Day 5

#Define the variable x, y and z:
x= 'apple'
y = 'orange'
z= 'limon'

#Define basket and assign x, y, z to it.
basket = x + y + z

#Use for & enumerate to loop & print basket:
for i, s in enumerate(basket.split('e')):
    print(s +'e') if i < 2 else print(s)
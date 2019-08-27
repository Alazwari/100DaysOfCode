#Day 8

#Rock Paper Scissors Game
from random import randint
computer = randint(0,2)
player = input('Player #1, your turn to play:  ').lower()


if computer == 0:
    computer_choice = 'rock'
elif computer == 1:
    computer_choice = 'paper'
else:
    computer_choice = 'scissors'

print(f'Computer plays {computer_choice}')

if player == computer_choice:
    print('Tie!')
elif player == 'rock':
    if computer_choice == 'scissors':
        print('You Wins!')
    else:
        print('Computer Wins!')
elif player == 'paper':
    if computer_choice == 'rock':
        print('You Wins!')
    else:
        print('Computer Wins!')
elif player == 'scissors':
    if computer_choice == 'rock':
        print('Computer Wins!')
    else:
        print('You Wins!')
else:
    print('You Enter A Wrong Word')

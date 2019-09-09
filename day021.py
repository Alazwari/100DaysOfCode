#Day 21
import random

def drow_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

def player():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Choose X or O')
        letter = input().upper()
    if letter == 'X':
        return['X','O']
    else:
        return['O','X']

def first():
    if random.randint(0,1) == 0:
        return 'Computer'
    else:
        return 'Player'

def main():
    print('Welcom to Tic Tac Toe game')
    random.seed()
    the_board = [''] * 10
    for i in range(9,0,-1):
        the_board[i] = str(i)
    drow_board(the_board)
    player_letter, computer_letter = player()
    turn = first()
    print(f'The first {turn} will go first')  
if __name__ == '__main__':
    main()
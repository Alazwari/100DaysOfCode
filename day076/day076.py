# Day 76
# Final Project
import random

def drow_board(board):
    print(' '+ board[7]+ ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' '+ board[4]+ ' | ' + board[5] + ' | ' + board[9])
    print('-----------')
    print(' '+ board[1]+ ' | ' + board[2] + ' | ' + board[3])

def main():
    print('Welcome To The Tic Tac Toe Game\n')
    random.seed()
    while True:
        board = ['']*10
        for i in range(9,0,-1):
            board[i] = str(i)
        drow_board(board)
        break

if __name__ == '__main__':
    main()
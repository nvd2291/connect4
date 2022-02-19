# clear
import numpy as np

ROWS = 6
COLUMNS = 7

def create_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

def is_valid_move(board, col):
    return board[ROWS -1][col] == 0

def get_next_row(board, col):
    for r in range(ROWS,0, -1):
        if board[r][col] == 0:
            return r

def determine_winner():
    pass

def update_board(board, row, col, piece):
    board[row][col] = piece
    

def get_player_move(player_name):
    print(player_name + " enter your move (0-6): ")
    move = int(input(""))
    return move

board = create_board()
print(board)
game_over = False
turn = 0

while not game_over :

    if turn == 0:

        col = get_player_move("Player 1")

        if is_valid_move(board, col):
            row = get_next_row(board, col)
            update_board(board, row, col, 1)

    if turn == 1:

        col = get_player_move("Player 2")

        if is_valid_move(board, col):
            row = get_next_row(board, col)
            update_board(board, row, col, 2)
    
    turn += 1
    turn = turn % 2

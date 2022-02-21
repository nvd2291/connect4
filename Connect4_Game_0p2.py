
import numpy as np

ROWS = 6
COLUMNS = 7
ROWS_MAX_INDEX = ROWS - 1
COL_MAX_INDEX  = COLUMNS - 1
PLAYER1        = 1
PLAYER2        = 2
def create_board():
    board = np.zeros((ROWS, COLUMNS))
    return board

def is_valid_move(board, col):
    # 0th Row is the top most row
    return board[0][col] == 0

def get_next_row(board, col):
    # 5th Row is the Bottom most Row3
    for r in range(ROWS_MAX_INDEX, 0, -1):
        if board[r][col] == 0:
            return r

def determine_winner(board, player):
    #Determine Horiztonal Winner

    horiz_piece_count = 0
    #Loop through each Row
    for rows in range(0, ROWS):
        #Loop through each index in the row
        for index in range(0, COLUMNS):
            #If we are at column 5 and there is no piece at
            #Column 4 winning is not possible for this row
            if index >= 5 and not horiz_piece_count:
                break
            
            if int(board[rows][index]) != player:
            # if board[rows][index] != player:
                #Reset the number of pieces
                horiz_piece_count = 0
                continue
            #Board piece is the current player piece
            else:
                horiz_piece_count +=1
        if horiz_piece_count == 4:
            return True

    #Determine Vertical Winner

    vert_piece_count = 0
    #Logic is the same from horizontal just modified
    #Loop through each Row
    for cols in range(0, COLUMNS):
        #Loop through each index in the row
        for index in range(0, ROWS):
            # If we are at row 3 and there is no piece at
            # row 3 for the given player winning is not possible 
            # for this row column
            if index >= 3 and not vert_piece_count:
                break 
            if int(board[index][cols]) != player:
                #Reset the number of pieces
                vert_piece_count = 0
                continue
            #Board piece is the current player piece
            else:
                vert_piece_count +=1
        if vert_piece_count == 4:
            return True

    #Determine Diagonal Winner L-R UP

    #Determine Diagonal Winner L-R Down

    #Determine Diagonal Winner R-L Up

    #Determine Diagonal Winner R-L Down


    return False

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
moves = 0
max_moves = 42
while not game_over:

    if(moves == max_moves):
        print("Game is a tie!")
        break
    
    if turn == 0:

        col = get_player_move("Player 1")

        if is_valid_move(board, col):
            row = get_next_row(board, col)
            update_board(board, row, col, PLAYER1)
        
        print(board)

        if (determine_winner(board, PLAYER1)):
            print("Player 1 Wins")
            gamer_over = True
            

    if turn == 1:

        col = get_player_move("Player 2")

        if is_valid_move(board, col):
            row = get_next_row(board, col)
            update_board(board, row, col, PLAYER2)
            
        print(board)
    
        if (determine_winner(board, PLAYER2)):
            print("Player 2 Wins")
            gamer_over = True

    moves += 1
    turn = moves % 2

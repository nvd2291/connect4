
import numpy as np

ROWS = 6
COLUMNS = 7
ROWS_MAX_cols = ROWS - 1
COL_MAX_cols  = COLUMNS - 1
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
    for r in range(ROWS_MAX_cols, 0, -1):
        if board[r][col] == 0:
            return r

def determine_winner(board, player):
    #Determine Horiztonal Winner

    horiz_piece_count = 0
    #Loop through each Row
    for rows in range(0, ROWS):
        #Loop through each cols in the row
        for cols in range(0, COLUMNS):
            #If we are at column 4 and there is no piece at
            #Column 4 winning is not possible for this row
            if cols >= 4 and not horiz_piece_count:
                break

            if int(board[rows][cols]) != player:
            # if board[rows][cols] != player:
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
        #Loop through each cols in the row
        for cols in range(0, ROWS):
            # If we are at row 3 and there is no piece at0
            # row 3 for the given player winning is not possible 
            # for this row column
            if cols < 3 and not vert_piece_count:
                break 
            if int(board[cols][cols]) != player:
                #Reset the number of pieces
                vert_piece_count = 0
                continue
            #Board piece is the current player piece
            else:
                vert_piece_count +=1
        if vert_piece_count == 4:
            return True

    #Determine Diagonal Winner Positive slope

    # diagonal_count = 0
    # Increment through each row
    for rows in range(ROWS_MAX_cols, ROWS -3, -1):
        # Loop through each cols in the row
        for cols in range(COLUMNS - 3):
            
            connect1 = [rows, cols]
            connect2 = [rows - 1, cols + 1]
            connect3 = [rows - 2, cols + 2]
            connect4 = [rows - 3, cols + 3]

            if connect4[0] > 0 and connect4[1] < COL_MAX_cols:
                if board[connect1[0], connect1[1]] == board[connect2[0], connect2[1]] == board[connect3[0], connect3[1]] == board[connect4[0], connect4[1]] == player:
                    return True
                else:
                    continue

    #Determine Diagonal Winner Negative slope

    # diagonal_count = 0
    # Increment through each row
    for rows in range(ROWS -3):
        # Loop through each cols in the row
        for cols in range(COLUMNS - 3):
            
            connect1 = [rows, cols]
            connect2 = [rows + 1, cols + 1]
            connect3 = [rows + 2, cols + 2]
            connect4 = [rows + 3, cols + 3]

            if connect4[0] < ROWS_MAX_cols and connect4[1] < COL_MAX_cols:
                if board[connect1[0], connect1[1]] == board[connect2[0], connect2[1]] == board[connect3[0], connect3[1]] == board[connect4[0], connect4[1]] == player:
                    return True
                else:
                    continue




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
            break
            

    if turn == 1:

        col = get_player_move("Player 2")

        if is_valid_move(board, col):
            row = get_next_row(board, col)
            update_board(board, row, col, PLAYER2)
            
        print(board)
    
        if (determine_winner(board, PLAYER2)):
            print("Player 2 Wins")
            gamer_over = True
            break

    moves += 1
    turn = moves % 2

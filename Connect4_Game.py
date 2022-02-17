## Connect 4 Game
## Naveed Naeem
## Requires 2 players
from atexit import _clear
import random as rand


class Player:

    def __init__(self, player_name):
       self.player_name  = player_name
       #Piece locations
       self.piece_locations = []
    
    def __repr__(self):
        return self.player_name
    
    def update_moves(self, row, column):
        self.piece_locations.append([row,column])
    

class Board:
    def __init__(self, player1, player2, winner = [], total_moves = 0, max_moves = 42):
        self.player1 = player1
        self.player2 = player2
        self.winner  = winner
        self.total_moves = total_moves
        self.max_moves   = max_moves
        self.board_init()
        self.rows = "ABCDEF"
        self.columns = "1234567"

    def __repr__(self):
        return self.board_state()

    def board_init(self):
        self.starting_board()

    def starting_board(self):
        self.boardA = [["A"], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]
        self.boardB = [["B"], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]
        self.boardC = [["C"], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]
        self.boardD = [["D"], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]
        self.boardE = [["E"], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]
        self.boardF = [["F"], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]
        self.boardCol = [[" "], ["1"], ["2"], ["3"], ["4"], ["5"], ["6"], ["7"]]
        print(self.boardA)
        print(self.boardB)
        print(self.boardC)
        print(self.boardD)
        print(self.boardE)
        print(self.boardF)
        print(self.boardCol)
    
    def print_board(self):
        print(self.boardA)
        print(self.boardB)
        print(self.boardC)
        print(self.boardD)
        print(self.boardE)
        print(self.boardF)
        print(self.boardCol)
    
    def determine_winner():
        pass

    



# Print welcome text, print game board, explain how 

print("Welcome to Connect 4!!!")
# intialize the players and the board objects
player1 = Player('player1')
player2 = Player('player2')
connect4_board = Board(player1, player2)

print("Pieces are enter by coordinates (row, column), similar to chess e.g. A , 4")
print("Player 1 always goes first. Chose among yourselves who Player 1 will be.")

#Get player names
player1_name = input("Player 1 please enter your name: ")
player2_name = input("Player 2 please enter your name: ")

#store the player names in their respective objects
player1.player_name = player1_name
player2.player_name = player2_name

# start_player = rand.choice([player1, player2])
# print(str(start_player) + " will go first.")

while(not connect4_board.winner or (connect4_board.total_moves <= connect4_board.max_moves)):
    # no winner and all spaces have been occupied
    if(connect4_board.total_moves == connect4_board.max_moves and not connect4_board.winner ):
        print("Game Ends in a Tie")
        break
    
    # get the starting players piece placement
    row_col_str_player1 = input("Player 1 Move: ").strip().split(',')

    # Update the players list of moves made
    player1.update_moves(row_col_str_player1[0],row_col_str_player1[1])

    #increment the number of total moves
    connect4_board.total_moves +=1

    #Update Board

    #Print Board
    connect4_board.print_board()



    # get the starting players piece placement
    row_col_str_player2 = input("Player 2 Move: ").strip().split(',')

    # Update the players list of moves made
    player2.update_moves(row_col_str_player2[0],row_col_str_player2[1])

    #increment the number of total moves
    connect4_board.total_moves +=1


    #Update Board

    #Print Board
    connect4_board.print_board()

    if (connect4_board.total_moves >= 8):
        connect4_board.determine_winner()
    # if(connect4_board.total_moves == 2):
    #     print(player1.pieces)
    #     print(player2.pieces)
    #     break
    break





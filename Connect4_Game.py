## Connect 4 Game
## Naveed Naeem
## Requires 2 players


import random as rand

###########################################################################################################################

## Player Class might not be necessary
class Player:

    def __init__(self, player_name, player_piece):
       self.player_name  = player_name
       self.player_piece = player_piece
       #Piece locations
       self.piece_locations = []
    
    def __repr__(self):
        return self.player_name
    
    def update_moves(self, row, column):
        self.piece_locations.append([row,column])
    

class Board:
    def __init__(self, player1_name, player2_name, winner = [], total_moves = 0, max_moves = 42):
        self.player1 = player1_name
        self.player2 = player2_name
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
        self.boardA = [6, " ", " ", " ", " ", " ", " ", " "]
        self.boardB = [5, " ", " ", " ", " ", " ", " ", " "]
        self.boardC = [4, " ", " ", " ", " ", " ", " ", " "]
        self.boardD = [3, " ", " ", " ", " ", " ", " ", " "]
        self.boardE = [2, " ", " ", " ", " ", " ", " ", " "]
        self.boardF = [1, " ", " ", " ", " ", " ", " ", " "]
        self.boardCol = ["", "1", "2", "3", "4", "5", "6", "7"]
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

    # def update_board(self):
    #     self.parse_board(self.player1)
    #     self.parse_board(self.player2)

    def update_board(self, player_moves, player_piece):
        for moves in player_moves:
            if not player_moves:
                break
            if moves[0]  == self.boardA[0]:
                self.boardA[moves[1]] = player_piece
            elif moves[0]  == self.boardB[0]:
                self.boardB[moves[1]] = player_piece
            elif moves[0]  == self.boardC[0]:
                self.boardC[moves[1]] = player_piece
            elif moves[0]  == self.boardD[0]:
                self.boardB[moves[1]] = player_piece
            elif moves[0]  == self.boardE[0]:
                self.boardE[moves[1]] = player_piece
            elif moves[0]  == self.boardF[0]:
                self.boardF[moves[1]] = player_piece
            else:
                print("INVALID")
        self.print_board()

    def determine_winner(self, player_moves):

        ## Horizontal Winner

        for moves in player_moves:
            winning_moves = 0



        ## Vertical Winner

        ## Left Diagonal Winner

        ## Right Diagonal Winner
        pass


def get_player_move(player_name):
    print(player_name + " enter your move")
    row_col_str_player = input(": ").strip().split(',')
    row = (int(row_col_str_player[0]))
    col = (int(row_col_str_player[1]))
    
    return row, col

#####################################################################################################

# Print welcome text, print game board

print("Welcome to Connect 4!!!")
# intialize the players and the board objects
player1 = Player('player1', 'X')
player2 = Player('player2', 'O')
connect4_board = Board(player1.player_name, player2.player_name)

print("Pieces are enter by coordinates (row, column), e.g. 1, 4")
print("Player 1 always goes first. Chose among yourselves who Player 1 will be.")

#Get player names
player1.player_name = input("Player 1 please enter your name: ")
player2.player_name = input("Player 2 please enter your name: ")

#store the player names in their respective objects
connect4_board.player1 = player1.player_name
connect4_board.player2 = player2.player_name

while(not connect4_board.winner or (connect4_board.total_moves <= connect4_board.max_moves)):
    # no winner and all spaces have been occupied
    if(connect4_board.total_moves == connect4_board.max_moves and not connect4_board.winner ):
        print("Game Ends in a Tie")
        break
    
    # Get the PLayer1 piece placement
    row, col = get_player_move(player1.player_name)
    player1.update_moves(row, col)

    #Update Board
    connect4_board.update_board(player1.piece_locations, player1.player_piece)

   #increment the number of total moves
    connect4_board.total_moves +=1

    # Get the Player2 piece placement
    row, col = get_player_move(player2.player_name)
    player2.update_moves(row, col)

    #Update Board
    connect4_board.update_board(player2.piece_locations, player2.player_piece)

    #increment the number of total moves
    connect4_board.total_moves +=1

    #Minimum number of moves to win is 7
    if (connect4_board.total_moves >= 7):
        player1_win = connect4_board.determine_winner(player1.piece_locations)
        player2_win = connect4_board.determine_winner(player2.piece_locations)

        if player1_win == True and not player2_win:
            connect4_board.winner = player1.player_name
            print(str(connect4_board.winner) + "is the winner!")
            break
        if player2_win == True and not player1_win:
            connect4_board.winner = player2.player_name
            print(str(connect4_board.winner) + "is the winner!")
            break


    # if(connect4_board.total_moves == 2):
    #     print(player1.pieces)
    #     print(player2.pieces)
    #     break





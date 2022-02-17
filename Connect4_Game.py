## Connect 4 Game
## Naveed Naeem
## Requires 2 players

class Player:

    # def __init__(self, player_name, player_moves):
    def __init__(self, player_name):
       self.player_name  = player_name
    #    self.player_moves = player_moves
       self.max_moves    = 21
       self.piece_positions = []
    
    def update_moves(self, row, column):
        self.piece_positions.append([row,column])


class Board:
    def __init__(self):
        pass
    def board_init(self):
        pass



print("Welcome to Connect4!!!")
player1_name = input("Player 1 please enter your name")
player2_name = input("Player 2 please enter your name")


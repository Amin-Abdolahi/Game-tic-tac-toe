class TicTacToe2:
    def __init__(self):
        self.board = [' ']* 10 # 0th index is not used
        #self.board = list(map(str, range(10)))
        #print(self.board)
        self.current_player = 'X'
    def show_board(self):
    #     for i in range(1, 10):
    #         print(f"{self.board[i]}", end="|")
    #         if i % 3 == 0:
    #             print()
    #             print("-------")
        print()
        print (self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-----")
        print (self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-----")
        print (self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print()
    def swap_players(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        print(f"Current player: {self.current_player}")
        return self.current_player

    def is_board_full(self):
        return ' ' not in self.board[1:]
    
    def fix_spot(self, cell, player):
        self.board[cell] = player

    def has_player_won(self, player):
        # Check rows, columns, and diagonals for a win
        # for i in range(1, 4):
        #     if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
        #         return True
        # for i in range(1, 8, 3):
        #     if self.board[i] == self.board[i + 1] == self.board[i + 2] == player:
        #         return True
        # if self.board[1] == self.board[5] == self.board[9] == player:
        #     return True
        # if self.board[3] == self.board[5] == self.board[7] == player:
        #     return True
        # return False

        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # rows
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # columns
            (1, 5, 9), (3, 5, 7)               # diagonals
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    def start(self):
        while True:
            self.show_board()
            move = int(input(f"Player {self.current_player}, enter your move (1-9): "))
            if 1 <= move <= 9 and self.board[move] == ' ':
                self.fix_spot(move, self.current_player)
                if self.has_player_won(self.current_player):
                    self.show_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if self.is_board_full():
                    self.show_board()
                    print("It's a draw!")
                    break
                self.swap_players()
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = TicTacToe2()
    game.start()
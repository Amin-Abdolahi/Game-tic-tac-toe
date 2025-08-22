

def game_won(player, board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check columns
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2 - i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

    

def game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    player_X = 'X'
    player_O = 'O'
    

    print(f"Player 1 ({player_X}) should start the game.")
    print(f"Player 2 ({player_O}) will play second.")

    for row in board:
        print("|".join(row))
        print("-" * 5)
    while True:
        for player in [player_X, player_O]:
            print(f"Player {player}'s turn.")
            try:
                row, col = map(int, input("Enter row and column separated by a space: ").split())
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
                continue
            if board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid move. Try again.")
                continue
            board[row][col] = player
            for row in board:
                print("|".join(row))
                print("-" * 5)
            if game_won(player, board):
                print(f"Player {player} wins!")
                print("Board has been reset.")
                board = [[' ' for _ in range(3)] for _ in range(3)]
                break
            elif ' ' not in board[0] and ' ' not in board[1] and ' ' not in board[2]:
                print("It's a draw!")
                print("Board has been reset.")
                board = [[' ' for _ in range(3)] for _ in range(3)]
                break

game()
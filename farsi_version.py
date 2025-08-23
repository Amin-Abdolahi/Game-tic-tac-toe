class TicTacToe2:
    """یک بازی Tic Tac Toe (دوز) با شماره‌گذاری 1 تا 9 برای خانه‌ها.
    
    این کلاس یک بازی دوز را پیاده‌سازی می‌کند که در آن بازیکنان به نوبت
    خانه‌های شماره‌گذاری شده از 1 تا 9 را انتخاب می‌کنند.
    
    Attributes:
        board (list): لیستی از 10 عنصر (ایندکس 0 استفاده نمی‌شود)
        current_player (str): بازیکن فعلی ('X' یا 'O')
    """
    
    def __init__(self) -> None:
        """مقداردهی اولیه بازی با صفحه خالی و بازیکن اول 'X'."""
        self.board = [' '] * 10  # ایندکس 0 استفاده نمی‌شود
        self.current_player = 'X'
    
    def show_board(self) -> None:
        """صفحه بازی را به صورت گرافیکی نمایش می‌دهد.
        
        خروجی نمونه:
          X|O|X
          -----
          O|X| 
          -----
           | |O
        """
        print()
        print(self.board[1] + "|" + self.board[2] + "|" + self.board[3])
        print("-----")
        print(self.board[4] + "|" + self.board[5] + "|" + self.board[6])
        print("-----")
        print(self.board[7] + "|" + self.board[8] + "|" + self.board[9])
        print()
    
    def swap_players(self) -> str:
        """بازیکن فعلی را تغییر می‌دهد و بازیکن جدید را برمی‌گرداند.
        
        Returns:
            str: بازیکن جدید ('X' یا 'O')
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        print(f"Current player: {self.current_player}")
        return self.current_player
    
    def is_board_full(self) -> bool:
        """بررسی می‌کند آیا همه خانه‌های صفحه پر شده‌اند یا خیر.
        
        Returns:
            bool: True اگر صفحه پر باشد، False در غیر این صورت
        """
        return ' ' not in self.board[1:]
    
    def fix_spot(self, cell: int, player: str) -> None:
        """علامت بازیکن را در خانه مشخص شده قرار می‌دهد.
        
        Args:
            cell (int): شماره خانه (1 تا 9)
            player (str): بازیکن ('X' یا 'O')
        """
        self.board[cell] = player
    
    def has_player_won(self, player: str) -> bool:
        """بررسی می‌کند آیا بازیکن مشخص شده برنده شده است یا خیر.
        
        Args:
            player (str): بازیکنی که باید بررسی شود ('X' یا 'O')
            
        Returns:
            bool: True اگر بازیکن برنده شده باشد، False در غیر این صورت
        """
        win_combinations = [
            (1, 2, 3), (4, 5, 6), (7, 8, 9),  # سطرها
            (1, 4, 7), (2, 5, 8), (3, 6, 9),  # ستون‌ها
            (1, 5, 9), (3, 5, 7)               # قطرها
        ]
        
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def start(self) -> None:
        """بازی را شروع می‌کند و حلقه اصلی بازی را مدیریت می‌نماید.
        
        این متد تا زمانی که بازی به پایان برسد (برد یا تساوی)
        از بازیکنان ورودی دریافت می‌کند.
        """
        print("Welcome to Tic Tac Toe!")
        print("Enter a number between 1-9 to make your move:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print()
        
        while True:
            self.show_board()
            
            try:
                move = int(input(f"Player {self.current_player}, enter your move (1-9): "))
            except ValueError:
                print("Invalid input. Please enter a number between 1-9.")
                continue
            
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
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(self, player):
        # Check rows
        for row in self.board:
            if all([cell == player for cell in row]):
                return True
        # Check columns
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        # Check diagonals
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False

    def check_draw(self):
        return all([cell in ['X', 'O'] for row in self.board for cell in row])

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        else:
            print("This cell is already occupied. Try again.")
            return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player}, enter your move (row and column): ")
            try:
                row, col = map(int, input().split())
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Row and column must be between 0 and 2. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter numbers for row and column. Try again.")
                continue
            
            if self.make_move(row, col):
                if self.check_winner(self.current_player):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if self.check_draw():
                    self.print_board()
                    print("It's a draw!")
                    break
                self.switch_player()

if __name__ == "__main__":
    game = TicTacToe()
    game.play()

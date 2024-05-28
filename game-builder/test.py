class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
    
    def check_winner(self):
        for row in self.board:
            if row.count(row[0]) == 3 and row[0] != ' ':
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True

        return False

    def is_board_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        while True:
            self.print_board()
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter col (0, 1, 2): "))
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                if self.check_winner():
                    print(f'{self.current_player} wins!')
                    break
                if self.is_board_full():
                    print('It\'s a draw!')
                    break
                self.current_player = 'X' if self.current_player == 'O' else 'O'
            else:
                print('Invalid move, try again.')

game = TicTacToe()
game.play()
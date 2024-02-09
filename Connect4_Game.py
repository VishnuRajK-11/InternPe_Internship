class Connect4:
    def __init__(self):
        self.board = [[' ' for _ in range(7)] for _ in range(6)]
        self.current_player = 'X'

    def print_board(self):
        print('+---+---+---+---+---+---+---+')
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')
            print('+---+---+---+---+---+---+---+')

    def is_valid_move(self, column):
        return self.board[0][column] == ' '

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == ' ':
                self.board[row][column] = self.current_player
                break

    def check_winner(self):
        # Check horizontally
        for row in range(6):
            for col in range(4):
                if (
                    self.board[row][col] == self.board[row][col + 1] == self.board[row][col + 2] == self.board[row][col + 3] != ' '
                ):
                    return True

        # Check vertically
        for row in range(3):
            for col in range(7):
                if (
                    self.board[row][col] == self.board[row + 1][col] == self.board[row + 2][col] == self.board[row + 3][col] != ' '
                ):
                    return True

        # Check diagonally (from bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if (
                    self.board[row][col] == self.board[row - 1][col + 1] == self.board[row - 2][col + 2] == self.board[row - 3][col + 3] != ' '
                ):
                    return True

        # Check diagonally (from top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if (
                    self.board[row][col] == self.board[row + 1][col + 1] == self.board[row + 2][col + 2] == self.board[row + 3][col + 3] != ' '
                ):
                    return True

        return False

    def is_board_full(self):
        return all(cell != ' ' for row in self.board for cell in row)

    def play_game(self):
        while True:
            self.print_board()

            try:
                column = int(input(f"Player {self.current_player}, enter column (0-6): "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if not (0 <= column <= 6):
                print("Invalid column. Please enter a number between 0 and 6.")
                continue

            if not self.is_valid_move(column):
                print("Column is full. Please choose another column.")
                continue

            self.make_move(column)

            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a tie!")
                break

            # Switch player
            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = Connect4()
    game.play_game()
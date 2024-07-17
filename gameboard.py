class GameBoard:
    def __init__(self, num_rows=6, num_cols=7):
        self.__space = ' '  # Represents an empty space on the board
        self.__num_rows = num_rows  # Number of rows in the board
        self.__num_cols = num_cols  # Number of columns in the board
        # Initialize the board with empty spaces
        self.__board = [[self.__space] * self.__num_cols for _ in range(self.__num_rows)]
        self.__winning_coords = []  # Stores the coordinates of the winning sequence

    def get_num_rows(self):
        return self.__num_rows  # Returns the number of rows

    def get_num_cols(self):
        return self.__num_cols  # Returns the number of columns

    def is_board_full(self):
        # Check if the top row is completely filled, indicating a full board
        return all(self.__board[0][col] != self.__space for col in range(self.__num_cols))

    def is_space_free(self, row, col):
        # Check if the specified space is free (empty)
        return self.__board[row][col] == self.__space

    def make_move(self, col, element):
        # Place the player's symbol in the specified column, from the bottom up
        for row in range(self.__num_rows - 1, -1, -1):
            if self.__board[row][col] == self.__space:
                self.__board[row][col] = element
                break

    def show_board_dynamic(self):
        # Display the current state of the board in the console
        for row in self.__board:
            print("|".join(row))
        print()

    def check_winner(self):
        # Check for a winner in all directions: horizontal, vertical, and both diagonals
        return self.__check_winner_hz() or self.__check_winner_vt() or self.__check_winner_diag1() or self.__check_winner_diag2()

    def get_winning_coords(self):
        # Return the coordinates of the winning sequence
        return self.__winning_coords

    def __check_winner_hz(self):
        # Check for a horizontal win
        for row in range(self.__num_rows):
            for col in range(self.__num_cols - 3):
                if self.__board[row][col] == self.__board[row][col + 1] == self.__board[row][col + 2] == self.__board[row][col + 3] != self.__space:
                    self.__winning_coords = [(row, col), (row, col + 1), (row, col + 2), (row, col + 3)]
                    return True
        return False

    def __check_winner_vt(self):
        # Check for a vertical win
        for col in range(self.__num_cols):
            for row in range(self.__num_rows - 3):
                if self.__board[row][col] == self.__board[row + 1][col] == self.__board[row + 2][col] == self.__board[row + 3][col] != self.__space:
                    self.__winning_coords = [(row, col), (row + 1, col), (row + 2, col), (row + 3, col)]
                    return True
        return False

    def __check_winner_diag1(self):
        # Check for a diagonal win (bottom-left to top-right)
        for row in range(self.__num_rows - 3):
            for col in range(self.__num_cols - 3):
                if self.__board[row][col] == self.__board[row + 1][col + 1] == self.__board[row + 2][col + 2] == self.__board[row + 3][col + 3] != self.__space:
                    self.__winning_coords = [(row, col), (row + 1, col + 1), (row + 2, col + 2), (row + 3, col + 3)]
                    return True
        return False

    def __check_winner_diag2(self):
        # Check for a diagonal win (top-left to bottom-right)
        for row in range(self.__num_rows - 3):
            for col in range(3, self.__num_cols):
                if self.__board[row][col] == self.__board[row + 1][col - 1] == self.__board[row + 2][col - 2] == self.__board[row + 3][col - 3] != self.__space:
                    self.__winning_coords = [(row, col), (row + 1, col - 1), (row + 2, col - 2), (row + 3, col - 3)]
                    return True
        return False

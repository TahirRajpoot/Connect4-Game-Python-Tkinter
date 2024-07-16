import random

class Player:
    def __init__(self, symbol, board):
        self.__symbol = symbol  # The player's symbol ('X' or 'O')
        self._gboard = board  # The game board

    def get_player_symbol(self):
        return self.__symbol  # Returns the player's symbol

class HumanPlayer(Player):
    def __init__(self, symbol, board):
        super().__init__(symbol, board)

    def play(self):
        # Human player's turn logic
        print("Player %s turn" % self.get_player_symbol())
        while True:
            try:
                # Prompt the player to enter a column number
                col = int(input("Please enter column number: "))
                # Validate the column number and check if the space is free
                if 0 <= col < self._gboard.get_num_cols() and self._gboard.is_space_free(0, col):
                    self._gboard.make_move(col, self.get_player_symbol())  # Make the move
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a valid column number.")

class ComputerPlayer(Player):
    def __init__(self, symbol, board, buttons_2d_list=[]):
        super().__init__(symbol, board)
        self.buttons_2d_list = buttons_2d_list  # Reference to the GUI buttons

    def play(self):
        # Determine whether the game is in GUI mode or CLI mode
        if self.buttons_2d_list:
            self.__play_gui()  # Play in GUI mode
        else:
            # CLI mode logic for the computer player
            print("Player %s turn" % self.get_player_symbol())
            while True:
                col = random.randint(0, self._gboard.get_num_cols() - 1)  # Choose a random column
                if self._gboard.is_space_free(0, col):
                    self._gboard.make_move(col, self.get_player_symbol())  # Make the move
                    break

    def __play_gui(self):
        # Logic for the computer player's turn in GUI mode
        def make_move():
            while True:
                col = random.randint(0, len(self.buttons_2d_list[0]) - 1)  # Choose a random column
                for row in range(len(self.buttons_2d_list) - 1, -1, -1):
                    if self.buttons_2d_list[row][col]["text"] == " ":
                        self.buttons_2d_list[row][col].invoke()  # Simulate a button click
                        return
        # Delay of 2000ms (2 second) before making the move
        self.buttons_2d_list[0][0].after(2000, make_move)

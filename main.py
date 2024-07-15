import tkinter as tk
from tkinter import messagebox, colorchooser
from gameboard import GameBoard
from player import HumanPlayer, ComputerPlayer

class GameGUI:
    def __init__(self):
        # Initialize the main window
        self.mw = tk.Tk()
        self.mw.title("Connect 4")
        self.center_window()
        self.mw.geometry("800x600")
        self.initialize_menu()  # Set up the initial menu

    def center_window(self):
        # Center the window on the screen
        window_width = 800
        window_height = 600
        screen_width = self.mw.winfo_screenwidth()
        screen_height = self.mw.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.mw.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    def initialize_menu(self):
        # Create and configure the menu frame
        self.menu_frame = tk.Frame(self.mw, padx=20, pady=20)
        self.menu_frame.pack()

        # Player 1 settings
        self.player1_label = tk.Label(self.menu_frame, text="Player 1 Symbol (X/O):")
        self.player1_label.grid(row=0, column=0, padx=10, pady=5)
        self.player1_entry = tk.Entry(self.menu_frame)
        self.player1_entry.grid(row=0, column=1, padx=10, pady=5)

        self.player1_color_label = tk.Label(self.menu_frame, text="Player 1 Color:")
        self.player1_color_label.grid(row=1, column=0, padx=10, pady=5)
        self.player1_color_button = tk.Button(self.menu_frame, text="Choose Color", command=self.choose_color1)
        self.player1_color_button.grid(row=1, column=1, padx=10, pady=5)

        # Player 2 settings
        self.player2_label = tk.Label(self.menu_frame, text="Player 2 Symbol (X/O):")
        self.player2_label.grid(row=2, column=0, padx=10, pady=5)
        self.player2_entry = tk.Entry(self.menu_frame)
        self.player2_entry.grid(row=2, column=1, padx=10, pady=5)

        self.player2_color_label = tk.Label(self.menu_frame, text="Player 2 Color:")
        self.player2_color_label.grid(row=3, column=0, padx=10, pady=5)
        self.player2_color_button = tk.Button(self.menu_frame, text="Choose Color", command=self.choose_color2)
        self.player2_color_button.grid(row=3, column=1, padx=10, pady=5)

        # Game mode selection
        self.mode_label = tk.Label(self.menu_frame, text="Game Mode (1: Human vs Human, 2: Human vs Computer):")
        self.mode_label.grid(row=4, column=0, padx=10, pady=5)
        self.mode_entry = tk.Entry(self.menu_frame)
        self.mode_entry.grid(row=4, column=1, padx=10, pady=5)

        # Start button
        self.start_button = tk.Button(self.menu_frame, text="Start Game", command=self.initialize_game)
        self.start_button.grid(row=5, columnspan=2, pady=10)

        # Default colors for the players
        self.p1_color = "#7CB9E8"  # Default color blue
        self.p2_color = "#DE3163"  # Default color red

    def choose_color1(self):
        # Open a color chooser dialog for Player 1
        color = colorchooser.askcolor(title="Choose Player 1 Color")[1]
        if color:
            self.p1_color = color

    def choose_color2(self):
        # Open a color chooser dialog for Player 2
        color = colorchooser.askcolor(title="Choose Player 2 Color")[1]
        if color:
            self.p2_color = color

    def initialize_game(self):
        # Initialize game settings based on user input
        p1_symbol = self.player1_entry.get().upper()
        p2_symbol = self.player2_entry.get().upper()
        mode = self.mode_entry.get()

        # Validate player symbols and game mode
        if p1_symbol not in ['X', 'O'] or p2_symbol not in ['X', 'O'] or p1_symbol == p2_symbol:
            messagebox.showerror("Error", "Invalid symbols. Choose 'X' or 'O' and ensure they are different.")
            return

        if mode not in ['1', '2']:
            messagebox.showerror("Error", "Invalid game mode. Enter 1 or 2.")
            return

        # Destroy menu frame and create game board
        self.menu_frame.destroy()
        self.gboard = GameBoard()
        self.buttons_2d_list = []

        # Create a grid of buttons for the game board
        for row in range(self.gboard.get_num_rows()):
            row_buttons = []
            for col in range(self.gboard.get_num_cols()):
                btn = tk.Button(self.mw, text=" ", width=4, height=2, command=lambda r=row, c=col: self.clicked_btn(r, c))
                btn.grid(row=row, column=col, sticky="nsew")
                self.mw.grid_rowconfigure(row, weight=1)
                self.mw.grid_columnconfigure(col, weight=1)
                row_buttons.append(btn)
            self.buttons_2d_list.append(row_buttons)

        # Create player objects based on game mode
        self.players_lst = [HumanPlayer(p1_symbol, self.gboard)]

        if mode == '1':
            self.players_lst.append(HumanPlayer(p2_symbol, self.gboard))
        else:
            self.players_lst.append(ComputerPlayer(p2_symbol, self.gboard, self.buttons_2d_list))

        self.player_colors = [self.p1_color, self.p2_color]
        self.current_player_index = 0
        self.create_game_board()
        self.update_turn_label()

        # If the first player is a computer, make the initial move
        if isinstance(self.players_lst[self.current_player_index], ComputerPlayer):
            self.players_lst[self.current_player_index].play()

    def create_game_board(self):
        # Create labels and input fields for game play
        self.turn_label = tk.Label(self.mw, text="")
        self.turn_label.grid(row=self.gboard.get_num_rows(), columnspan=self.gboard.get_num_cols(), pady=10)

        self.column_input_label = tk.Label(self.mw, text="Enter column number(0-6):")
        self.column_input_label.grid(row=self.gboard.get_num_rows() + 1, column=0, columnspan=self.gboard.get_num_cols() // 2, pady=10)

        self.column_input_entry = tk.Entry(self.mw)
        self.column_input_entry.grid(row=self.gboard.get_num_rows() + 1, column=self.gboard.get_num_cols() // 2, columnspan=self.gboard.get_num_cols() // 2, pady=10)

        self.column_input_button = tk.Button(self.mw, text="Submit", command=self.submit_column_input)
        self.column_input_button.grid(row=self.gboard.get_num_rows() + 2, column=0, columnspan=self.gboard.get_num_cols(), pady=10)

    def submit_column_input(self):
        # Handle column input from the player
        column = self.column_input_entry.get()
        if column.isdigit() and 0 <= int(column) < self.gboard.get_num_cols():
            self.clicked_btn(int(column), int(column))
        else:
            messagebox.showerror("Error", "Invalid column number. Please enter a valid column.")

    def clicked_btn(self, x, y):
        # Handle button click, make move, check for winner or tie
        p = self.players_lst[self.current_player_index]
        if self.gboard.is_space_free(0, y):
            for row in range(self.gboard.get_num_rows() - 1, -1, -1):
                if self.gboard.is_space_free(row, y):
                    self.gboard.make_move(y, p.get_player_symbol())
                    self.update_button_text(y, p.get_player_symbol())
                    if self.gboard.check_winner():
                        self.highlight_winner()
                        messagebox.showinfo("Winner Info", f"Player {p.get_player_symbol()} is the Winner!")
                        self.show_menu()
                        return
                    elif self.gboard.is_board_full():
                        messagebox.showinfo("Game Over", "The board is full. It's a tie!")
                        self.show_menu()
                        return
                    self.current_player_index = (self.current_player_index + 1) % len(self.players_lst)
                    self.update_turn_label()
                    if isinstance(self.players_lst[self.current_player_index], ComputerPlayer):
                        self.players_lst[self.current_player_index].play()
                    break

    def update_button_text(self, col, element):
        # Update the button text and color when a move is made
        color = self.player_colors[self.current_player_index]
        for row in range(len(self.buttons_2d_list) - 1, -1, -1):
            if self.buttons_2d_list[row][col]["text"] == " ":
                self.buttons_2d_list[row][col]["text"] = element
                self.buttons_2d_list[row][col]["state"] = "disabled"
                self.buttons_2d_list[row][col].config(bg=color, fg='white')
                break

    def highlight_winner(self):
        # Highlight the winning sequence of buttons
        winning_coords = self.gboard.get_winning_coords()
        for row, col in winning_coords:
            self.buttons_2d_list[row][col].config(bg="green", fg='white')

    def update_turn_label(self):
        # Update the label to show the current player's turn
        p = self.players_lst[self.current_player_index]
        color = self.player_colors[self.current_player_index]
        self.turn_label.config(text=f"Player {p.get_player_symbol()}'s turn", bg=color)

    def show_menu(self):
        # Clear the game board and show the menu again
        for widget in self.mw.winfo_children():
            widget.destroy()
        self.initialize_menu()

def main():
    gui = GameGUI()
    gui.mw.mainloop()

if __name__ == "__main__":
    main()

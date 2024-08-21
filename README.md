# Connect 4 Game

## Overview
Welcome to the Connect 4 game, a classic two-player connection game where the objective is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. The game supports two-player mode (Human vs Human) and single-player mode (Human vs Computer).
![Game UI](images/Winner Screen.png)


## Features
- **Game Modes:** Play against another human or challenge the computer in single-player mode.
- **Customizable Player Settings:** Choose your symbol (X/O) and customize your disc color.
- **Dynamic GUI:** Intuitive and visually appealing game board interface.
- **Computer AI:** The computer player selects its moves randomly, providing a fun challenge.

## Getting Started

### Prerequisites
Ensure you have Python installed on your system. This project requires Python 3.x.

### Installation

#### Clone the Repository
```bash
git clone https://github.com/TahirRajpoot/Connect4-Game-Python-Tkinter.git
cd Connect4-Game-Python-Tkinter
```
## Install Required Packages

This game uses `tkinter` for the GUI, which comes pre-installed with most Python distributions. If you don't have it installed, you can install it using:

```bash
pip install tk
```
## How to Play

### Launch the Game:

- Upon starting the game, you'll be greeted with the main menu where you can set up your game.
- Choose symbols for Player 1 and Player 2 (either 'X' or 'O').
- Select colors for each player using the color picker.
- Choose the game mode: `1` for Human vs Human, `2` for Human vs Computer.
  
### Start the Game:

- After configuring your settings, press the "Start Game" button to initialize the board.
- The game board will display, and the current player's turn will be highlighted.
  
### Make a Move:

- Players take turns clicking on the column where they want to drop their disc.
- The game automatically detects when a player wins or if the board is full, declaring a tie if necessary.

## Project Structure

- `main.py`: The entry point for the game.Manages the graphical user interface (GUI) for the game.
- `gameboard.py`: Contains the logic for the game board, including move validation and winner detection.
- `player.py`: Defines the Player, HumanPlayer, and ComputerPlayer classes, handling player interactions.


## Contributions
Contributions are welcome! If you'd like to improve this game, please fork the repository and submit a pull request with your enhancements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- This project is inspired by the classic Connect 4 game.
- Thanks to the open-source community for providing the tools and libraries used in this project.



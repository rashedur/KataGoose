# KataGoose
This repository contains a Python script implementing a simplified version of the traditional "Goose Game". In this game, players take turns rolling dice and moving their pieces along a track. The game includes special rules for encountering geese and bridges, as well as interactions between players when landing on the same space.

## How to Play

  **Setup:** Run the Python script kata_goose.py.

  **Adding Players:** Enter player names when prompted. It requires minimum two players. To start the game, type 'start' after entering at least two player names.

  **Gameplay:** 
  - Players take turns rolling two dice. To roll, enter two numbers separated by a comma or press ENTER to simulate a random roll. 
  - Players move forward according to the sum of the dice roll. 
  - Special rules apply for certain positions:
    * Landing on space 6 (Bridge) allows the player to jump to space 12.
    * Landing on spaces 5, 9, 14, 18, 23, or 27 (Goose) results in the player moving again and adding the roll to their position.
    * If a player lands on a space occupied by another player, the latter is moved back to the position the current player was on.
    * The game ends when a player reaches or exceeds space 63.
  - **Winning:** The first player to reach or exceed space 63 wins the game.


## Classes

  **Player:** Represents a player in the game, with attributes for name and position on the board.

  **KataGoose:** Manages the game logic, including adding players, rolling dice, moving players, handling special spaces, and orchestrating gameplay.

## Repository Contents

  **kata_goose.py:** The main Python script containing the game implementation.

  **README.md (this file):** Provides instructions on how to play the game and an overview of its implementation.

## Running the Game

To play the Goose Game, ensure you have Python v3.10 installed on your system (I used Python 3.10.12). Run the script kata_goose.py in your preferred Python environment.

## Contributors

This project is maintained by Rashedur Rahman. Contributions and suggestions are welcome. Please feel free to submit issues or pull requests.

## License

This project is licensed under the GNU General Public License v3.0.

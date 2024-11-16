# Ladders-and-Snakes
:purple_circle: **Google Mentoring Program Entry:** <br> A collaborative Python-based Ladders and Snakes game that impressed judges with its innovative features, clean code, and engaging gameplay.

> [!IMPORTANT]
> Python Ladders and Snakes: A comprehensive Python implementation of the classic board game. <br> <ins>Features include: </ins>
>- Multiplayer support for up to 4 players
>- Intuitive user interface with separate windows for game setup and gameplay
>- Engaging visuals and sound effects

## [CODE BREAKDOWN](Ladders_and_snakes.py)
### Mandatory imports 
 ```
import random
import turtle
import time
from pygame import mixer
```
# Constants

**Game Board Dimensions and Layout**

* **`sqr_size`**: Size of each square on the board in pixels.
* **`x1`, `y1`**: Coordinates of the top-left corner of the board.
* **`start_buttons_size`**: Size of the start buttons.

**Game Start Point and Initial Cell**

* **`GAME_START_POINT`**: Coordinates of the starting point on the board.
* **`START_CELL`**: The initial cell number for players.

**Player Start Positions**

* **`x_blue`, `y_blue`**: Coordinates of the blue player's start button.
* **`x_green`, `y_green`**: Coordinates of the green player's start button.
* **`x_red`, `y_red`**: Coordinates of the red player's start button.
* **`x_yellow`, `y_yellow`**: Coordinates of the yellow player's start button.

**Start Game Button Position**

* **`x_start_game`, `y_start_game`**: Coordinates of the "Start Game" button.

**Window Size**

* **`WINDOW_SIZE`**: Dimensions of the game window.

**Ladders and Snakes**

* **`LADDERS_SNAKES`**: A dictionary mapping starting cell numbers to ending cell numbers for ladders and snakes.

```
sqr_size = 70
x1 = 180
y1 = 290
start_buttons_size = 50
GAME_START_POINT = (-233.75, -233.75)
START_CELL = 1
step = 52.5
x_blue = -150
y_blue = 0
x_green = x_blue + 1.5 * start_buttons_size
y_green = 0
x_red = x_green + 1.5 * start_buttons_size
y_red = 0
x_yellow = x_red +1.5 * start_buttons_size
y_yellow = 0
x_start_game = -start_buttons_size
y_start_game = -start_buttons_size
WINDOW_SIZE = (550, 750)
LADDERS_SNAKES = {5:27, 17:46, 23:42, 24:18, 32:13, 64:83, 67:46, 72:91, 73:49, 80:58, 94:76}
```
# Variables

**Player Status**

* **`blue_player`, `green_player`, `red_player`, `yellow_player`**: Boolean flags to indicate whether a player of that color has been selected.
* **`min_players_picked`**: Boolean flag to check if the minimum number of players has been selected.

**Game State**

* **`index`**: Integer variable to keep track of the current player's turn.
* **`players`**: List to store information about the selected players.
* **`snakes_ladder_dict`**: Dictionary to store the mapping of starting and ending positions for ladders and snakes.
* **`colors_list`, `colors_list_2`**: Lists to store color information for players.


# Functions

| **Function Name**    | **Purpose** |
| --------- | ------- |
|`add_player_button`   |     	Creates a button for player selection.    |
| `start_buttons`     |     	Sets up the initial screen with player selection buttons.    |
|  `run_buttons`   |   Handles button clicks for player selection and starting the game.      |
|  `dice`    |    Draws the dice on the screen.     |
|  `rand_num`   |   Generates a random dice roll and plays a sound effect.      |
|  `roll_write`    |     Displays the current player and the rolled dice number.    |
|  `find_next_cell_position`   |    Calculates the coordinates of a cell on the board.     |
|  `move_player`    |        Moves the player's token, handles ladders and snakes, and checks for game over.         |
|  `run_player`    |      Handles clicks on the dice to initiate a player's turn.     |
|  `add_player`    |      Adds a new player to the game.     |
|   `register_players`     |     	Registers the selected players for the game.      |
|   `draw_board`   |      Draws the game board and initializes the game.     |
|   `reset_game`    |     Resets the game for a new round.      |


# Main
This code block sets up the main game loop and initializes the game environment.

**Key Steps:**

1. **Screen Setup:**
   Sets the screen size to 550 pixels wide and 750 pixels high.
   ```
   screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])
   ```
2. **Turtle Initialization:**
   Creates three turtle objects:
   * `drawer`: Used for drawing game elements like the board and dice.
   * `writer`: Used for writing text on the screen.
   * `sketch`: Used for drawing buttons and other UI elements. Hides these turtles to make them invisible.
   ```
   drawer = turtle.Turtle()
   drawer.hideturtle()
   writer = turtle.Turtle()
   writer.hideturtle()
   sketch = turtle.Turtle()
   sketch.hideturtle()
   ```
3. **Initial Screen Setup:**
   Calls the `start_buttons()` function to display the initial screen with player selection buttons.
   ```
   start_buttons()
   ```
4. **Event Handling:**
   Sets up a click event handler. Whenever the user clicks on the screen, the `run_buttons` function is called.
   ```
   screen.onclick(run_buttons, btn=1)
   ```
5. **Game Loop:**
   Starts the main game loop using `turtle.mainloop()`. This keeps the window open and listens for user input (clicks) until the user closes the window.
   ```
   turtle.mainloop()
   ```

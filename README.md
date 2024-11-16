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
###Constants

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


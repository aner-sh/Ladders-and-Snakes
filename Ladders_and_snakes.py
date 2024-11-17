import random
import turtle
import time
from pygame import mixer

# Constants
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

# Variables
blue_player = False
green_player = False
red_player = False
yellow_player = False
min_players_picked = False

index = 0
players = []
snakes_ladder_dict = {}
colors_list = []
colors_list_2 = []


# functions
def add_player_button(x, y, image):
    pass
    sketch.hideturtle()
    sketch.speed(100)
    sketch.color("black")
    sketch.penup()
    sketch.goto(x, y)
    sketch.pensize(3)
    sketch.fillcolor("light blue")
    sketch.begin_fill()
    sketch.setheading(0)
    sketch.forward(start_buttons_size)
    sketch.setheading(90)
    sketch.forward(start_buttons_size)
    sketch.setheading(180)
    sketch.forward(start_buttons_size)
    sketch.setheading(270)
    sketch.forward(start_buttons_size)
    sketch.end_fill()
    sketch.goto(x + start_buttons_size / 2,
                y + start_buttons_size / 2)
    screen.register_shape(image)
    sketch.shape(image)
    sketch.stamp()
    sketch.penup()


def start_buttons():
    '''
    Draw player button and allow to select the game players
    :return: None
    '''
    global x_blue, y_blue, x_green, y_green, x_red, y_red, x_yellow, y_yellow, x_start_game, y_start_game, min_players_picked

    screen.bgpic('snakesAndLadders.png')
    add_player_button(x_blue, y_blue, 'player-blue-sl.gif')
    add_player_button(x_green, y_green, 'player-green-sl.gif')
    add_player_button(x_red, y_red, 'player-red-sl.gif')
    add_player_button(x_yellow, y_yellow, 'player-yellow-sl.gif')


    # Continue button
    sketch.hideturtle()
    sketch.color("black")
    sketch.penup()
    sketch.goto(x_start_game, y_start_game)
    sketch.speed(100)
    sketch.pensize(3)
    sketch.fillcolor("orange")
    sketch.begin_fill()
    sketch.setheading(0)
    sketch.forward(start_buttons_size * 1.4)
    sketch.setheading(90)
    sketch.forward(start_buttons_size / 2)
    sketch.setheading(180)
    sketch.forward(start_buttons_size * 1.4)
    sketch.setheading(270)
    sketch.forward(start_buttons_size / 2)
    sketch.end_fill()
    sketch.color("black")
    sketch.goto(start_buttons_size / 4 + x_start_game,
                start_buttons_size / 6 + y_start_game)
    sketch.write("continue", font=("arial", int(start_buttons_size / 6), "bold"))


def run_buttons(y, x):
    global min_players_picked, players, red_player, blue_player, yellow_player, green_player
    if y > x_blue and y < start_buttons_size + x_blue and x > y_blue and x < start_buttons_size + y_blue:
        blue_player = True
        sketch.hideturtle()
        sketch.speed(100)
        sketch.color("black")
        sketch.penup()
        sketch.goto(x_blue, y_blue)
        sketch.speed(100)
        sketch.pensize(3)
        sketch.fillcolor("royalblue")
        sketch.begin_fill()
        sketch.setheading(0)
        for _ in range(4):
            sketch.hideturtle()
            sketch.forward(start_buttons_size)
            sketch.left(90)
        sketch.end_fill()
        sketch.goto(start_buttons_size / 2 + x_blue,
                    start_buttons_size / 2.7 + y_blue)
        sketch.color("white")
        sketch.write("picked",
                     align="center",
                     font=("Arial", int(start_buttons_size / 5), "bold"))
        sketch.penup()
        blue_player = True
        min_players_picked = True

    if y > x_green and y < start_buttons_size + x_green and x > y_green and x < start_buttons_size + y_green:
        green_player = True
        sketch.hideturtle()
        sketch.speed(100)
        sketch.color("black")
        sketch.penup()
        sketch.goto(x_green, y_green)
        sketch.speed(100)
        sketch.pensize(3)
        sketch.fillcolor("mediumseagreen")
        sketch.begin_fill()
        sketch.setheading(0)
        for _ in range(4):
            sketch.forward(start_buttons_size)
            sketch.left(90)
        sketch.end_fill()
        sketch.goto(start_buttons_size / 2 + x_green,
                    start_buttons_size / 2.7 + y_green)
        sketch.color("white")
        sketch.write("picked",
                     align="center",
                     font=("Arial", int(start_buttons_size / 5), "bold"))
        sketch.penup()
        green_player = True
        min_players_picked = True

    if y > x_red and y < start_buttons_size + x_red and x > y_red and x < start_buttons_size + y_red:
        red_player = True
        sketch.hideturtle()
        sketch.speed(100)
        sketch.color("black")
        sketch.penup()
        sketch.goto(x_red, y_red)
        sketch.speed(100)
        sketch.pensize(3)
        sketch.fillcolor("firebrick")
        sketch.begin_fill()
        sketch.setheading(0)
        for _ in range(4):
            sketch.forward(start_buttons_size)
            sketch.left(90)
        sketch.end_fill()
        sketch.goto(start_buttons_size / 2 + x_red,
                    start_buttons_size / 2.7 + y_red)
        sketch.color("white")
        sketch.write("picked",
                     align="center",
                     font=("Arial", int(start_buttons_size / 5), "bold"))
        sketch.penup()
        red_player = True
        min_players_picked = True

    if y > x_yellow and y < start_buttons_size + x_yellow and x > y_yellow and x < start_buttons_size + y_yellow:
        yellow_player = True
        sketch.hideturtle()
        sketch.speed(100)
        sketch.color("black")
        sketch.penup()
        sketch.goto(x_yellow, y_yellow)
        sketch.speed(100)
        sketch.pensize(3)
        sketch.fillcolor("gold")
        sketch.begin_fill()
        sketch.setheading(0)
        for _ in range(4):
            sketch.forward(start_buttons_size)
            sketch.left(90)
        sketch.end_fill()
        sketch.goto(start_buttons_size / 2 + x_yellow,
                    start_buttons_size / 2.7 + y_yellow)
        sketch.color("white")
        sketch.write("picked",
                     align="center",
                     font=("Arial", int(start_buttons_size / 5), "bold"))
        sketch.penup()
        yellow_player = True
        min_players_picked = True

    if y > x_start_game and y < start_buttons_size * 1.5 + x_start_game and x > y_start_game and x < start_buttons_size / 2 + y_start_game and min_players_picked:
        sketch.clear()
        screen.onclick(None)
        draw_board()


def dice():
    drawer.hideturtle()
    drawer.penup()
    drawer.goto(x1, y1)
    drawer.speed(0)
    drawer.pensize(4)
    drawer.fillcolor('light grey')
    drawer.begin_fill()
    drawer.forward(sqr_size)
    drawer.setheading(90)
    drawer.forward(sqr_size)
    drawer.setheading(180)
    drawer.forward(sqr_size)
    drawer.setheading(270)
    drawer.forward(sqr_size)
    drawer.end_fill()
    drawer.penup()


def rand_num():
    '''
    select random bumber between 1-6 and draw the dice number
    :return: None
    '''
    global dice_num

    writer.penup()
    writer.goto(sqr_size / 2.5 + x1, sqr_size / 3.5 + y1)
    writer.color("black")
    mixer.init()


    mixer.music.load(r"roll_dice.mpeg")
    mixer.music.play()


    while mixer.music.get_busy():  # wait for music to finish playing
        for _ in range(4):
            time.sleep(0.08)
            writer.clear()
            dice_num = (random.randint(1, 6))
            writer.write(f"{dice_num}", font=("comic Sans MS", int(sqr_size / 3.2), "bold"))

    return dice_num


def roll_write(index=0):
    color = colors_list[index]
    color2 = colors_list_2[index]

    drawer.penup()
    drawer.speed(0)
    drawer.goto(-250, 290)
    drawer.pencolor("deeppink4")
    drawer.pendown()
    drawer.write("LADDERS & SNAKES", font=("Verdana pro black", 23, "bold"))
    drawer.penup()
    drawer.goto(80, 330)
    drawer.pendown()
    drawer.pencolor(color)
    drawer.write("Dice ➜", font=("Aharoni", 20, "bold"))
    drawer.speed(0)
    drawer.penup()
    drawer.goto(x1, y1)
    drawer.pendown()
    drawer.pencolor(color2)
    drawer.pensize(4)
    drawer.setheading(0)
    drawer.forward(sqr_size)
    drawer.setheading(90)
    drawer.forward(sqr_size)
    drawer.setheading(180)
    drawer.forward(sqr_size)
    drawer.setheading(270)
    drawer.forward(sqr_size)
    drawer.penup()
    drawer.hideturtle()
    drawer.penup()
    drawer.home()


def find_next_cell_position(new_player_cell_number):
    x1 = (new_player_cell_number - 1) % 10
    y1 = (new_player_cell_number - 1) // 10

    if y1 % 2 == 0:
        x = GAME_START_POINT[0] + x1 * step
    else:
        x = -GAME_START_POINT[1] - x1 * step
    y = GAME_START_POINT[0] + y1 * step
    return x, y


def move_player(player, player_cell_number):
    global index

    screen.onclick(None)

    new_player_cell_number = player_cell_number + rand_num()
    if new_player_cell_number > 100:
        new_player_cell_number = 100
    x, y = find_next_cell_position(new_player_cell_number)
    player.goto(x,y)

    if new_player_cell_number in LADDERS_SNAKES.keys():
        time.sleep(0.5)
        new_player_cell_number2 = LADDERS_SNAKES[new_player_cell_number]
        mixer.init()
        if new_player_cell_number2 < new_player_cell_number:
            mixer.music.load(r"slide_down.mpeg")
        else:
            mixer.music.load(r"going_up.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            x, y = find_next_cell_position(new_player_cell_number2)
            time.sleep(0.5)
            player.speed(1)
            player.goto(x, y)
            player.speed(0)
        new_player_cell_number = new_player_cell_number2

    players[index % len(players)][1] = new_player_cell_number

    if index < len(players) - 1:
        index += 1
    else:
        index = 0
    roll_write(index)

    screen.onclick(run_player)

    if new_player_cell_number == 100:
        drawer.goto(-200, 0)
        drawer.pencolor("black")
        drawer.write("Game Over", font=("Varela round", 50, "bold"))
        mixer.init()
        mixer.music.load(r"winning.mp3")
        mixer.music.play()
        while mixer.music.get_busy():  # wait for music to finish playing
            pass

        another_game = screen.textinput(title="another_game", prompt="Type Yes for another game and no to finish game.").title()
        if another_game == "Yes":
            reset_game()
        else:
            screen.onclick(None)

    return new_player_cell_number


def run_player(x, y):
    global index
    if x1 < x < sqr_size + x1 and y1 < y < sqr_size + y1:
        player = players[index % len(players)][0]
        player_cell_number = players[index % len(players)][1]
        move_player(player, player_cell_number)


def add_player(image, color ):
    new_player = turtle.Turtle()
    new_player.penup()
    new_player.speed(0)
    new_player.goto(GAME_START_POINT)
    screen.register_shape(image)
    new_player.shape(image)
    players.append([new_player, START_CELL])
    colors_list.append(color)
    colors_list_2.append(color)


def register_players():
    global blue_player, green_player, red_player, yellow_player, colors_list_2
    if blue_player == True:
        add_player('player-blue-sl.gif', 'blue')

    if green_player == True:
        add_player('player-green-sl.gif', 'green')

    if red_player == True:
        add_player('player-red-sl.gif', 'red')

    if yellow_player == True:
        add_player('player-yellow-sl.gif', 'darkgoldenrod1')


def draw_board():
    bored = turtle.Turtle()
    screen.register_shape("laddersAndSnakesBoard.gif")
    bored.shape("laddersAndSnakesBoard.gif")
    register_players()
    dice()
    roll_write()

    tw = turtle.Screen()
    screen.onclick(run_player)


def reset_game():
    global blue_player, green_player, red_player, yellow_player, min_players_picked, \
        players, snakes_ladder_dict, colors_list, colors_list_2, index, sketch
    screen.clear()
    blue_player = False
    green_player = False
    red_player = False
    yellow_player = False
    min_players_picked = False

    index = 0
    players = []
    snakes_ladder_dict = {}
    colors_list = []
    colors_list_2 = []

    drawer.home()
    writer.home()
    sketch = turtle.Turtle()
    sketch.hideturtle()

    start_buttons()

    screen.onclick(run_buttons, btn=1)


SCREEN_SIZE = (550, 750)
# main
# Create turtles to draw game objects on screen

drawer = turtle.Turtle()
drawer.hideturtle()
writer = turtle.Turtle()
writer.hideturtle()
screen = turtle.Screen()
screen.setup(SCREEN_SIZE[0], SCREEN_SIZE[1])
sketch = turtle.Turtle()
sketch.hideturtle()
# Draw initial screen to select players
start_buttons()
# Manage mouse click event
screen.onclick(run_buttons, btn=1)
turtle.mainloop()

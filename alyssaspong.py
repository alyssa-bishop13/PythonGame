from random import choice, random
import turtle
from turtle import *
from freegames import vector
#Source: freegames-pong. classic arcade game https://grantjenks.com/docs/freegames/pong.html

#I have rewrote and personalized the code, changing colours, frame rate, and adding a start menu with instructions, and a game over / restart menu.

#window
wn = turtle.Screen()
wn.title("Alyssa's PONG")
setup(420, 420, 370, 0)
bgcolor("#0f0c24")

#info page
info = turtle.Turtle()
info.hideturtle()
info.color("white")
info.penup()
info.goto(0, 0)
info.write(
    "Welcome to Alyssa's PONG!\n\n"
    "Use 'W' / 'S' for left paddle\n"
    "Use 8 / 2 for right paddle\n"
    "Press SPACE to start!",
    align="center",
    font=("Arial", 16, "normal")
)

def value():
    return (3 + random() * 2) * choice([1, -1])

#game
ball = vector(0, 0)
aim = vector(value(), value())
state = {1: 0, 2: 0}
game_running = False #stops game from running before space

def move(player, change):
    if game_running:
        state[player] += change

def rectangle(x, y, width, height):
    up()
    goto(x, y)
    down()
    begin_fill()
    for count in range(2):
        forward(width)
        left(90)
        forward(height)
        left(90)
    end_fill()

def draw():
    clear()
    color("#c1436d")#paddle color(pink)
    rectangle(-200, state[1], 10, 50)
    rectangle(190, state[2], 10, 50)

    ball.move(aim)
    x = ball.x
    y = ball.y

    up()
    goto(x, y)
    color("#ffdd44") #ball color (yellow)
    dot(10)
    update()

    if y < -200 or y > 200:
        aim.y = -aim.y

    if x < -185:
        low = state[1]
        high = state[1] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            game_over()
            return

    if x > 185:
        low = state[2]
        high = state[2] + 50
        if low <= y <= high:
            aim.x = -aim.x
        else:
            game_over()
            return

    ontimer(draw, 20) #changed frame rate

#game over / restart menu
def game_over():
    global game_running
    game_running = False
    info.goto(0, 0)
    info.write(
        "Game Over!\nPress SPACE to restart",
        align="center",
        font=("Arial", 16, "normal"))

def start_game():
    info.clear()
    global aim, ball, state, game_running
    ball = vector(0, 0)
    aim = vector(value(), value())
    state = {1: 0, 2: 0}
    game_running = True

    setup(420, 420, 370, 0)
    hideturtle()
    listen()
    onkey(lambda: move(1, 30), 'w')
    onkey(lambda: move(1, -30), 's')
    onkey(lambda: move(2, 30), '8')
    onkey(lambda: move(2, -30), '2')

    tracer(False)
    draw()

wn.listen()
wn.onkey(start_game, "space")
done()

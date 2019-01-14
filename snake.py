import turtle
import time

delay = 0.2

# screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('#0a6c03')
wn.setup(width=600, height=600)
wn.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color('#00cccc')
head.penup()
head.goto(0, 0)
head.direction = 'right'

# functions


def move():
    if head.direction == 'up':
        head.sety(head.ycor() + 20)
    elif head.direction == 'down':
        head.sety(head.ycor() - 20)
    elif head.direction == 'left':
        head.setx(head.xcor() - 20)
    elif head.direction == 'right':
        head.setx(head.xcor() + 20)


def move_up():
    head.direction = 'up'


def move_down():
    head.direction = 'down'


def move_left():
    head.direction = 'left'


def move_right():
    head.direction = 'right'

# keybindings
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")


# main game loop
while True:
    wn.update()
    move()
    time.sleep(delay)


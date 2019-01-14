import turtle
import time
import random

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

# snake body color 009a9a

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('#cd6700')
food.penup()
food.setposition(random.randint(-275, 275), random.randint(-275, 275))
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

# scoring
score = 0
snake_score = "Score: %s" % score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-150, 275)
score_pen.write(snake_score, False, align="center", font=("Mono", 14, "bold"))
score_pen.hideturtle()

high_score = 0
snake_high_score = "High Score: %s" % high_score
high_score_pen = turtle.Turtle()
high_score_pen.speed(0)
high_score_pen.color("white")
high_score_pen.penup()
high_score_pen.setposition(150, 275)
high_score_pen.write(snake_high_score, False, align="center", font=("Mono", 14, "bold"))
high_score_pen.hideturtle()

# main game loop
while True:
    wn.update()
    if head.distance(food) < 20:
        # snake has eaten food
        score += 1
        score_pen.clear()
        snake_score = "Score: %s" % score
        score_pen.write(snake_score, False, align="center", font=("Mono", 14, "bold"))
        food.setposition(random.randint(-275, 275), random.randint(-275, 275))
        if delay > 0.01:
            delay -= 0.02
    move()
    time.sleep(delay)


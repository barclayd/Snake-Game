import turtle
import time
import random
import pickle

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
head.color('#00cece')
head.penup()
head.goto(0, 0)
head.direction = 'right'

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('#cd6700')
food.penup()
food.setposition(random.randint(-275, 275), random.randint(-275, 275))
head.direction = 'right'


# snake body growth
segments = []

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
    if head.direction != 'down':
        head.direction = 'up'


def move_down():
    if head.direction != 'up':
        head.direction = 'down'


def move_left():
    if head.direction != 'right':
        head.direction = 'left'


def move_right():
    if head.direction != 'left':
        head.direction = 'right'


def random_food():
    food.setposition(random.randint(-275, 275), random.randint(-275, 275))


def set_new_score():
    score_pen.clear()
    snake_score = "Score: %s" % score
    score_pen.write(snake_score, False, align="center", font=("Mono", 14, "bold"))


def set_high_score():
    global snake_high_score
    snake_high_score = "High Score: %s" % high_score
    high_score_pen = turtle.Turtle()
    high_score_pen.speed(0)
    high_score_pen.color("#001c1c")
    high_score_pen.penup()
    high_score_pen.setposition(150, 275)
    high_score_pen.clear()
    high_score_pen.write(snake_high_score, False, align="center", font=("Mono", 14, "bold"))
    high_score_pen.hideturtle()


def save_high_score_data():
    highest_score = [high_score]
    pickle.dump(highest_score, open("data.txt", "wb"))


def load_high_score_data():
    global high_score
    global game_status
    loaded_highest_score = pickle.load(open("data.txt", "rb"))
    print(loaded_highest_score[-1])
    if int(loaded_highest_score[-1]) > high_score:
        high_score = int(loaded_highest_score[-1])
        set_high_score()
        game_status = 'loaded'


def end_game():
    head.direction = 'stop'
    global game_status
    game_status = False
    time.sleep(1)
    head.setposition(0, 0)
    # hide segments
    for segment in segments:
        segment.setposition(1000, 1000)
    segments.clear()
    random_food()
    global score
    global high_score
    global snake_high_score
    global delay
    if score > high_score:
        high_score = score
        save_high_score_data()
        set_high_score()
    score = 0
    set_new_score()
    delay = 0.2


# keybindings
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# game status
game_status = 'loading'

# scoring
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-150, 275)
set_new_score()
score_pen.hideturtle()

high_score = 0

# main game loop
while True:
    wn.update()
    if game_status == 'loading':
        load_high_score_data()

    # border checking
    if head.xcor() < -290 or head.xcor() > 290 or head.ycor() > 290 or head.ycor() < -290:
        end_game()
    # snake has eaten food
    if head.distance(food) < 20:
        score += 1
        set_new_score()
        random_food()
        if delay > 0.03 and score < 7:
            delay -= 0.02
        elif score > 8 and delay > 0.03:
            delay /= 1.1
        elif delay < 0.03:
            delay += 0

        # add body segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color('#009b9b')
        new_segment.penup()
        segments.append(new_segment)

    # move end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].setposition(x, y)

    # move 1st segment to where the head is
    if len(segments) > 0:
        segments[0].setposition(head.xcor(), head.ycor())

    move()

    # check for snake collision with own body segment
    for segment in segments:
        if segment.distance(head) < 20:
            end_game()

    time.sleep(delay)


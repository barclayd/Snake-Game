import turtle
import time
import random
import pickle

delay = 0.2
file = "data.dat"
# screen
wn = turtle.Screen()
wn.title('Snake Game')
wn.bgcolor('#000')
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
head.hideturtle()

# snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color('#cd6700')
food.penup()
food.setposition(random.randint(-275, 275), random.randint(-275, 275))
food.hideturtle()

# snake body growth
segments = []

# functions


def move():
    global game_speed
    if head.direction == 'up':
        head.sety(head.ycor() + game_speed)
    elif head.direction == 'down':
        head.sety(head.ycor() - game_speed)
    elif head.direction == 'left':
        head.setx(head.xcor() - game_speed)
    elif head.direction == 'right':
        head.setx(head.xcor() + game_speed)


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
    global high_score_pen
    high_score_pen = turtle.Turtle()
    high_score_pen.speed(0)
    if game_status == 'loading':
        high_score_pen.color('#0059b3')
    else:
        high_score_pen.color("#001c1c")
    high_score_pen.penup()
    high_score_pen.setposition(150, 275)
    high_score_pen.clear()
    high_score_pen.write(snake_high_score, False, align="center", font=("Mono", 14, "bold"))
    high_score_pen.hideturtle()


def save_high_score_data():
    highest_score = [high_score]
    pickle.dump(highest_score, open(file, "wb"))


def load_high_score_data():
    global high_score
    global game_status
    loaded_highest_score = pickle.load(open(file, "rb"))
    if int(loaded_highest_score[-1]) >= high_score:
        high_score = int(loaded_highest_score[-1])
        print(high_score)
        set_high_score()
        # game_status = 'loaded'
    global data_status
    data_status = 'loaded'


def end_game():
    head.direction = 'stop'
    global game_status
    game_status = 'ended'
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
        high_score_pen.clear()
        save_high_score_data()
        set_high_score()
    score = 0
    set_new_score()
    if game_level == 'Easy':
        delay = 0.24
    elif game_level == 'Medium':
        delay = 0.09
    elif game_level == 'Hard':
        delay = 0.05

    game_status = 'loaded'


def start_game():
    global game_status
    if game_status == 'loading':
        game_status = 'loaded'


def load_game_elements():
    # clear welcome text
    welcome_pen.clear()
    intro_pen.clear()
    reset_pen.clear()
    change_difficulty_pen.clear()
    # load head and food
    head.showturtle()
    food.showturtle()
    wn.bgcolor('#0a6c03')
    high_score_pen.clear()
    high_score_pen.color("#001c1c")
    high_score_pen.write(snake_high_score, False, align="center", font=("Mono", 14, "bold"))


def reset_high_score():
    global reset_check_pen
    global snake_high_score
    global high_score
    if high_score_reset:
        reset_check_pen.clear()
        highest_score = [0]
        pickle.dump(highest_score, open(file, "wb"))
        high_score_pen.clear()
        high_score = 0
        print(snake_high_score)
        snake_high_score = "High Score: %s" % high_score
        high_score_pen.write(snake_high_score, False, align="center", font=("Mono", 14, "bold"))


def reset_high_score_check():
    global high_score_reset
    if game_status == 'loading':
        reset_pen.clear()
        high_score_reset = True
        reset_check_pen.write(reset_message, False, align="center", font=("Verdana", 14, "bold"))


def easy():
    global delay
    if game_status == 'loading':
        delay = 0.28
        update_difficulty('Easy')


def medium():
    global delay
    global game_level
    global game_speed
    if game_status == 'loading':
        delay = 0.12
        game_speed = 25
        update_difficulty('Medium')


def hard():
    global delay
    global game_speed
    if game_status == 'loading':
        delay = 0.06
        game_speed = 30
        update_difficulty('Hard')


def update_difficulty(level):
    global game_level
    global difficulty_message
    difficulty_pen.clear()
    game_level = level
    difficulty_message = "Difficulty: %s" % game_level
    difficulty_pen.write(difficulty_message, False, align="center", font=("Mono", 14, "bold"))


# keybindings
wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")
wn.onkeypress(start_game, "space")
wn.onkeypress(reset_high_score_check, "r")
wn.onkeypress(reset_high_score, "s")
wn.onkeypress(easy, "e")
wn.onkeypress(medium, "m")
wn.onkeypress(hard, "h")



# game status
game_status = 'loading'
data_status = 'loading'
high_score_reset = False
game_level = 'Medium'
game_speed = 20

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

# game welcome

welcome_message = "Snake Game"
welcome_pen = turtle.Turtle()
welcome_pen.speed(0)
welcome_pen.color("blue")
welcome_pen.penup()
welcome_pen.setposition(0, 100)
welcome_pen.write(welcome_message, False, align="center", font=("Verdana", 42, "bold"))
welcome_pen.hideturtle()

intro_message = "Press Space to Begin"
intro_pen = turtle.Turtle()
intro_pen.speed(0)
intro_pen.color("white")
intro_pen.penup()
intro_pen.setposition(0, -50)
intro_pen.write(intro_message, False, align="center", font=("Verdana", 24, "bold"))
intro_pen.hideturtle()

difficulty_message = "Difficulty: %s" % game_level
difficulty_pen = turtle.Turtle()
difficulty_pen.speed(0)
difficulty_pen.color("white")
difficulty_pen.penup()
difficulty_pen.setposition(0, 275)
difficulty_pen.write(difficulty_message, False, align="center", font=("Mono", 14, "bold"))
difficulty_pen.hideturtle()

change_difficulty_message = "\tChange difficulty by pressing:\n      'e' for Easy | 'm' for Medium | 'h' for hard"
change_difficulty_pen = turtle.Turtle()
change_difficulty_pen.speed(0)
change_difficulty_pen.color("#006633")
change_difficulty_pen.penup()
change_difficulty_pen.setposition(0, -175)
change_difficulty_pen.write(change_difficulty_message, False, align="center", font=("Verdana", 16, "bold"))
change_difficulty_pen.hideturtle()

reset_message_check = "Press R to reset high score"
reset_pen = turtle.Turtle()
reset_pen.speed(0)
reset_pen.color("#aaaaaa")
reset_pen.penup()
reset_pen.setposition(0, -250)
reset_pen.write(reset_message_check, False, align="center", font=("Verdana", 11, "bold"))
reset_pen.hideturtle()


reset_message = "Are you sure you want to reset high score?\n\t     Press 's' to confirm"
reset_check_pen = turtle.Turtle()
reset_check_pen.speed(0)
reset_check_pen.color("#bb2124")
reset_check_pen.penup()
reset_check_pen.setposition(0, -250)
reset_check_pen.hideturtle()


# main game loop
while True:
    wn.update()
    if game_status == 'loading' and data_status == 'loading':
        load_high_score_data()
    if game_status == 'loaded':
        load_game_elements()
        # border checking
        if head.xcor() < -290 or head.xcor() > 290 or head.ycor() > 290 or head.ycor() < -290:
            end_game()
        # snake has eaten food
        if head.distance(food) < 20:
            score += 1
            set_new_score()
            random_food()
            if delay > 0.03 and game_level == 'Easy':
                delay -= 0.01
                game_speed += 0.5
            if delay > 0.03 and game_level == 'Medium':
                delay -= 0.02
            if delay > 0.03 and game_level == 'Hard':
                delay -= 0.02
            elif score > 8 and game_level == 'Medium' and delay > 0.03:
                delay /= 1.1
                game_speed += 1
            elif 5 < score < 10 and game_level == 'Hard' and delay > 0.1:
                delay /= 1.3
                game_speed += 4
            elif score >= 10 and game_level == 'Hard':
                delay = 0
            elif delay < 0.004 and game_level == 'Easy':
                delay = 0
            elif delay < 0.003 and game_level == 'Medium':
                delay = 0

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


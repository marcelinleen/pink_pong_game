import turtle # for grafic

win = turtle.Screen()
win.title("Pink Pong")
win.bgcolor("pink")
win.setup(width=800, height=600)
win.tracer(0) #stop updating

# score
score_a = 0
score_b = 0

# paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("black")
pad_a.shapesize(stretch_wid=5, stretch_len=0.5)
pad_a.penup()
pad_a.goto(-350, 0)

# paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("black")
pad_b.shapesize(stretch_wid=5, stretch_len=0.5)
pad_b.penup()
pad_b.goto(350, 0)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 24, 'normal'))


# function to moving paddles
def pad_a_up():
    y = pad_a.ycor()
    y += 20
    pad_a.sety(y)

def pad_a_down():
    y = pad_a.ycor()
    y -= 20
    pad_a.sety(y)

def pad_b_up():
    y = pad_b.ycor()
    y += 20
    pad_b.sety(y)

def pad_b_down():
    y = pad_b.ycor()
    y -= 20
    pad_b.sety(y)

# keyboard binding
win.listen()
win.onkeypress(pad_a_up, 'w')
win.onkeypress(pad_a_down, 's')
win.onkeypress(pad_b_up, 'Up')
win.onkeypress(pad_b_down, 'Down')

# main game loop
while True:
    win.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align='center', font=("Courier", 24, 'normal'))

    # paddles and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 50 and ball.ycor() > pad_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 50 and ball.ycor() > pad_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    
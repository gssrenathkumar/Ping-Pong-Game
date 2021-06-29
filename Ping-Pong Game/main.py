import turtle as t
from turtle import Screen, Turtle
from time import sleep


class paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


class ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_coor = self.xcor() + self.x_move
        y_coor = self.ycor() + self.y_move
        self.goto(x_coor, y_coor)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1

    def refresh(self):
        self.goto(0, 0)
        self.x_bounce()


class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        score.lscore += 1
        self.update_scoreboard()

    def r_point(self):
        score.rscore += 1
        self.update_scoreboard()


r_paddle = paddle((350, 0))
l_paddle = paddle((-350, 0))
ball = ball()
screen = Screen()
score = score_board()
screen.bgcolor("black")
screen.setup(height=600, width=800)

screen.tracer(0)
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    if ball.xcor() > 380:
        ball.refresh()
        score.l_point()
    if ball.xcor() < -380:
        ball.refresh()
        score.r_point()

screen.exitonclick()

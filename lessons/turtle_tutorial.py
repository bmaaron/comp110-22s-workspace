from turtle import Turtle, colormode, done
leo: Turtle = Turtle()
bob: Turtle = Turtle()

leo.penup()
leo.goto(0, 0)
leo.pendown()
colormode(255)
leo.begin_fill()
# leo.pencolor("pink")
# leo.fillcolor(22, 255, 0)
leo.color("green", "gray")
leo.speed(25)
leo.hideturtle()
i: int = 0
while (i < 3):
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()


bob.penup()
bob.goto(0, 0)
bob.pendown()
colormode(255)
bob.color(230, 132, 14)
bob.speed(50)
bob.hideturtle()

side_length: float = 300

i: int = 0
while (i < 200):
    bob.forward(side_length)
    bob.left(122.5)
    side_length = side_length * 0.97
    i = i + 1

done()
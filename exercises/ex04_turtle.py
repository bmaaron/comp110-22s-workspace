"""Some happy accidents with help from turtles."""

__author__ = "730530687"

from turtle import Turtle, colormode, done, tracer, update

"""Breaking up complex functions is demonstrated at ln. 78 & 95 -- these functions were one but were split into two for ease of use."""
"""Trying something fun is demonstrated at ln. 134 where I randomize the coords for the blades of grass. It is also demonstrated at ln. 85 where the radius of the circles
for the clouds is randomized creating unique patterns that are different from each other and each time the program is run."""


def main() -> None:
    """Entry point of scene."""
    tracer(0, 0)
    sun_turtle: Turtle = Turtle()
    sky_turtle: Turtle = Turtle()
    circle_turtle: Turtle = Turtle()    
    mtn_turtle: Turtle = Turtle()
    grass_turtle: Turtle = Turtle()
    blade_turtle: Turtle = Turtle()
    draw_background(sky_turtle)
    draw_sun(sun_turtle, 150, 230)
    draw_mnts(mtn_turtle, "#5D5B5B", -400, -100, 350)
    draw_mnts(mtn_turtle, "#474A48", 75, -100, 200)
    draw_mnts(mtn_turtle, "#5D5B5B", 150, -100, 250)
    draw_mnts(mtn_turtle, "#8B8484", -250, -100, 450)
    draw_cloud(circle_turtle, -250, 300)
    draw_cloud(circle_turtle, 50, 250)
    draw_cloud(circle_turtle, -150, 230)
    draw_grass(grass_turtle, -400, -100)
    draw_grass_blades(blade_turtle)
    update()
    done()
      

def draw_sun(sun_turtle: Turtle, x: float, y: float) -> None:
    """Draw a cool sun in the top right corner."""
    sun_turtle.penup()
    sun_turtle.goto(x, y)
    sun_turtle.setheading(0.0)
    sun_turtle.pendown()
    colormode(255)
    sun_turtle.color("orange", "yellow")
    sun_turtle.speed(0)
    sun_turtle.begin_fill()
    for i in range(73):
        sun_turtle.fd(200)
        sun_turtle.left(175)
    sun_turtle.end_fill()
    sun_turtle.hideturtle()


def draw_background(sky_turtle: Turtle) -> None:
    """Draw a blue sky background."""
    colormode(255)
    sky_turtle.getscreen().bgcolor(14, 182, 230)  # the getscreen and bgcolor functions are from the official python.org turtle page
    sky_turtle.hideturtle()


def draw_mnts(mtn_turtle: Turtle, color: str, x: float, y: float, size: int) -> None:  # size is just the fd length the turtle travels which scales up or down 
    """Draws some lovely little mountains."""
    """The color of the mtns are  different and can be changed in this fxn's call in the main block."""
    """This is a procedure that is run more than once."""
    mtn_turtle.color(color)
    mtn_turtle.penup()
    mtn_turtle.goto(x, y)
    mtn_turtle.pendown()
    mtn_turtle.setheading(0.0)
    colormode(255)
    mtn_turtle.begin_fill()
    mtn_turtle.speed(0)
    i: int = 0
    for i in range(3):
        mtn_turtle.fd(size)
        mtn_turtle.left(120)
        i += 1
    mtn_turtle.end_fill()
    mtn_turtle.hideturtle()


def draw_circle_for_clouds(circle_turtle: Turtle, color: str) -> None:
    """Draws circles which will be randomized to create a cloud."""
    """This is something fun - the clouds will never the the same in each iteration, as well as each cloud being different than the others due to the 
    random aspect of its formation"""
    """This is also a def that I broke up from the draw_cloud def to simplify things. Otherwise this code for clouds would be longer and 
    harder to follow"""
    from random import randint
    radius: int = randint(10, 35)
    circle_turtle.begin_fill()
    circle_turtle.circle(radius)
    circle_turtle.pencolor("white")
    circle_turtle.color("white")
    circle_turtle.end_fill()
    circle_turtle.speed(0)
    circle_turtle.hideturtle()


def draw_cloud(circle_turtle: Turtle, x: float, y: float) -> None:
    """Uses the draw_circle_for_clouds fxn to draw a cloud."""
    """Calls the draw_circle_for_clouds def which breaks up a larger fxn and allows for the coder to follow easier."""
    circle_turtle.penup()
    circle_turtle.pencolor("white")
    circle_turtle.goto(x, y)
    circle_turtle.pendown()
    circle_turtle.hideturtle()
    for i in range(9):
        draw_circle_for_clouds(circle_turtle, "white")
        circle_turtle.left(60)
        i += 1


def draw_grass(grass_turtle: Turtle, x: float, y: float) -> None:
    """Draws a rectangle which is grass in the foreground."""
    grass_turtle.penup()
    grass_turtle.goto(x, y)
    grass_turtle.pendown()
    grass_turtle.color("green")
    grass_turtle.begin_fill()
    grass_turtle.speed(0)
    i: int = 0

    while i < 4:
        grass_turtle.fd(800)
        grass_turtle.right(90)
        i += 1
    grass_turtle.end_fill()


def draw_grass_blades(blade_turtle: Turtle) -> None:
    """Draws random blades of grass across the green foreground. Uses random coords so that the blades are spread out and look somewhat natural."""
    colormode(255)
    blade_turtle.color(8, 81, 36)
    blade_turtle.penup()
    blade_turtle.goto(-150, -150)
    blade_turtle.speed(0)
    for i in range(1000):
        from random import randint
        x: int = randint(-400, 400)
        y: int = randint(-400, -150)
        blade_turtle.goto(x, y)
        blade_turtle.pendown()
        blade_turtle.setheading(90.0)
        blade_turtle.fd(35)
        blade_turtle.penup()
        i += 1
    blade_turtle.hideturtle()


if __name__ == "__main__": 
    main()
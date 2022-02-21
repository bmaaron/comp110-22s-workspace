"""Some happy accidents with help from turtles."""

__author__ = "730530687"

from turtle import Turtle, colormode, done


def main() -> None:
    """Entry point of scene."""
    sun_turtle: Turtle = Turtle()
    sky_turtle: Turtle = Turtle()
    # cloud_turtle: Turtle = Turtle()
    mtn_turtle: Turtle = Turtle()
    draw_background(sky_turtle)
    draw_sun(sun_turtle, 150, 200)
    # draw_clouds(cloud_turtle, 0, 0, "white")
    draw_mnts(mtn_turtle, -400, -100, 350)
    draw_mnts(mtn_turtle, 150, -100, 250)
    draw_mnts(mtn_turtle, -250, -100, 450)
    done()
      

def draw_sun(sun_turtle: Turtle, x: float, y: float) -> None:
    """Draw a cool sun in the top right corner."""
    sun_turtle.penup()
    sun_turtle.goto(x, y)
    sun_turtle.setheading(0.0)
    sun_turtle.pendown()
    colormode(255)
    sun_turtle.color("orange", "yellow")
    sun_turtle.speed(1000)
    sun_turtle.begin_fill()

    for i in range(80):
        sun_turtle.fd(200)
        sun_turtle.left(169)
    sun_turtle.end_fill()
    sun_turtle.hideturtle()


def draw_background(sky_turtle: Turtle) -> None:
    """Draw a blue sky background."""
    colormode(255)
    sky_turtle.getscreen().bgcolor(14, 182, 230)  # the getscreen and bgcolor functions are from the official python.org turtle page
    sky_turtle.hideturtle()


def draw_mnts(mtn_turtle: Turtle, x: float, y: float, size: int) -> None:  # size is just the fd length the turtle travels which scales up or down 
    """Draws some lovely little mountains."""
    mtn_turtle.penup()
    mtn_turtle.goto(x, y)
    mtn_turtle.pendown()
    mtn_turtle.setheading(0.0)
    colormode(255)
    mtn_turtle.begin_fill()
    mtn_turtle.color(139, 132, 132)
    mtn_turtle.speed(100)
    i: int = 0
    for i in range(3):
        mtn_turtle.fd(size)
        mtn_turtle.left(120)
        i += 1
    mtn_turtle.end_fill()
    mtn_turtle.hideturtle()


if __name__ == "__main__": 
    main()
import turtle as t
import random 

turtle = t.Turtle()
t.colormode(255)


def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    random_color = (red,green,blue)
    return random_color

def draw_triangle():
    turtle.forward(100)
    turtle.right(120)


def draw_spirograph(gap):
    for _ in range(int(360/gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading()+gap)



draw_spirograph(10)

screen = t.Screen()
screen.exitonclick()
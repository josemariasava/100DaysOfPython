import turtle as t
import random 

directions = [0,90,180,270]

def random_color():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    random_color = (red,green,blue)
    return random_color


tim = t.Turtle()
t.colormode(255)

tim.pensize(10)
tim.speed("normal")

for _ in range(300):
    tim.color(random_color())
    tim.forward(40)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
import turtle as t
import random 

directions = [0,90,180,270]
colours = ["medium orchid","indigo","chocolate","firebrick","forest green","navy","gold","hot pink"]

tim = t.Turtle()
tim.pensize(10)
tim.speed("normal")

for _ in range(300):
    tim.color(random.choice(colours))
    tim.forward(40)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
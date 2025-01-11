from turtle import Turtle
from turtle import Screen
import random   

def draw_square(turtle):
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)

def draw_dashed(turtle):
    for _ in range(15):
        turtle.forward(10)
        turtle.penup()
        turtle.forward(10)
        turtle.pendown()

def draw_shapes(turtle,num_side):
    angle = 360/num_side
    for _ in range(num_side):
        turtle.forward(100)
        turtle.right(angle)



colours = ["medium orchid","indigo","chocolate","firebrick","forest green","navy","gold","hot pink"]

my_turtle = Turtle() # create an object from class Turtle() 
# use methods from Turtle class 
my_turtle.shape("turtle")
my_turtle.color("dark blue")
#my_turtle.forward(100)
#my_turtle.right(90)

#draw_square(my_turtle)
#draw_dashed(my_turtle)

for side in range (3,10):
    my_turtle.color(random.choice(colours))
    draw_shapes(my_turtle,side)

my_screen = Screen() # create an object from class Screen() 
my_screen.exitonclick()
my_screen.title("Day18 - welcome to turtle")
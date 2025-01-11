from turtle import Turtle,Screen, TK
import random 

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Enter the color of your bet: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles=[]
starting = -300
race_on = False

for color in colors:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    turtles.append(new_turtle)


for turtle in turtles:
    turtle.goto(x=-250,y=starting)
    starting += 90


if user_bet:
    race_on = True

while race_on:
    
    for turtle in turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner! ")
            else:
                print(f"You lose! The {winning_color} turtle is the winner! ")
            race_on = False

        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()

### Passing function as an argument - Higher order function

> Because functions are objects we can pass them as arguments to other functions. Functions that can accept other functions as arguments are also called
> 

```python
# Python program to illustrate functions 
# can be passed as arguments to other functions 
def shout(text): 
    return text.upper() 

def whisper(text): 
    return text.lower() 

def greet(func): 
    # storing the function in a variable 
    greeting = func("Hi, I am created by a function passed as an argument.") 
    print(greeting)

greet(shout) 
greet(whisper)
```
---

### Hetch a Sketch with turtle and listen()

```python
from turtle import Turtle,Screen

t = Turtle()
s = Screen() 

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def move_counter_clockwise():
    new_heading = t.heading() + 10
    t.setheading(new_heading)

def move_clockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(key="w", fun=move_forward)
s.onkey(key="s", fun=move_backward)
s.onkey(key="a", fun=move_counter_clockwise)
s.onkey(key="d", fun=move_clockwise)
s.onkey(key="c", fun=clear)

s.exitonclick()
```
---

### Turtle race

```python
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

```
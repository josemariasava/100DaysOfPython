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
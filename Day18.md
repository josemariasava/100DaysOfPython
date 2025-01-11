[turtle — Turtle graphics](https://docs.python.org/3/library/turtle.html)

### Importing modules with from … import

```python
from turtle import Turtle
from turtle import Screen
```

In this way to use the two classes, Turtle and Screen we can do 

```python
my_t = Turtle()
my_s = Screen() 
```

Otherwise importing only the main module 

```python
import turtl

my_t = turtle.Turtle() 
my_s = turtle.Screen() 
```

### Alias name

Aliases are alternative names for existing Python modules or objects. Assigning aliases can make Python programs easier to read and write.

```python
import turtle as t 

my_t = t.Turtle() 
```

---

### Tuples

> Tuples are used to store multiple items in a single variable.
> 
> 
> Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
> 
> A tuple is a collection which is ordered and unchangeable.
> 
> Tuples are written with round brackets.
> 
> Tuple items are ordered, unchangeable, and allow duplicate values.
> 
> Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
> 

```python
thistuple = ("apple", "banana", "cherry")
print(thistuple)
```

> **Unchangeable**
> 
> 
> Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
> 

---

### Spirograph with turtle

```python
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
```
---

### Hirst Painting dots

```python
import colorgram
import turtle as t
import random 

#list of color 
rgb = [(244, 234, 224), (215, 149, 92), (246, 229, 236), (231, 243, 237), (53, 106, 136), 
       (221, 232, 240), (151, 85, 55), (124, 162, 187), (142, 68, 94), (201, 132, 155), 
       (216, 87, 61), (166, 151, 47), (54, 122, 87), (196, 87, 117), (123, 179, 153), 
       (26, 50, 76), (228, 201, 117), (75, 159, 121), (54, 42, 29), (40, 56, 107), 
       (238, 162, 184), (56, 35, 50), (119, 35, 57), (51, 158, 177)]

#Used just to extract the colors
#colors = colorgram.extract('Day18/image.jpg',30)
#for color in colors: 
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb.append(new_color)
#
#print(rgb)

t.colormode(255)
my_t = t.Turtle()
my_t.speed("fast")
my_t.penup()
my_t.hideturtle()
my_t.setheading(255)
my_t.forward(300)
my_t.setheading(0)
dots_n = 100 

for dot in range (1,dots_n+1):
    my_t.dot(20,random.choice(rgb))
    my_t.forward(50)

    if dot % 10 == 0:
        my_t.setheading(90)
        my_t.forward(50)
        my_t.setheading(180)
        my_t.forward(500)
        my_t.setheading(0)

screen = t.Screen()
screen.exitonclick()
```
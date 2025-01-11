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
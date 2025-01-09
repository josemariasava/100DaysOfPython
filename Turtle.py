import turtle # import module 

timmy = turtle.Turtle() # creating an object [timmy] of class Turtle() 
print(timmy) # turtle.Turtle object at 0x70f15d7fe210> Console output of print of an object, is the memory address where is stored

# call methods from the class Turtle()
timmy.shape("turtle") 
timmy.color("coral") 
timmy.forward(100)

my_screen = turtle.Screen() # creating an object [my_screen] of class Screen()
print(my_screen.canvheight)

my_screen.exitonclick() 
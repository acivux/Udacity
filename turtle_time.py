__author__ = 'jannie'

import turtle


def create_turtle(shape, color, speed):
    temp_turtle = turtle.Turtle()
    temp_turtle.shape(shape)
    temp_turtle.color(color)
    temp_turtle.speed(speed)
    return temp_turtle


def draw_square(def_turtle, sidelength, x):
    def_turtle.pu()
    def_turtle.setx(x)
    def_turtle.pd()
    for var_x in range(0, 4):
        def_turtle.forward(sidelength)
        def_turtle.right(90)


def draw_circle(def_turtle, radius, x):
    def_turtle.pu()
    def_turtle.setx(x)
    def_turtle.pd()
    def_turtle.circle(radius)


def draw_triangle(def_turtle, sidelength, x):
    def_turtle.pu()
    def_turtle.setx(x)
    def_turtle.pd()
    for var_x in range(0, 3):
        def_turtle.forward(sidelength)
        def_turtle.right(120)



#set up window
window = turtle.Screen()
window.bgcolor("black")

#set up turtles
brad_pitt = create_turtle("circle", "blue", 2)
angie = create_turtle("turtle", "red", 2)
ufudu = create_turtle("classic", "green", 2)

#draw
draw_square(brad_pitt, 75, -150)
draw_circle(angie, 75, 0)
draw_triangle(ufudu, 75, 50)

window.exitonclick()
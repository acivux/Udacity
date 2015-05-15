__author__ = 'jannie'


import turtle


def create_turtle(shape, color, speed):
    temp_turtle = turtle.Turtle()
    temp_turtle.shape(shape)
    temp_turtle.color(color)
    temp_turtle.speed(speed)
    return temp_turtle


def draw_rhombus(def_turtle, sidelength, a, b):
    def_turtle.forward(sidelength)
    def_turtle.right(a)
    def_turtle.forward(sidelength)
    def_turtle.right(b)
    def_turtle.forward(sidelength)
    def_turtle.right(a)
    def_turtle.forward(sidelength)
    def_turtle.right(b)


#set up window
window = turtle.Screen()
window.bgcolor("black")

#set up turtles
brad_pitt = create_turtle("circle", "white", 7)

brad_pitt.pu()
brad_pitt.sety(-300)
brad_pitt.left(90)
brad_pitt.pd()
brad_pitt.forward(300)
brad_pitt.right(90)

for x in range(1,37):
    draw_rhombus(brad_pitt, 75, 60, 120)
    brad_pitt.right(10)


window.exitonclick()

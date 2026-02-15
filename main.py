# Case-study #1
# Developers: Burykhina E., Yasminskaya V.

import turtle

def square(x, y, a, color, angle=0):
    '''
    Function to draw a square.
    :param x: x-coordinate of the top-left corner
    :param y: y-coordinate of the top-left corner
    :param a: side length of the square
    :param color: color of the square
    :param angle: angle of the square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.setheading(angle)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(a)
        turtle.right(90)
    turtle.end_fill()

def circle(x, y, radius, color):
    '''
    Function to draw a circle.
    :param x: x-coordinate of the center
    :param y: y-coordinate of the center
    :param radius: radius of the circle
    :param color: color of the circle
    :return: None
    '''
    turtle.pu()
    turtle.goto(x, y - radius)  # идёт в нижнюю точку круга
    turtle.pd()

    turtle.fillcolor(color)

    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def rectangle(x, y, width, height, color):
    '''
    Function to draw a rectangle.
    :param x: x-coordinate of the bottom-left corner
    :param y: y-coordinate of the bottom-left corner
    :param width: width of the rectangle
    :param height: height of the rectangle
    :param color: color of the rectangle
    :return: None
    '''
    turtle.pu()
    turtle.goto(x, y)
    turtle.setheading(90)  # начинает с левого нижнего угла
    turtle.pd()

    turtle.fillcolor(color)

    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def parallelogram(x, y, width, height, angle, rotation_angle, color):
    '''
    Function to draw a parallelogram.
    :param x: x-coordinate of the bottom-left corner
    :param y: y-coordinate of the bottom-left corner
    :param width: width of the parallelogram
    :param height: height of the parallelogram
    :param angle: bottom-left angle
    :param rotation_angle: angle for the rotation of the parallelogram
    :param color: color of the parallelogram
    :return: None
    '''
    turtle.pu()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.setheading(rotation_angle)
    turtle.pd()

    turtle.fillcolor(color)

    turtle.begin_fill()
    for i in range(2):
        turtle.forward(height)
        turtle.right(angle)  # рисует с заданного левого нижнего угла
        turtle.forward(width)
        turtle.right(180 - angle)
    turtle.end_fill()

def rhombus(x, y, height, angle, color):
    '''
    Function to draw a rhombus.
    :param x: x-coordinate of the bottom-left corner
    :param y: y-coordinate of the bottom-left corner
    :param height: length of the side
    :param angle: bottom corner
    :param color: color of the rhombus
    :return: None
    '''
    turtle.pu()
    turtle.goto(x, y)
    turtle.setheading(180 - angle)
    turtle.pd()

    turtle.fillcolor(color)

    turtle.begin_fill()
    for i in range(2):
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def equilateral_triangle(x, y, a, color, angle=0):
    '''
    Function to draw a equilateral triangle.
    :param x: x-coordinate of the top point of the triangle
    :param y: y-coordinate of the top point of the triangle
    :param a: side length of the triangle
    :param color: color of the equilateral triangle
    :param angle: angle of the equilateral triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(angle)
    for _ in range(3):
        turtle.forward(a)
        turtle.left(120)
    turtle.end_fill()

def right_triangle(x, y, base, height, color, angle=0):
    '''
    Function to draw a right triangle.
    :param x: x-coordinate of the vertex of the triangle
    :param y: y-coordinate of the vertex of the triangle
    :param base: length of the base
    :param height: height of the triangle
    :param color: color of the right triangle
    :param angle: angle of the right triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.setheading(angle)
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward((base ** 2 + height ** 2) ** 0.5)
    turtle.end_fill()

def plane():

   rhombus(80, 100, 60, 45, 'yellow')
   right_triangle(165, 100, 60, 60, 'pink', 135)
   right_triangle(80, 185, 120, 120, 'orange', -45)
   parallelogram(165,100,80,60, 45, 45, 'blue')
   right_triangle(245, 20, 80, 80, 'red', 90)
   right_triangle(207, 142, 120, 120, 'green', 0)
   equilateral_triangle(80,185,80,'purple', 0)

def car():

    square(270, -170, 60, 'green')
    square(310,-170,20, 'yellow')
    rectangle(210,-230,120,60,'blue')
    square(225, -140, 30, 'red')
    rectangle(30, -230, 80, 180, 'orange')
    right_triangle(210,-150, 130, 130, 'yellow',135)
    circle(100,-270,40, 'pink')
    circle(250,-270,40, 'pink')

def butterfly():
    right_triangle(-300, 300, 120, 120, 'orange', 270)

    right_triangle(-240, 120, 60, 60, 'red', 90)
    square(-240, 180, 60, 'green')
    right_triangle(-180, 120, 60, 60, 'purple', 180)

    right_triangle(-180, 180, 120, 120, 'blue', 0)

    right_triangle(-180, 180, 85, 85, 'pink', -45)
    parallelogram(-180, 180, 60, 85, 45, -45, 'yellow')

def candle():
    right_triangle(-100, -300, 110, 110, 'blue', 135)

    right_triangle(-144, -186, 50, 50, 'purple', 225)
    right_triangle(-145, -115, 50, 50, 'red', 225)
    right_triangle(-222, -265, 110, 110, 'orange', 45)
    right_triangle(-233, -98, 75, 75, 'pink', -45)

    square(-205, -48, 50, 'green')
    parallelogram(-178, 50, 40, 65, 45, -75, 'yellow')

def main():
    butterfly()
    plane()
    candle()
    car()

    turtle.hideturtle()
    turtle.done()

main()
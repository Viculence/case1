# Case-study #1
# Developers: Burykhina E., Yasminskaya V.

import turtle

def square(x, y, a, color):
    '''
    Function to draw a square.
    :param x: x-coordinate of the top-left corner
    :param y: y-coordinate of the top-left corner
    :param a: side length of the square
    :param color: color of the square
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
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

    turtle.pencolor(color)
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

    turtle.pencolor(color)
    turtle.fillcolor(color)

    turtle.begin_fill()
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)
    turtle.end_fill()

def parallelogram(x, y, width, height, angle, color):
    '''
    Function to draw a parallelogram.
    :param x: x-coordinate of the bottom-left corner
    :param y: y-coordinate of the bottom-left corner
    :param width: width of the parallelogram
    :param height: height of the parallelogram
    :param angle: bottom-left angle
    :param color: color of the parallelogram
    :return: None
    '''
    turtle.pu()
    turtle.goto(x, y)
    turtle.setheading(angle)
    turtle.pd()

    turtle.pencolor(color)
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

    turtle.pencolor(color)
    turtle.fillcolor(color)

    turtle.begin_fill()
    for i in range(2):
        turtle.forward(height)
        turtle.right(angle)
        turtle.forward(height)
        turtle.right(180 - angle)
    turtle.end_fill()

def equilateral_triangle(x, y, a, color):
    '''
    Function to draw a equilateral triangle.
    :param x: x-coordinate of the top point of the triangle
    :param y: y-coordinate of the top point of the triangle
    :param a: side length of the triangle
    :param color: color of the equilateral triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(a)
        turtle.left(120)
    turtle.end_fill()

def right_triangle(x, y, base, height, color):
    '''
    Function to draw a right triangle.
    :param x: x-coordinate of the vertex of the triangle
    :param y: y-coordinate of the vertex of the triangle
    :param base: length of the base
    :param height: height of the triangle
    :param color: color of the right triangle
    :return: None
    '''
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(base)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(135)
    turtle.forward((base ** 2 + height ** 2) ** 0.5)
    turtle.end_fill()

def fish():
    # Мила
    pass

def car():
    # Мила
    pass

def butterfly():
    # Вика
    pass

def candle():
    # Вика
    pass

def main():
    fish()
    car()
    butterfly()
    candle()

    turtle.done()

main()

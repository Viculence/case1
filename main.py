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
    :param x: x-coordinate of the top-left center
    :param y: y-coordinate of the top-left center
    :param radius: radius of the circle
    :param color: color of the circle
    :return: None
    '''
    # Мила
    pass

def rectangle(x, y, width, height, color):
    '''
    Function to draw a rectangle.
    :param x: x-coordinate of the top-left corner
    :param y: y-coordinate of the top-left corner
    :param width: width of the rectangle
    :param height: height of the rectangle
    :param color: color of the rectangle
    :return: None
    '''
    # Мила
    pass

def parallelogram(x, y, base, heigh, angle, color):
    '''
    Function to draw a parallelogram.
    :param x: x-coordinate of the top-left corner
    :param y: y-coordinate of the top-left corner
    :param base: length of the base of the parallelogram
    :param heigh: height of the parallelogram
    :param angle: angle between the base and the sides
    :param color: color of the parallelogram
    :return: None
    '''
    # Мила
    pass

def rhombus(x, y, diagonal1, diagonal2, color):
    '''
    Function to draw a rhombus.
    :param x: x-coordinate of the top-left corner
    :param y: y-coordinate of the top-left corner
    :param diagonal1: length of the first diagonal
    :param diagonal2: length of the second diagonal
    :param color: color of the rhombus
    :return: None
    '''
    # Мила
    pass

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

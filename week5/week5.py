# import random
# for i in range(10):
#     number = random.randint(1,10)
#     print(number)
import math


# import random
# for i in range(10):
#     number = random.randint(25,36)
#     print(number)
#
# import math
# hypotenuse = math.hypot(3,4)
# print(hypotenuse)

# import math
# a = int(input("enter lenght: "))
# b = int(input("enter width: "))
# hypotenuse = math.sqrt(a**2 + b**2)
# print(hypotenuse)
#
# def areaOfCircle(radius):
#     return math.pi * radius**2
# print(areaOfCircle(1))


#
#
# import turtle
# screen = turtle.Screen()
# y = turtle.Turtle()
# def drawStar(y , side):
#     for i in range(5):
#         y.forward(side)
#         y.right(144)
#
# y.pensize(3)
# drawStar(y, 100)
# turtle.hideturtle()
# screen.exitonclick()
#
# import turtle
# y = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# y.color("pink")
# y.pensize(3)
#
# def drawSquare(y , side ):
#     for i in range(4):
#         y.forward(side)
#         y.right(90)
#
# for i in range(5):
#     drawSquare(y , 20)
#     y.penup()
#     y.forward(50)
#     y.pendown()
#
#
#
# y.hideturtle()
#
#
#
#
# screen.exitonclick()


import turtle
screen = turtle.Screen()
screen.bgcolor("lightgreen")
y = turtle.Turtle()
y.color("pink")
y.pensize(3)

def drawSquare(y, i):
    for i in range(4):
        y.forward(50)
        y.left(90)



for i in range(20, 120, 20):
    drawSquare(y , i)
    y.penup()
    y.backward(10)
    y.right(90)
    y.forward(10)
    y.left(90)
    y.pendown()






y.hideturtle()
screen.exitonclick()

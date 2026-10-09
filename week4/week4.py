# for i  in range(100):
#     print("We like python's turtles")
#
# months = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "August" , "September" , "October" , "November" , "December"]
#
# for month in months:
#      print("One of the months of the year is" , month)

# numbers = ["12", "10", "32", "3", "66", "17", "42", "99", "20"]
# for number in numbers:
#     print(number , "squared is" )

# import turtle
# t = turtle.Turtle()
# screen = turtle.Screen()
# t.penup()
# t.pendown()
# t.goto( x=-200, y=0)
#
# for i in range(3):
#     t.forward(80)
#     t.right(120)
# t.goto( x= -100, y=0)
# t.penup()
# t.pendown()
# for i in range(4):
#  t.forward(90)
#  t.right(90)
# t.penup()
# t.pendown()
#
# t.goto( x=20 , y=0)
# t.penup()
# t.pendown()
#
# for i in range(6):
#     t.forward(50)
#     t.right(60)
#
# t.goto( x=150 , y=0)
# t.penup()
# t.pendown()
# for i in range(8):
#     t.forward(50)
#     t.right(45)
#
# screen.exitonclick()
#

# import turtle
#
# y = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("light green")
# y.shape("turtle")
# y.color("blue")
# y.pensize(4)
# y.stamp()
#
# y.penup()
#
# for i in range(12):
#     y.forward(125)
#     y.pendown()
#     y.forward(15)
#
#     y.penup()
#     y.forward(25)
#     y.stamp()
#     y.backward(165)
#     y.left(30)
#
# screen.exitonclick()

import turtle
pirate = turtle.Turtle()
screen = turtle.Screen()
turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for angle in turns:
    pirate.left(angle)
    pirate.forward(100)
print("the current heading" , pirate.heading())
screen.exitonclick()







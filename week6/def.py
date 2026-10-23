# import turtle
#
# def drawPoly(t, num_sides, side_length):
#     for i in range(num_sides):
#         t.forward(side_length)
#         t.left(360/num_sides)
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# tess = turtle.Turtle()
# tess.color('hotpink')
# tess.pensize(3)
#
# drawPoly(tess, 8, 50)








































# import turtle
#
# def drawSpiral(t, angle):
#
#     length = 1
#     for i in range(84):
#         t.forward(length)
#         t.right(angle)
#         length = length + 2
#
#
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
#
# yasin = turtle.Turtle()
# yasin.color('blue')
#
#
# yasin.penup()
# yasin.backward(110)
# yasin.pendown()
#
#
# drawSpiral(yasin, 90)
#
#
#
# yasin.home()
# yasin.penup()
# yasin.forward(90)
# yasin.pendown()
#
# drawSpiral(guido, 89)
#
#
#
# def drawSpiral(someturtle,angle):
#     size = 1
#     for i in range(100):
#         someturtle.forward(size)
#         someturtle.right(angle)
#         size = size + 2






#
# import turtle
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# yasin = turtle.Turtle()
#
# def drawStar(someturtle, size):
#     for i in range(5):
#         someturtle.forward(size)
#         someturtle.right(144)
# yasin.pencolor("hotpink")
# for i in range(5):
#     drawStar(yasin, 50)
#     yasin.penup()
#     yasin.forward(350)
#     yasin.right(144)
#     yasin.pendown()






import turtle
wn = turtle.Screen()
wn.bgcolor("blue")
yasin = turtle.Turtle()
yasin.pencolor("black")
def drawSprite(someturtle,legs,length):
    angle = 360 / legs
    for i in range(legs):
        someturtle.forward(length)
        someturtle.backward(length)
        someturtle.left(angle)

    drawSprite(yasin,legs,length)

wn.exitonclick()
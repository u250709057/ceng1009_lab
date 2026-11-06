# def gradeMark(mark):
#     if mark >= 90:
#         return "A"
#     elif mark >= 80:
#         return "B"
#     elif mark >= 70:
#         return "C"
#     elif mark >= 60:
#         return "D"
#     else:
#         return "F"
#
#
#     marks={95,90,89,9,80,79,70,65,60,59.5,0}
#            for mark in marks:
#     print("Grade is" , gradeMark(mark))
# work = input("Enter your work ")
# gradeMark(work)

# import turtle
#
#
# def chooseColor(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t,height,gap):
#     t.penup()
#     t.left(90)
#     t.forward(height , gap)
#     t.write(" " + str(height))
#     t.backward(height + gap)
#     t.right(90)
#     t.pendown()
#
#     t.fillcolor(chooseColor(height))
#     t.begin_fill()
#     t.left(90)
#
#     t.forward(height)
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#
# def barChart(data):
#     max_height  = max(data)
#     num_bars = len(data)
#     border = 10
#     gap = (max_height +  border) / 25
#
#     wn = turtle.Screen()
#     wn.bgcolor("light green")
#     right = 40 + num_bars * border
#     top = max_height + 4 * border
#     wn.setworldcoordinates(border, border, right, top)
#
#     t = turtle.Turtle()
#     t.color("blue")
#     t.pensize(3)
#
#
#
#     for height in data:
#          drawBar(t,height,gap)
#
#
#
# data = [90,80,55,40,200,105,101]
# barChart(data)

#gem

# import turtle
#
# def get_color(height):
#     if height >= 200:
#         return "red"
#     elif height >= 100:
#         return "yellow"
#     else:
#         return "green"
#
# def drawBar(t, height):
#     """ Get turtle t to draw one bar of a given height. """
#     t.color("black", get_color(height)) # Outline black, fill based on height
#     t.begin_fill()
#     t.left(90)
#     t.forward(height)
#     t.write("  " + str(height))
#     t.right(90)
#     t.forward(40)
#     t.right(90)
#     t.forward(height)
#     t.left(90)
#     t.end_fill()
#     t.forward(10) # Gap between bars
#
# # Example usage:
# xs = [48, 117, 200, 240, 160, 90, -30] # Includes a negative value for Exercise 3
# wn = turtle.Screen()
# tess = turtle.Turtle()
# tess.pensize(3)
#
# for val in xs:
#     drawBar(tess, val)
#
# wn.exitonclick()

# import math
# def findHypot(a,b):
#     return math.sqrt(a**2 + b**2)
#
#
# print(findHypot(15,26))
# print(findHypot(3,4))


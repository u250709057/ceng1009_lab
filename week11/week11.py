# def fizz_buzz(n):
#     for i in range(1,n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
#
# print(fizz_buzz(16))
#
# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total= total + n%10
#         n = n // 10
#
#     return total
# print(digit_sum(1234))
#
# def alternate_case(s):
#     result =  ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result + s(i).upper()
#         else:
#             result = result + s(i).lower()
#     return result
#
# print(alternate_case("Hello world"))

# import turtle
# yasin = turtle.Turtle()
# screen = turtle.Screen()
# yasin.pensize(3)
# screen.bgcolor("lightgreen")
# colors = ["red","yellow","blue"]
#
# def draw_polygon(yasin, sides, length):
#     for i in range(sides):
#         yasin.forward(length)
#         yasin.left(360/sides)
#
# for i in range (3):
#     yasin.penup()
#     yasin.goto(-150 + i*120 ,-30)
#     yasin.pendown()
#     yasin.color(colors[i])
#     draw_polygon(yasin, i+3,60)
#
# yasin.hideturtle()
# screen.exitonclick()
#
# import turtle
# y = turtle.Turtle()
# screen  = turtle.Screen()
# y.pensize(2)
# screen.bgcolor("lightgreen")
#
# def filled_square(y,size,color):
#     y.fillcolor(color)
#     y.begin_fill()
#     for i in range(4):
#         y.forward(size)
#         y.left(90)
#     y.end_fill()
#
# for i in range(5):
#     y.penup()
#     y.goto(-165 +i*70,-25)
#     y.pendown()
#     if i % 2 == 0:
#         filled_square(y,50,"red")
#     else:
#         filled_square(y,50,"blue")
#
# import turtle
# y = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# y.pensize(3)
# def draw_square(y,size):
#     for i in range(4):
#         y.forward(size)
#         y.left(90)
#
#
# for i in range(12):
#     draw_square(y,80)
#     y.penup()
#     y.goto(0,0)
#     y.pendown()
#     y.left(30)


import turtle
y= turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("lightgreen")
y.pensize(1)
size=40
def draw_square(y, size,filled):
    if filled:
        y.begin_fill()
    for i in range(4):
        y.forward(size)
        y.left(90)
    if filled:
       y.end_fill()

for row in range(6):
    for col in range(6):
        y.penup()
        y.goto(-120 + col * size,-120 + row * size)
        y.pendown()
        draw_square(y,size,(row +col)  % 2 == 0)




y.hideturtle()
screen.exitonclick()
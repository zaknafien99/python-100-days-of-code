import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list = [(251, 251, 248), (238, 246, 241), (248, 233, 238), (196, 169, 98), (242, 246, 250), (130, 177, 191),
               (160, 57, 77), (231, 219, 123), (51, 112, 163), (110, 91, 85), (138, 184, 127), (212, 152, 170),
               (67, 124, 76), (93, 124, 179), (86, 163, 95), (195, 69, 90), (150, 32, 47), (64, 53, 49),
               (204, 118, 46), (221, 170, 182), (151, 118, 108), (74, 59, 57), (157, 203, 217), (176, 205, 181),
               (222, 178, 169), (94, 139, 157), (86, 30, 37), (172, 189, 216), (33, 68, 96)]

tim.setheading(225)
tim.forward(380)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()

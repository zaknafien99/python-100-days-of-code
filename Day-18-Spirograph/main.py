# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle as t
import random


tim = t.Turtle()
t.colormode(255)

def random_color():
    # Use a breakpoint in the code line below to debug your script.
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading((tim.heading() + size_of_gap))

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# import another_module
#
# print(another_module.another_variable)
#
# from turtle import Turtle, Screen
#
# timmy = Turtle()  # create a new turtle object
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = 'l'

print(table)

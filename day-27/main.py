import tkinter
from tkinter import *

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))  # create a label
my_label.config(text="New Text")
# my_label.pack(side="left")  # show the window
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)

my_label["text"] = "New Text"


# button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=2)
#button.pack()

# Entry
input = Entry(width=10)
#input.pack()
print(input.get())
input.grid(column=2, row=2)

window.mainloop()

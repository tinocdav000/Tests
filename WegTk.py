#Wegscheid Tkiner intro

from tkinter import *
from tkinter import ttk

# Setup Window
myWindow = Tk()
myWindow.title("STRINGSSTRINGSSTRINGSSTRINGSSTRINGSSTRINGSSTRINGSSTRINGSSTRINGS")
myWindow.configure(background="#FFFFFF")


# Label(myWindow, text="Hello Succer!",bg="#0000FF", fg="#00FF00"  ,font="Times 160 bold underline italic").pack()
Label(myWindow, text="Hello Succer!",bg="#FFFFFF", font="none 12 bold").pack()

# Widget
B1 = ttk.Button(myWindow, text="Exit", command=myWindow.destroy)
B1.pack()

# Main loop
myWindow.geometry("300x200+400+350")
myWindow.mainloop()

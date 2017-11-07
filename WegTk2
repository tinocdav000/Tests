# BUTT(ONS)

from tkinter import *

# main window setup
root = Tk()
root.title("Iba")
root.geometry('300x200+250+250')

# Variables
C1 = 0

# functions
def f1():
    global C1
    C1 += 1
    L1.configure(text='f1')
    print("rawr", C1)

def f2():
    global C1
    C1 -= 1
    L1.configure(text=C1)
    print('why', C1)

# widgets
L1 = Label(root, text="nothing")
b1 = Button(root, text='THIS MAY BE A BUTTON', command=f1)
b2 = Button(root, text='this may be a button', command=f2)
L1.pack()
b1.pack(side='left')
b2.pack(side='left')

# Main loop
root.mainloop()
